import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

def genkey(password_provided):
    password = password_provided.encode()
    salt = b'\xc9F\xbc\xa0A\x18\x92j\xdd\xcev\xd3ju\x9e\x03'

    kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
            )

    key = base64.urlsafe_b64encode(kdf.derive(password))
    return key

def encrypt_prkey(prkey, key):
    prkey = prkey.encode()
    f = Fernet(key)
    encrypted = f.encrypt(prkey)
    return encrypted

def decrypt_prkey(encrypted, key):
    f = Fernet(key)
    decrypted = f.decrypt(encrypted)
    return decrypted
