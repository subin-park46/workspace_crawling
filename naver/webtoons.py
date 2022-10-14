import requests
from bs4 import BeautifulSoup
import json

url = "https://comic.naver.com/webtoon/weekdayList?week=fri"
resp = requests.get(url)
# print(resp)
# print(resp.text)

soup = BeautifulSoup(resp.text, "html.parser")
# print(soup)

# find 사용했기 때문에, img_list의 개수는 한개
img_list = soup.find("ul", {"class": "img_list"}) # ul 태그 가져오는데 class가 img_list
webtoons = img_list.select("dl") # 전부 찾는 코드

webtoon_list = list()
for webtoon in webtoons:
    title = webtoon.find("a")['title'] # a태그에서 title 속성 가져오기 / 여러 개 있어도 가장 먼저 찾아진 a 태그 먼저 가져옴.
    star = webtoon.find("strong").text # strong 태그 안의 text 즉, 평점
    #print(f"[{star}] {title}")
    tmp = dict()
    tmp['title'] = title
    tmp['star'] = star

    webtoon_list.append(tmp)

# print(webtoon_list)

res = dict()
res['webtoons'] = webtoon_list
# print(res)

res_json = json.dumps(res, ensure_ascii=False)
#print(res_json)

with open("webtoons.json", "w", encoding="utf-8") as f:
    f.write(res_json)