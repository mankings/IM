import requests
from time import sleep

if __name__ == '__main__':
    # Replace this URL with the URL of your dummy API
    api_url = "http://localhost:5000/"
    # Send a GET request to the API
    response = requests.get(api_url + "player_run")
    print(response)
    sleep(1.1)
    response = requests.get(api_url + "player_stop")
    print(response)
