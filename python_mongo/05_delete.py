from pymongo import MongoClient


client = MongoClient("localhost", 27017)
db = client.test
score = db.score

res01 = score.delete_one({"name": "윤하"})
print(res01.deleted_count)

# 국어점수가 100점이고, 수학점수도 100점인 학생들을 모두 삭제하자.
res02 = score.delete_many({"$and": [{"kor": 100}, {"math": 100}]})
print(res02.deleted_count)