import requests

url = 'https://www.xe.com/currencyconverter/'

params = {
    'limit': 500,
    'skip': 0
}

response = requests.get(url, params=params)
response_json = response.json()

valutes = response_json['USD']


for valute in valutes:
    if valute['age'] < 30:
        people_younger_thirty += 1
    if user['gender'] == 'female' and user['eyeColor'] == 'Green':
        female_with_green_eyes += 1
    if user['address']['city'] == 'San Francisco':
        people_live_in_san_francisco += 1


