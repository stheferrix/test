import requests
import base64
import os

# Prepare o valor do segredo
new_secret_value = os.environ['NEW_SECRET_VALUE']
encoded_value = base64.b64encode(new_secret_value.encode()).decode()

# URL para a API do GitHub
url = f"https://api.github.com/repos/{os.environ['REPO']}/actions/secrets/{os.environ['SECRET_NAME']}"

# Cabeçalhos da requisição
headers = {
  'Authorization': f'token {os.environ["GITHUB_TOKEN"]}',
  'Accept': 'application/vnd.github.v3+json'
}

# Obter a chave pública para encriptação

key_id = os.environ['KEY_ID']
public_key = os.environ['PUBLIC_ID']

# Encriptar o novo valor do segredo
from cryptography.fernet import Fernet
import json

# Criar um Fernet com a chave pública
fernet = Fernet(public_key.encode())
encrypted_value = fernet.encrypt(encoded_value.encode())

# Atualizar o segredo
data = {
  'encrypted_value': encrypted_value.decode(),
  'key_id': key_id
}

requests.put(url, headers=headers, json=data)
