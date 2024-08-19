import base64
import os
import requests

secret_name = os.environ['SECRET_NAME']
new_secret_value = os.environ['NEW_SECRET_VALUE']
token = os.environ['GITHUB_TOKEN']

# Codificando o novo valor do segredo para base64
new_secret_value_encoded = base64.b64encode(new_secret_value.encode()).decode()

# Obter o SHA do segredo atual
repo = os.environ['REPO']
url = f'https://api.github.com/repos/{repo}/actions/secrets/{secret_name}'

response = requests.get(url, headers={'Authorization': f'token {token}'})
if response.status_code == 200:
    secret_info = response.json()
    secret_sha = secret_info['key_id']

    # Atualizar o segredo
    update_url = f'https://api.github.com/repos/{repo}/actions/secrets/{secret_name}'
    payload = {
        'encrypted_value': new_secret_value_encoded,
        'key_id': key_id
    }
    response = requests.put(update_url, json=payload, headers={'Authorization': f'token {token}'})
    if response.status_code == 201:
        print('Segredo atualizado com sucesso!')
    else:
        print('Erro ao atualizar o segredo:', response.json())
else:
    print('Erro ao obter o segredo:', response.json())
