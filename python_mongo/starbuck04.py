import json
from pymongo import MongoClient
from pprint import pprint

with open("starbucks.json", "r", encoding="utf8") as file:
    json_data = file.readline()

dict_data = json.loads(json_data)
# pprint(dict_data)

geo_list = list()
for data in dict_data['list']:
    geo_dict = dict()
    geo_dict['s_name'] = data['s_name']
    geo_dict['doro_address'] = data['doro_address']

    coordinates = [float(data['lot']), float(data['lat'])]
    geo_dict['location'] = {"type": "Point", "coordinates": coordinates}

    geo_list.append(geo_dict)

# print(geo_list)

client = MongoClient("localhost", 27017)
db = client.test
starbucks = db.starbucks
res = starbucks.insert_many(geo_list)
pprint(res.inserted_ids)

all = starbucks.find()
for doc in all:
    pprint(doc)