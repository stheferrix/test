import requests
import base64
import os

print("testando")

new_secret_value = os.environ['NEW_SECRET_VALUE']
key_id = os.environ['KEY_ID']
public_key = os.environ['PUBLIC_KEY']

print('VALOR =', new_secret_value )

encoded_value = base64.urlsafe_b64encode(new_secret_value.encode('utf-8')).decode()

url = f"https://api.github.com/repos/{os.environ['REPO']}/actions/secrets/{os.environ['SECRET_NAME']}"

headers = {
    'Authorization': f'token {os.environ["GITHUB_TOKEN"]}',
    'Accept': 'application/vnd.github.v3+json'
}

from cryptography.fernet import Fernet
import json

fernet = Fernet(public_key.encode('utf-8'))
encrypted_value = fernet.encrypt(encoded_value.encode('utf-8'))

data = {
    'encrypted_value': encrypted_value.decode('utf-8'),
    'key_id': key_id
}

requests.put(url, headers=headers, json=data)                    
