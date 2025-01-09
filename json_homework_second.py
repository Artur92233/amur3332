import requests


url = 'http://api.open-notify.org/astros.json'

params = {}

response = requests.get(url, params=params)
response_json = response.json()


people = response_json['people']


how_many_people_in_iss = []


for human in people:
    if human['craft'] == 'ISS':
        how_many_people_in_iss.append(human['name'])


result = ', '.join(how_many_people_in_iss)

print(result)
