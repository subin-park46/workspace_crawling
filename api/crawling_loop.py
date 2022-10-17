import requests
from bs4 import BeautifulSoup

url = "https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=FILE&keyword=%EA%B5%90%EC%9C%A1&detailKeyword=&publicDataPk=&recmSe=N&detailText=&relatedKeyword=&commaNotInData=&commaAndData=&commaOrData=&must_not=&tabId=&dataSetCoreTf=&coreDataNm=&sort=&relRadio=&orgFullName=&orgFilter=&org=&orgSearch=&currentPage=1&perPage=10&brm=&instt=&svcType=&kwrdArray=&extsn=&coreDataNmArray=&pblonsipScopeCode="
resp = requests.get(url)
soup = BeautifulSoup(resp.text, "html.parser")
paging = soup.find("nav", class_="pagination")

"""
nums = list()
for page in paging:
    # print(page.text)
    if page.text.isdigit():
        # print(page.text)
        nums.append(page.text)
"""
nums = list(filter(None, map(lambda x: x.text if x.text.isdigit() else None, paging)))

for i in nums:
    # f string 만들기
    sub_url = f"https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=FILE&keyword=교육&currentPage={i}"
    # sub_resp = requests.get(sub_url) 이랑
    # sub_soup = BeautifulSoup(sub_resp.text, "html.parser") 합친 것.
    sub_soup = BeautifulSoup(requests.get(sub_url).text, "html.parser")
    titles = sub_soup.select("span[class=title]")  # 한 페이지 제목 가져오기
    for title in titles:
        print(title.text.strip())