from django.shortcuts import render
from . import starbucks02
from django.http import JsonResponse

def index(request):
    return render(request, "index.html")

def starbucks(request):
    list_all = list()  # 새로운 리스트 만들기

    sido_all = starbucks02.getSido()  # 데이터 응답 받기
    for sido in sido_all:
        if sido == '17':
            result = starbucks02.getStore(sido_cd=sido)
            print(result)
            list_all.extend(result)
        else:
            gugun_all = starbucks02.getGuGun(sido)
            for gugun in gugun_all:
                result = starbucks02.getStore(gugun_cd=gugun)
                print(result)
                list_all.extend(result)

    result_dict = dict()
    result_dict['list'] = list_all
    # result_json = json.dumps(result_dict, ensure_ascii=False)

    # JsonResponse : dictionary 객체를 받아서 json 변환
    return JsonResponse(result_dict)