import time
from pprint import pprint

import requests


# 查老板
def cat_boss():
    url = 'https://api9.tianyancha.com/services/v3/search/homePageHotWord'

    headers = {
        'referer': 'https://servicewechat.com/wx9f2867fc22873452/31/page-frame.html',
        'content-type':'application/json',
        'version': 'TYC-XCX-WX',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Mi Note 2 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 XWEB/1162 MMWEBSDK/21 Mobile Safari/537.36 MicroMessenger/6.7.1321(0x26070010) NetType/WIFI Language/zh_CN MicroMessenger/6.7.1321(0x26070010) NetType/WIFI Language/zh_CN',
        'Host': 'api9.tianyancha.com',
    }

    rr = requests.get(url=url, headers=headers,)

    print(rr.text)



# 查公司
def cat_company():
    url = 'https://api9.tianyancha.com/services/v3/hotSearch/wxHotWord'
    headers = {
        "referer": 'https://servicewechat.com/wx9f2867fc22873452/31/page-frame.html',
        'content-type': 'application/json',
        'version': 'TYC-XCX-WX',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Mi Note 2 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 XWEB/1162 MMWEBSDK/21 Mobile Safari/537.36 MicroMessenger/6.7.1321(0x26070010) NetType/WIFI Language/zh_CN MicroMessenger/6.7.1321(0x26070010) NetType/WIFI Language/zh_CN',
        'Host': "api9.tianyancha.com",
    }
    r = requests.get(url=url, headers=headers)
    print(r.text)


# 获得Authorization，用于url拼接
def get_authorization():
    url = 'https://api9.tianyancha.com/services/v3/thirdParty/wx/getToken'
    headers = {
        'referer': 'https://servicewechat.com/wx9f2867fc22873452/31/page-frame.html',
        'content-type': 'application/json',
        'version': 'TYC-XCX-WX',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Mi Note 2 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 XWEB/1162 MMWEBSDK/21 Mobile Safari/537.36 MicroMessenger/6.7.1321(0x26070010) NetType/WIFI Language/zh_CN MicroMessenger/6.7.1321(0x26070010) NetType/WIFI Language/zh_CN',
        'Host': 'api9.tianyancha.com',
        'Connection': 'Keep-Alive',
    }
    # 目前还不知道去哪里拿的,应该是有时限的，？？？
    data = {"code": "091iAR3y1p5n4c0m9v2y1mfV3y1iAR3A"}
    r = requests.post(url=url, headers=headers, data=data)
    print(r.text)


# 搜索人名，与公司, authorization没有失效
def search_url():
    # https://api9.tianyancha.com/services/v3/search/sNorV4/360?sortType=0&pageSize=10&pageNum=1
    url = 'https://api9.tianyancha.com/services/v3/search/sNorV4/360?sortType=0&pageSize=10&pageNum=1'
    # 1580897487849
    date = int(time.time()*1000)
    # print(date)
    headers = {
        'referer': 'https://servicewechat.com/wx9f2867fc22873452/31/page-frame.html',
        # authorization: 0###oo34J0Tc5MAMQYthfaz3VqUiduBk###1580903721060###a06de22f220c3eecf709d5c810751585
        'authorization': '0###oo34J0Tc5MAMQYthfaz3VqUiduBk###1580897487849###a06de22f220c3eecf709d5c810751585',
        'content-type': 'application/json',
        'version': 'TYC-XCX-WX',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Mi Note 2 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 XWEB/1162 MMWEBSDK/21 Mobile Safari/537.36 MicroMessenger/6.7.1321(0x26070010) NetType/WIFI Language/zh_CN MicroMessenger/6.7.1321(0x26070010) NetType/WIFI Language/zh_CN',
        'Host': 'api9.tianyancha.com',
        'Connection': 'Keep-Alive',
    }
    r = requests.get(url=url, headers=headers)
    print(r.text)


def get_company(company):
    url = 'https://api9.tianyancha.com/services/v3/search/sNorV4/{}?sortType=0&pageSize=10&pageNum=1'.format(company)
    # 1580897487849 时间戳
    date = round(time.time()*1000,)
    print(date)
    headers = {
        'referer': 'https://servicewechat.com/wx9f2867fc22873452/31/page-frame.html',
        'authorization': '0###oo34J0Tc5MAMQYthfaz3VqUiduBk###{}###a06de22f220c3eecf709d5c810751585'.format(date),
        'content-type': 'application/json',
        'version': 'TYC-XCX-WX',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Mi Note 2 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 XWEB/1162 MMWEBSDK/21 Mobile Safari/537.36 MicroMessenger/6.7.1321(0x26070010) NetType/WIFI Language/zh_CN MicroMessenger/6.7.1321(0x26070010) NetType/WIFI Language/zh_CN',
        'Host': 'api9.tianyancha.com',
        'Connection': 'Keep-Alive',
    }
    r = requests.get(url=url, headers=headers)
    pprint(r.text)

get_company('腾讯')