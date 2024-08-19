import os
import sys
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def encrypt_secret(public_key, secret):
    key = RSA.import_key(base64.b64decode(public_key))
    cipher = PKCS1_OAEP.new(key)
    encrypted_secret = cipher.encrypt(secret.encode())
    return base64.b64encode(encrypted_secret).decode()

def main():
    secret_value = os.getenv('secret_value')
    public_key = os.getenv('public_key')
    key_id = os.getenv('key_id')

    encrypted_value = encrypt_secret(public_key, secret_value)
    print(f"::set-output name=encrypted_value::{encrypted_value}")

if __name__ == "__main__":
    main()
