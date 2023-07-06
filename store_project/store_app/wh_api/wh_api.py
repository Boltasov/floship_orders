import requests
import posixpath


def create_user(name, password, wh_url, users_path):
    user_creds = {
        "username": name,
        "password": password,
    }

    create_wh_user_url = posixpath.join(wh_url, users_path)

    response = requests.post(create_wh_user_url, data=user_creds)
    print(response.request.body)
    response.raise_for_status()
    return response.status_code


def get_token(name, password, wh_url, get_token_path):
    user_creds = {
        "username": name,
        "password": password,
    }

    auth_wh_url = posixpath.join(wh_url, get_token_path)

    response = requests.post(auth_wh_url, data=user_creds)
    response.raise_for_status()

    token = response.json()['auth_token']
    return token


def create_store_account(wh_url, accounts_path, token, store_token):
    create_store_account_url = posixpath.join(wh_url, accounts_path)

    headers = {
        'Authorization': f'Token {token}'
    }
    store = {
        'name': 'store_1',
        'token': f'Token {store_token}',
    }

    response = requests.post(create_store_account_url, headers=headers, data=store)
    print('Header:', response.request.headers)
    print('Body:', response.request.body)
    response.raise_for_status()
    return response.status_code


def create_order(order_serialized, wh_url, orders_path, token):
    wh_url = posixpath.join(wh_url, orders_path)
    headers = {
        'Authorization': token
    }

    response = requests.post(wh_url, headers=headers, data=order_serialized.data)
    response.raise_for_status()
    return response.status_code
