from pymongo import MongoClient


client = MongoClient("localhost", 27017)
db = client.test
score = db.score

# res01 = score.insert_one({"name": "아이유", "kor": 100, "eng": 100, "math": 100})
# print(res01.inserted_id)

yoon = {"name": "윤하", "kor": 100, "eng": 100, "math": 100}

res02 = score.insert_many([
    yoon,
    {"name": "뷔", "kor": 100, "eng": 100, "math": 100}
])
print(res02.inserted_ids)
