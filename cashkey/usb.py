from cryptography.fernet import InvalidToken
from bitcash import Key, PrivateKeyTestnet
import colorama
import getpass
import qrcode
import sys
import os

try:
    from encrypt import genkey, encrypt_prkey, decrypt_prkey
except ImportError:
    from .encrypt import genkey, encrypt_prkey, decrypt_prkey


# operating system
if sys.platform == 'darwin':
    keypath = '/Volumes/BCH/'
elif sys.platform == 'linux':
    keypath = '/media/BCH/'
elif sys.platform == 'win32' or 'cygwin':
    keypath = 'd:/BCH/' # assuming it's mounted in letter d // not tested


# generate a new private key and encrypt it on usb drive
def register_drive(testing=False):
    if os.path.exists(keypath+'key.enc') == True:
        print("")
        print(colorama.Fore.RED+"WARNING:")
        print("")
        print(colorama.Fore.WHITE+"A wallet already exists in this usb drive. Deleting it will result in the loss of all your funds.")
        print("")
        print("Would you really like to continue and delete your current wallet? yes | no")
        print("")
        decision = input("")
        if decision == 'no':
            print(colorama.Fore.RED+"Operation aborted")
            exit()
        elif decision == 'yes':
            pass
        else:
            print(colorama.Fore.RED+"Operation aborted")
            exit()
    os.system('cls' if os.name=='nt' else 'clear')
    passwd = getpass.getpass("Set a strong password to access your wallet: ")
    passwd_repeat = getpass.getpass("Retype password to confirm: ")

    if passwd != passwd_repeat:
        print(colorama.Fore.RED+"Passwords don't match. Please retry.")
        exit()
    
    if testing == True:
        private_key = PrivateKeyTestnet()
    elif testing == False:
        private_key = Key()

    bch_private_key = private_key.to_wif()

    generated_key = genkey(passwd)
    encrypted = encrypt_prkey(bch_private_key, generated_key)

    try:
        with open(keypath+'key.enc', 'wb') as f:
            f.write(encrypted)
    except FileNotFoundError:
        print(colorama.Fore.RED+"Please insert a USB flash drive named BCH and retry.")
        exit()
    address_qr = qrcode.make(private_key.address)
    address_qr.save(keypath+'address.png')
    print(colorama.Fore.GREEN+'The private key has been registred and encrypted successfully on your USB flash drive.')

# return decrypted private key from usb drive
def read_drive(testing):
    # verify if drive is registred
    if os.path.exists(keypath+'key.enc') == False:
        print(colorama.Fore.GREEN+'New USB Drive detected.')
        print("")
        register_drive(testing=testing)
        print("")
        print(colorama.Fore.GREEN+"Please relaunch the program to continue.")
        exit()

    passwd = getpass.getpass("Type your wallet password: ")
    generated_key = genkey(passwd)

    try:
        with open(keypath+'key.enc', 'rb') as f:
            encr_prkey = f.read()
    except FileNotFoundError:
        print(colorama.Fore.RED+"Please insert your USB flash drive and retry.")
        exit()

    try:
        decrypted = decrypt_prkey(encr_prkey, generated_key)
    except InvalidToken:
        print("Invalid password...")
        exit()

    return decrypted.decode("utf-8") 

