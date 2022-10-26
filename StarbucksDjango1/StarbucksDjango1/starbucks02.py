import requests
import json

def getSido():
    url = "https://www.starbucks.co.kr/store/getSidoList.do"
    resp = requests.post(url)
    sido_json = resp.json()['list']
    sido_cd = list(map(lambda x: x['sido_cd'], sido_json))
    sido_name = list(map(lambda x: x['sido_nm'], sido_json))
    sido_dict = dict(zip(sido_cd, sido_name))
    return sido_dict

def getGuGun(sido_cd):
    url = "https://www.starbucks.co.kr/store/getGugunList.do"
    resp = requests.post(url, data={"sido_cd": sido_cd})
    gugun_json = resp.json()['list']
    gugun_cd = list(map(lambda x: x['gugun_cd'], gugun_json))
    gugun_name = list(map(lambda x: x['gugun_nm'], gugun_json))
    gugun_dict = dict(zip(gugun_cd, gugun_name))
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

    store_list = list()
    for store in store_json:
        store_dict = dict()
        store_dict['s_name'] = store['s_name']
        store_dict['doro_address'] = store['doro_address']
        store_dict['lat'] = store['lat']
        store_dict['lot'] = store['lot']

        store_list.append(store_dict)

    return store_list

if __name__ == '__main__':
    '''
    print(getSido())
    sido = input("도시 코드를 입력해 주세요. : ")
    # print(getGuGun(sido))

    if sido == "17":
        print(getStore(sido_cd=sido))
    else:
        print(getGuGun(sido))
        gugun = input("구군 코드를 입력해 주세요 : ")
        print(getStore(sido_cd=sido, gugun_cd=gugun))
    '''

    list_all = list() # 새로운 리스트 만들기

    sido_all = getSido() # 데이터 응답 받기
    for sido in sido_all:
        if sido == '17':
            result = getStore(sido_cd=sido)
            print(result)
            list_all.extend(result)
        else:
            gugun_all = getGuGun(sido)
            for gugun in gugun_all:
                result = getStore(gugun_cd=gugun)
                print(result)
                list_all.extend(result)

    # print(len(list_all))
    result_dict = dict()
    result_dict['list'] = list_all

    result_json = json.dumps(result_dict, ensure_ascii=False)

    with open('starbucks.json', 'w', encoding='utf-8') as file:
        file.write(result_json)
