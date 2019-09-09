#TODO: improve this mess
import pytest
import sys
import os
from cashkey.wallet import Wallet


prkey = 'Kxr9tQED9H44gCmp6HAdmemAzU3n84H3dGkuWTKvE23JgHMW8gct' 
wallet = Wallet(testing=False, unittest_prkey=prkey)

def test_bch_address():
    address = wallet.bch_address()
    assert address == 'bitcoincash:qpvhecpzh25gw7ve28syjmrknkwvp36ems5cc43vh8'

def test_bch_balance():
    balance = wallet.bch_balance("bch")
    assert float(balance) >= 0

