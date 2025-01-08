import requests

url = 'http://api.open-notify.org/astros.json'

params = {
    'limits' : 12
}


response = requests.get(url, params=params)
response_json = response.json()


people = response_json['people']
how_many_people_in_iss = 0
pass

for human in people:
    if human['craft'] == 'ISS':
        how_many_people_in_iss += 1



result = f'На момент запуску коду знаходяться на міжнародній космічній станції --> {how_many_people_in_iss} людей.'
print(result)
