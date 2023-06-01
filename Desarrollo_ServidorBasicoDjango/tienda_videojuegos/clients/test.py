import requests

endpoint ='http://localhost:8000/videojuego/PS5'
response = requests.get(endpoint)

print(response.json())