from bitcash import Key, PrivateKeyTestnet
from bitcash.network import get_fee
from bitcash.exceptions import InsufficientFunds
import colorama
from halo import Halo
import re

try:
    from usb import read_drive
except ImportError:
    from .usb import read_drive

# colors
colorama.init()

# spinner
spinner = Halo(text='Please wait ...', spinner='dots')

class Wallet:
    def __init__(self, testing=False, unittest_prkey=''):
        if testing == True:
            self.testing = testing
            self.private_key = read_drive(testing)
            self.key = PrivateKeyTestnet(self.private_key)
        elif unittest_prkey != '':
            self.testing = testing
            self.private_key = unittest_prkey
            self.key = Key(self.private_key)
        else:
            self.testing = testing
            self.private_key = read_drive(testing)
            self.key = Key(self.private_key)

    def bch_address(self):
        return self.key.address

    def bch_segwit_address(self):
        return self.key.segwit_address

    def bch_balance(self, currency="bch"):
        spinner.start()
        balance = self.key.get_balance(currency)
        spinner.stop()
        return balance

    def bch_history(self):
        spinner.start()
        transactions = self.key.get_transactions()
        spinner.stop()
        print("")
        print(colorama.Fore.GREEN+str(len(transactions))+ " transactions:")
        print("")
        for transaction in transactions:
            print("[ "+transaction+" ]")

    # perform a transaction
    def transaction(self, recipient_addr, amount, currency):
        cashaddr = re.match('^((bitcoincash:)?(q|p)[a-z0-9]{41})', recipient_addr)
        legacyaddr = re.match('^([13][a-km-zA-HJ-NP-Z1-9]{25,34})', recipient_addr)
        caplegacyaddr = re.match('^((BITCOINCASH:)?(Q|P)[A-Z0-9]{41})$', recipient_addr)
        if not any([cashaddr, legacyaddr, caplegacyaddr]):
            print(colorama.Fore.RED+"Transaction aborted: Invalid bitcoin cash address.")
            exit()
        print('You are about to send {} {} to {}'.format(str(amount), currency.upper(), recipient_addr))

        amount_left = float(self.bch_balance(currency)) - amount
        if amount_left <= 0:
            print(colorama.Fore.RED+'You don\'t have enough funds to perform the transaction.')
            exit()

        if currency == 'usd':
            print("You will have ${} left on your wallet.".format(str(amount_left)))
        elif currency == 'bch':
            print("You will have {} BCH left on your wallet.".format(str(amount_left)))
        elif currency == 'eur':
            print("You will have {}€ left on your wallet.".format(str(amount_left)))
        elif currency == 'gbp':
            print("You will have £{} left on your wallet.".format(str(amount_left)))
        elif currency == 'jpy':
            print("You will have ¥{} left on your wallet.".format(str(amount_left)))
        print("")
        decision = input('Are you sure you want to perform this transaction? yes | no\n')
        if decision != 'yes':
            print("")
            print(colorama.Fore.RED+'Transaction aborted')
            exit()
        else:
            try:
                spinner.start()
                transaction_id = self.key.send([(recipient_addr, amount, currency)])
                spinner.stop()
                print(colorama.Fore.GREEN+'Success: '+colorama.Fore.WHITE+transaction_id)
            except InsufficientFunds:
                print(colorama.Fore.RED+'You don\'t have enough funds to perform the transaction.')
            

    def bch_tx_fee(self):
        fee = get_fee()
        return fee
