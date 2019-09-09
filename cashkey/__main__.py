import os
import sys
import colorama
try:
    from .wallet import Wallet
    from .usb import read_drive, register_drive
except Exception:
    from wallet import Wallet
    from usb import read_drive, register_drive

# DANGER ZONE: setting testing to True will overwrite you private key
# use another usb flash drive to use the Testnet
testing = False

# colors
colorama.init()

# init wallet
wallet = Wallet(testing=testing)

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def prompt():
    cls()
    print("")
    print(colorama.Fore.GREEN+"Select an option: ")
    print(colorama.Fore.WHITE+"")
    print("1 – Print your bitcoin cash address")
    print("2 – Get your wallet balance in a given currency")
    print("3 – Get your transaction history")
    print("4 – Make a transaction")
    print("5 – Get transaction fees in satoshis per byte")
    print("6 – Create a new wallet"+colorama.Fore.RED+" (Danger zone!)")
    print(colorama.Fore.WHITE+"0 – Exit")
    print("")
    decision = input("")
    return decision

def selcurrency():
    print("")
    print(colorama.Fore.GREEN+"Select a currency (1 - 5): ")
    print(colorama.Fore.WHITE+"")
    print("1 – BCH")
    print("2 – USD")
    print("3 – EUR")
    print("4 – GBP")
    print("5 – JPY")
    print("")
    decision = input("")
    if decision == '1':
        currency = 'bch'
    elif decision == '2':
        currency = 'usd'
    elif decision == '3':
        currency = 'eur'
    elif decision == '4':
        currency = 'gbp'
    elif decision == '5':
        currency = 'jpy'
    else:
        currency = 'usd'
    return currency

def main(args=None):
    if args is None:
        args = sys.argv[1:]

    user_input = prompt()
    if user_input == '6':
        register_drive(testing)
    elif user_input == '1':
        print("")
        print(colorama.Fore.GREEN+"Bitcoin cash address: "+colorama.Fore.WHITE+wallet.bch_address())
    elif user_input == '2':
        cls()
        currency = selcurrency()
        print(colorama.Fore.GREEN+'BALANCE: '+colorama.Fore.WHITE+wallet.bch_balance(currency) + " "+currency.upper())
    elif user_input == '3':
        cls()
        wallet.bch_history()
        print("")
    elif user_input == '4':
        cls()
        currency = selcurrency()
        cls()
        print("Please select an amount in "+currency.upper()+" to send:")
        print("")
        amount = input("amount: ")
        cls()
        print("Paste or write the recipient address here:")
        print("")
        address = input("address: ")
        print("")
        wallet.transaction(recipient_addr=address, amount=float(amount), currency=currency)
    elif user_input == '5':
        print("")
        print(colorama.Fore.GREEN+"Transaction fees: ")
        print(colorama.Fore.WHITE+str(wallet.bch_tx_fee())+' satoshis/byte')
    elif user_input == '0':
        exit()
    else:
        print(colorama.Fore.RED+"Please enter a number between 0 and 6")
        exit()

if __name__ == "__main__":
    main()
