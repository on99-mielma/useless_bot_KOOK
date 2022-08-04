import json
import aiohttp
import urllib.request
import urllib.parse
import uuid
import hashlib
import time

with open('D:\\code\\kookbot\\kook_bot\\config\\translate.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

Cykey = config['token']
app_key = config['app_key']
app_sercet = config['app_sercet']

async def caiyunTL(source,direction):
    url = "http://api.interpreter.caiyunai.com/v1/translator"
    token = Cykey
    payload = {
        "source": source,
        "trans_type" : direction,
        "request_id": "demo",
        "detect" : True,
    }
    headers = {
        'content-type': "application/json",
        'x-authorization': "token " + token,
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(url,data=json.dumps(payload),headers=headers) as response:
            return json.loads(await response.text())["target"]

def is_CN(word):
    for ch in word:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False

async def youdaoTL(source,towhat):
    q = source
    url = 'https://openapi.youdao.com/api'
    data = {}
    data['from'] = 'EN'
    data['to'] = towhat
    data['signType'] = 'v3'
    curtime = str(int(time.time()))
    data['curtime'] = curtime
    salt = str(uuid.uuid1())
    signStr = app_key + truncate(q) + salt + curtime + app_sercet
    sign = encrypt(signStr)
    data['appKey'] = app_key
    data['q'] = q
    data['salt'] = salt
    data['sign'] = sign
    data['vocabId'] = ""

    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    async with aiohttp.ClientSession() as session:
        async with session.post(url,data=data,headers=headers) as response:
            # print(json.loads(await response.text())['translation'][1:-1]," !    !!!!!")
            print(json.loads(await response.text()))
            return json.loads(await response.text())['translation'][0]

def encrypt(signStr):
    hash_algorithm = hashlib.sha256()
    hash_algorithm.update(signStr.encode('utf-8'))
    return hash_algorithm.hexdigest()


def truncate(q):
    if q is None:
        return None
    size = len(q)
    return q if size <= 20 else q[0:10] + str(size) + q[size - 10:size]