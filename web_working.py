import requests

url = 'https://dummyjson.com/users'

params = {
    'limit': 500,
    'skip': 0
}

response = requests.get(url, params=params)
response_json = response.json()

users = response_json['users']
people_younger_thirty = 0
female_with_green_eyes = 0
people_live_in_san_francisco = 0

for user in users:
    if user['age'] < 30:
        people_younger_thirty += 1
    if user['gender'] == 'female' and user['eyeColor'] == 'Green':
        female_with_green_eyes = + 1
    if user['address']['city'] == 'San Francisco':
        people_live_in_san_francisco = + 1

print(f'Кількість людей яким менше тридцяти --> {people_younger_thirty}')
print(f'Кількість жінок які мають зелені очі --> {female_with_green_eyes}')
print(f'Кількість людей , що живуть у Сан Франциско --> {people_live_in_san_francisco}')
