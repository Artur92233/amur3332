import json
import requests


url = 'http://api.open-notify.org/astros.json'

params = {}

response = requests.get(url, params=params)
response_json = response.json()


with open('json_data.json', mode='w', encoding='utf-8') as file:
    json.dump(response_json, file, indent=4)
