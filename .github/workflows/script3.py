import base64
import json
import os
import requests
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Configurações
GITHUB_TOKEN = os.environ['GITHUB_TOKEN']
REPO = os.environ['REPO']
SECRET_NAME = os.environ['SECRET_NAME']
SECRET_VALUE = os.environ['NEW_SECRET_VALUE']
PUBLIC_KEY = os.environ['PUBLIC_KEY']
KEY_ID = os.environ['KEY_ID']

# Função para criptografar o segredo
def encrypt_secret(secret_value, public_key):
    # Carregando a chave pública
    rsa_key = RSA.import_key(base64.b64decode(public_key))
    cipher = PKCS1_OAEP.new(rsa_key)
    
    # Criptografando o valor do segredo
    encrypted_value = cipher.encrypt(secret_value.encode())
    return base64.b64encode(encrypted_value).decode()

# Função para atualizar o segredo no GitHub
def update_secret(encrypted_value):
    url = f'https://api.github.com/repos/{REPO}/actions/secrets/{SECRET_NAME}'
    headers = {
        'Authorization': f'token {GITHUB_TOKEN}',
        'Accept': 'application/vnd.github.v3+json',
    }
    data = {
        'encrypted_value': encrypted_value,
        'key_id': KEY_ID,
    }
    response = requests.put(url, headers=headers, data=json.dumps(data))
    response.raise_for_status()  # Levanta um erro se a requisição falhar
    print('Segredo atualizado com sucesso!')

# Execução
if __name__ == '__main__':
    # Criptografar o valor do segredo
    encrypted_value = encrypt_secret(SECRET_VALUE, PUBLIC_KEY)
    
    # Atualizar o segredo no GitHub
    update_secret(encrypted_value)
    
    # Atualizar o segredo no GitHub
    update_secret(public_key_info, encrypted_value)
