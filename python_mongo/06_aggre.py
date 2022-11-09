from pymongo import MongoClient


client = MongoClient("localhost", 27017)
db = client.test
score = db.score

# 국어점수가 50점 이상인 학생들의 국어점수 평균을 출력하자.
aggr = score.aggregate([{"$match": {"kor": {"$gte": 50}}}, {"$group": {"_id": "kor", "avg": {"$avg": "$kor"}}}])

print(aggr)
print(list(aggr))