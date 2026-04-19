import requests

def fetch_emails():
    url = "http://127.0.0.1:8000/emails"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Error al obtener emails")