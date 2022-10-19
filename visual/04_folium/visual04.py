import requests
import json
import folium


def getSiDo():

    url = 'https://www.starbucks.co.kr/store/getSidoList.do'
    resp = requests.post(url)
    sido_json = resp.json()['list']
    sido_code = list(map(lambda x: x['sido_cd'], sido_json))
    sido_name = list(map(lambda x: x['sido_nm'], sido_json))
    sido_dict = dict(zip(sido_code, sido_name))

    return sido_dict


def getGuGun(sido_code):
    url = 'https://www.starbucks.co.kr/store/getGugunList.do'
    resp = requests.post(url, data={'sido_cd': sido_code})

    gugun_json = resp.json()['list']
    gugun_dict = dict(zip(list(map(lambda x: x['gugun_cd'], gugun_json)), list(map(lambda x: x['gugun_nm'], gugun_json))))

    return gugun_dict


def getStore(sido_code='', gugun_code=''):
    url = 'https://www.starbucks.co.kr/store/getStore.do'

    resp = requests.post(url, data={
        'ins_lat': "37.56682",
        'ins_lng': "126.97865",
        'p_sido_cd': sido_code,
        'p_gugun_cd': gugun_code,
        'in_biz_cd': "",
        'set_date': ""})

    store_json = resp.json()['list']

    store_list = list()
    count = 0
    for store in store_json:
        store_dict = dict()
        store_dict['s_name'] = store['s_name']
        store_dict['tel'] = store['tel']
        store_dict['doro_address'] = store['doro_address']
        store_dict['lat'] = store['lat']
        store_dict['lot'] = store['lot']
        store_list.append(store_dict)
        count += 1

    store_dict = dict()
    store_dict['store_list'] = store_list
    store_dict['count'] = count

    result = json.dumps(store_dict, ensure_ascii=False)

    make_map(store_dict)

    return result


def make_map(result):
    min_lat = min(list(map(lambda x: x['lat'], result['store_list'])))
    max_lat = max(list(map(lambda x: x['lat'], result['store_list'])))
    center_lat = float(max_lat) - (float(max_lat) - float(min_lat))/2

    min_lot = min(list(map(lambda x: x['lot'], result['store_list'])))
    max_lot = max(list(map(lambda x: x['lot'], result['store_list'])))
    center_lot = float(max_lot) - (float(max_lot) - float(min_lot))/2

    m = folium.Map(location=[center_lat, center_lot], zoom_start=14)

    for data in result['store_list']:
        popup = folium.Popup(folium.Html(data['s_name']),max_width=len(data['s_name'])*30)
        folium.Marker(
            location=[data['lat'], data['lot']],
            popup=popup,
            icon=folium.Icon(color='red')
        ).add_to(m)

    m.save('result.html')


if __name__ == '__main__':
    print(getSiDo())
    sido = input('도시 코드를 입력해 주세요')
    if sido == '17':
        print(getStore(sido_code=17, gugun_code=1701))
    else:
        print(getGuGun(sido))
        gugun = input('구군 코드를 입력해 주세요')
        print(getStore(gugun_code=gugun))