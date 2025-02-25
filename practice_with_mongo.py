from pprint import pprint

from bson import ObjectId
from oauthlib.uri_validate import query

from config import uri

from pymongo.mongo_client import MongoClient

client = MongoClient(uri)

db = client.store

collection_store = db.products

products_to_add = [
    {"name": "Laptop", "price": 50000, "quantity": 5, "category": "Electronics"},
    {"name": "Sneakers", "price": 7000, "quantity": 12, "category": "Clothing"},
    {"name": "Book", "price": 1200, "quantity": 20, "category": "Books"},
    {"name": "Headphones", "price": 3500, "quantity": 15, "category": "Electronics"},
    {"name": "Guitar", "price": 15000, "quantity": 3, "category": "Musical Instruments"},
    {"name": "Kettle", "price": 2500, "quantity": 10, "category": "Home Appliances"}

]

collection_store.insert_many(products_to_add)

all_products = collection_store.find()
for product in all_products:
    pprint(product)

wanted_name_milk = collection_store.find_one({"name": "Laptop"})
print(wanted_name_milk)

query = {'price': {'$gt': 50}}
all_products = collection_store.find(query)
for product in all_products:
    pprint(product)

query_one = {"name": {'$regex': 'S*'}}
all_products = collection_store.find(query_one)
for product in all_products:
    pprint(product)

query_two = {}
all_products = collection_store.find(query_two).limit(3).sort("quantity", -1)
for product in all_products:
    pprint(product)

query_three = {"category": "Clothing"}
new_data = {"$set": {"category": "Electronics"}}
collection_store.update_one(query_three, new_data)

query_four = {}
new_dataa = {"$inc": {"quantity": 5}}
collection_store.update_one(query_four, new_dataa)

query_five = {}
neww_dataa = {"$mul": {"price": 0.5}}
collection_store.update_one(query_five, neww_dataa)

query_six = {"quantity": 0}
operation = {"$unset": {"warranty": 1}}

query_seven = {"_id": ObjectId("67b749a782e872aafb776853")}
operation_one = {"$unset": {"warranty": 1}}
