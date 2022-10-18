import requests
from xml.etree import ElementTree # xml 객체로 만들자
import re

def today():
    service_key = "wlDJ%2F9iedzCniA3yJopx238L05ZHBtuK%2BTGcIaXOLYn4aJzq48Yqih%2FoSmwykMmUZX204XOAdWd79FbkhilJWQ%3D%3D"
    url = f"http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson?ServiceKey={service_key}"
    # print(url)
    resp = requests.get(url)
    # print(resp.text)
    tree = ElementTree.fromstring(resp.text) # fromstring() : 문자열에서 Element로 XML을 직접 구문 분석하는데, 구문 분석된 트리의 루트 엘리먼트

    for items in tree[1][0]: # item의 내용을 찾음
        if items.find('gubun').text == '합계':
            incDec = items.find('incDec').text # 전일대비 증감수
            localOccCnt = items.find('localOccCnt').text # 지역발생 수
            overFlowCnt = items.find('overFlowCnt').text # 해외유입 수
            # (\D)는 숫자가 아닌 것과 매치하는 정규 표현식
            stdDay = re.sub(r'(\D)+', '', items.find('stdDay').text)[2: 8]
            # print(stdDay) # 221018
            stdDay = stdDay[:2] + "/" + stdDay[2:4] + "/" + stdDay[4:]
            print(f'[{stdDay}]\n일일합계:{incDec}\n국내발생:{localOccCnt}\n해외발생:{overFlowCnt}')


if __name__ == '__main__':
    today()