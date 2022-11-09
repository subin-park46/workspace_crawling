from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017")
db = client["test"]
score = db["score"]

# 유재석의 국어점수를 100점으로 수정하자.
res01 = score.update_one({"name": "유재석"}, {"$set": {"kor": "100"}})

print(res01.matched_count)
print(res01.modified_count)

res02 = score.update_many(
    {"eng": {"$lt": 80}},
    {"$set": {"eng": 100}}
)
print(res02.matched_count) # 찾은 도큐먼트 수
print(res02.modified_count) # 변경된 도큐먼트 수