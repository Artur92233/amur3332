import json
import requests

data =

with open('json_data.json', mode='w', encoding='utf-8') as file:
    json.dump(data, file, indent=4)
