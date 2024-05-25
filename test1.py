import requests

cookies = {
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Origin': 'https://m.ctyun.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://m.ctyun.cn/wap/main/auth/login',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"'
}

params = {
    'referrer': 'wap',
    'mainVersion': '300031500',
    'comParam_curTime': '1696000893681',
    'comParam_seqCode': 'BBA6CAE50AD300B8E8532568D8A83236',
    'comParam_signature': '3e8b3f5918d79e8b8868dcc2e74a14ff',
    'isCheck': 'true',
    'locale': 'zh-cn',
}

data = {
    'userName': '7256753@qq.com',
    'password': 'ruAhtrD/xxg=',
}

response = requests.post('https://m.ctyun.cn/account/login', params=params, cookies=cookies, headers=headers, data=data)
print(response.text)
print('test')
print("bug")