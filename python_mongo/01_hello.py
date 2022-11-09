from pymongo import MongoClient


# client = MongoClient("localhost", 27017)
client = MongoClient("mongodb://localhost:27017")

# db = client.test
db = client["test"]

# collection = db.score
collection = db["score"]

documents = collection.find()
# print(document)
for document in documents:
    print(document)

inventory = db.inventory.find()
for item in inventory:
    print(item)