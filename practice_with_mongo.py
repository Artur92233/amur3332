from config import uri

from pymongo.mongo_client import MongoClient

client = MongoClient(uri)

db = client.shop

collection_laptops_initial = db.laptops

laptops_to_add =[
    {'brand': 'Apple','model': 'MacBook Pro 16','price': 2500,'year': 2023,'specs': {'cpu': 'M2 Max', 'ram': '32GB', 'storage': '1TB SSD'}},
    {'brand': 'Dell','model': 'XPS 15','price': 1800,'year': 2022,'specs': {'cpu': 'Intel i7-12700H', 'ram': '16GB', 'storage': '512GB SSD'}},
    {'brand': 'ASUS','model': 'ROG Zephyrus G14','price': 2000,'year': 2023,'specs': {'cpu': 'AMD Ryzen 9 6900HS', 'ram': '32GB', 'storage': '1TB SSD'}},
    {'brand': 'Lenovo','model': 'ThinkPad X1 Carbon','price': 2200,'year': 2023,'specs': {'cpu': 'Intel i7-1365U', 'ram': '16GB', 'storage': '1TB SSD'}}
]


collection_laptops_initial.insert_many(laptops_to_add)

first_laptop = collection_laptops_initial.find_one()

wanted_laptop = collection_laptops_initial.find_one({'price': 2000})
print(wanted_laptop)

wanted_laptop_brand_and_model = collection_laptops_initial.find_one({'brand': 'Apple','model': 'MacBook Pro 16'})
print(wanted_laptop_brand_and_model)
