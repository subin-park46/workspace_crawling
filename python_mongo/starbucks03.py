from pymongo import MongoClient
import json
from pprint import pprint


with open('starbucks.json', 'r', encoding='utf8') as file:
    starbucks = file.readline()

starbucks_dict = json.loads(starbucks)
# print(starbucks_dict)

# mongodb의 test database에 starbucks 라는 collection으로 starbucks_dict 데이터를 저장하자.
client = MongoClient("localhost", 27017)
db = client.test
# res = db.starbucks.insert_many(starbucks_dict["list"])
# print(res.inserted_ids)

for doc in db.starbucks.find():
    pprint(doc)


