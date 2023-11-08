import requests
import json
from time import sleep

if __name__ == '__main__':
    api_url = "http://localhost:5000/movement/player_move"
    
    body = {
        "direction": 'baixo',
        "unit": 5
    }
    
    response = requests.post(api_url, json=body)
    
    print(response)