# TODO: Improve this mess
import pytest
from cashkey.encrypt import genkey, encrypt_prkey, decrypt_prkey

def test_genkey():
    generated = genkey('test')
    key =  b'OpbG4DyGjgEnS_GS43XULswuofM2GySQnasLGSUkOgg='
    assert generated == key
    generated_two = genkey('test')
    assert generated_two == key

def test_encrypt_decrypt():
    key =  b'OpbG4DyGjgEnS_GS43XULswuofM2GySQnasLGSUkOgg='
    prkey = "5KWTi8xHwof7TPPfu7BGg857zucEVmimMr6Ko9ooZQyg7tifH7G"
    # encrypt
    encrypted = encrypt_prkey(prkey, key)
    encrypted_two = encrypt_prkey(prkey, key)
    assert encrypted != encrypted_two
    # decrypt
    decrypted = decrypt_prkey(encrypted, key)
    assert decrypted.decode("utf-8") == prkey
