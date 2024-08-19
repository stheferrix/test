import requests
import base64
import os

print("testando")

new_secret_value = os.environ['NEW_SECRET_VALUE']
encoded_value = base64.b64encode(new_secret_value.encode()).decode()

url = f"https://api.github.com/repos/{os.environ['REPO']}/actions/secrets/{os.environ['SECRET_NAME']}"

headers = {
    'Authorization': f'token {os.environ["GITHUB_TOKEN"]}',
    'Accept': 'application/vnd.github.v3+json'
}

response = requests.get(f"https://api.github.com/repos/{os.environ['REPO']}/actions/secrets/public-key", headers=headers)
public_key_info = response.json()
key_id = public_key_info['key_id']
public_key = public_key_info['key']

from cryptography.fernet import Fernet
import json

fernet = Fernet(public_key.encode())
encrypted_value = fernet.encrypt(encoded_value.encode())

data = {
    'encrypted_value': encrypted_value.decode(),
    'key_id': key_id
}

requests.put(url, headers=headers, json=data)
                    
