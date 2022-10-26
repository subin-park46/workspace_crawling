from django.shortcuts import render
from django.http import JsonResponse
import requests

def index(request):
    return render(request, "index.html")

def getSiDo(request):
    url = "https://www.starbucks.co.kr/store/getSidoList.do"
    resp = requests.post(url)
    sido_json = resp.json()['list']
    sido_cd = list(map(lambda x: x['sido_cd'], sido_json))
    sido_name = list(map(lambda x: x['sido_nm'], sido_json))
    sido_dict = dict(zip(sido_cd, sido_name))

    return JsonResponse(sido_dict)

def getGuGun(request):
    url = "https://www.starbucks.co.kr/store/getGugunList.do"
    resp = requests.post(url, data={"sido_cd": request.GET["sido_code"]})
    gugun_json = resp.json()['list']
    #gugun_cd = list(map(lambda x: x['gugun_cd'], gugun_json))
    #gugun_name = list(map(lambda x: x['gugun_nm'], gugun_json))
    gugun_dict = dict(zip(list(map(lambda x: x['gugun_cd'], gugun_json)), list(map(lambda x: x['gugun_nm'], gugun_json))))

    return JsonResponse(gugun_dict)

def getStore(request):
    url ="https://www.starbucks.co.kr/store/getStore.do"

    code = request.GET["code"]
    sido_cd = code if code == '17' else ''
    gugun_cd = '' if code == '17' else code

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

    result = dict()
    result['list'] = store_list

    return JsonResponse(result)