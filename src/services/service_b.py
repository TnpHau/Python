import requests

def post_service_b_data(data):

    username = data.get('username')
    password = data.get('password') 

    if not username or not password:
        return {'error': 'Username and password are required'}

    payload = {
        'username': username,
        'password': password
    }

    url = "http://httpbin.org/post"
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {'error': str(e)}
