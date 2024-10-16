import requests

def get_service_a_response():
    url = "https://expired.badssl.com/"
    try:
        response = requests.get(url, verify=False)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        return {'error': str(e)}
