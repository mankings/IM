import requests
import json
from time import sleep

if __name__ == '__main__':
    api_url = "http://localhost:5000/misc/save_game"
    
    body = {
        "text": "Guarda o jogo"
    }
    
    response = requests.post(api_url, json={})
    
    for key in response.json():
        print(key)
        print(response.json()[key])
        