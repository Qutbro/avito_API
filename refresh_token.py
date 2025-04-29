import requests
import json
import time
import os
import subprocess
import sys
from colorama import init, Fore, Back, Style
import time
from config import CLIENT_ID, CLIENT_SECRET

TOKEN_URL = 'https://api.avito.ru/token/'


def get_access_token(client_id, client_secret):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret
    }

    response = requests.post(TOKEN_URL, headers=headers, data=data)
    response_data = response.json()

    if response.status_code == 200:
        return response_data['access_token']
    else:
        raise Exception(f"Error getting access token: {response_data}")


def save_token_to_file(token, filename='access_token.json'):
    token_data = {
        'access_token': token,
        'timestamp': int(time.time())
    }
    with open(filename, 'w') as file:
        json.dump(token_data, file)


def load_token_from_file(filename='access_token.json'):
    try:
        with open(filename, 'r') as file:
            token_data = json.load(file)
            return token_data
    except FileNotFoundError:
        return None


def is_token_expired(token_data, expiry_time=86400):
    current_time = int(time.time())
    token_age = current_time - token_data['timestamp']
    return token_age > expiry_time


def main():
    token_data = load_token_from_file()

    if token_data is None or is_token_expired(token_data):
        print("Fetching new access token...")
        access_token = get_access_token(CLIENT_ID, CLIENT_SECRET)
        save_token_to_file(access_token)
        print(f"New access token saved: {access_token}")
    else:
        print(f"Access token is still valid: {token_data['access_token']}")
    process = subprocess.Popen([sys.executable, "avito.py"])
    process.wait()


if __name__ == '__main__':
    main()
