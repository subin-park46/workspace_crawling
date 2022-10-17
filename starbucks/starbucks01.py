import requests

def getSido():
    url = "https://www.starbucks.co.kr/store/getSidoList.do"
    resp = requests.post(url) # post 방식으로 url 요청
    # print(resp.text)
    # print(resp.json()) # json 형태의 문자열을 json 객체로 바꿔서 파이썬에서 사용할 수 있게 dict로 바꿔서 제공
    sido_json = resp.json()['list']
    # print(sido_json[0])
    sido_cd = list(map(lambda x: x['sido_cd'], sido_json))
    sido_name = list(map(lambda x: x['sido_nm'], sido_json))
    sido_dict = dict(zip(sido_cd, sido_name))
    return sido_dict

def getGuGun(sido_cd):
    url = "https://www.starbucks.co.kr/store/getGugunList.do"
    resp = requests.post(url, data={"sido_cd": sido_cd})
    # print(getGuGun(resp.text)) -> list 형태로 정보가 많이 들어있음.
    gugun_json = resp.json()['list'] # dict 형이기 때문에 list해서 값을 받음
    # print(gugun_json[0])
    gugun_cd = list(map(lambda x: x['gugun_cd'], gugun_json))
    gugun_name = list(map(lambda x: x['gugun_nm'], gugun_json))
    gugun_dict = dict(zip(gugun_cd, gugun_name))
    #gugun_dict = dict(zip(list(map(lambda x: x['gugun_cd'], gugun_json)), list(map(lambda x: x['gugun_nm'], gugun_json))))
    return gugun_dict

def getStore(sido_cd = "", gugun_cd = ""):
    url ="https://www.starbucks.co.kr/store/getStore.do"
    resp = requests.post(url, data={"ins_lat": "35.8563312",
                                    "ins_lng": "128.4909363",
                                    "p_sido_cd": sido_cd,
                                    "p_gugun_cd": gugun_cd,
                                    "in_biz_cd": "",
                                    "set_date": ""})

    store_json = resp.json()['list']

    store_list = list() # 데이터 저장
    for store in store_json:
        store_dict = dict()
        store_dict['s_name'] = store['s_name']
        store_dict['doro_address'] = store['doro_address']
        store_dict['lat'] = store['lat']
        store_dict['lot'] = store['lot']

        store_list.append(store_dict)

    result = dict()
    result['store_list'] = store_list
    return result


if __name__ == '__main__':
    print(getSido())
    sido = input("도시 코드를 입력해 주세요. : ")
    # print(getGuGun(sido))

    if sido == "17":
        print(getStore(sido_cd=sido))
    else:
        print(getGuGun(sido))
        gugun = input("구군 코드를 입력해 주세요 : ")
        print(getStore(sido_cd=sido, gugun_cd=gugun))