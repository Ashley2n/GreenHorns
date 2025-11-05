import os

from cryptography.fernet import Fernet


def load_key() -> bytes:
    _key_file = 'key.txt'

    if os.path.exists(_key_file):
        with open(_key_file, 'rb') as f:
            key = f.read()
    else:
        key = Fernet.generate_key()
        with open(_key_file, 'wb') as f:
            f.write(key)

    return key


def encrypt_password(password: str) -> bytes:
    return fernet.encrypt(password.encode())

def decrypt_password(encrypted_password: bytes) -> str:
    return fernet.decrypt(encrypted_password).decode()



fernet = Fernet(load_key())