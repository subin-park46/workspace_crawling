from pymongo import MongoClient
import pprint


client = MongoClient("localhost", 27017)
db = client.test
score = db.score

cursor = score.find()
# print(cursor)

# pretty print / mongo에서는 db.score.find().pretty() 동일한 결과
for doc in cursor:
    pprint.pprint(doc)

print("=============================================")
pprint.pprint(score.find_one({"name": "이순신"}))

print(f"document의 총 갯수 : {score.count_documents({})}")
print("=============================================")
print("국어점수가 60점 이상인 학생들 출력")

kors = score.find({"kor": {"$gte": 60}})
for doc in kors:
    pprint.pprint(doc)