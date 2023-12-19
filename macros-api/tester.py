import requests
import json
from time import sleep

if __name__ == '__main__':
    api_url = "http://localhost:5000/misc/start_game"
    
    body = {
    }
    
    response = requests.post(api_url, json=body)
    
    print(response)