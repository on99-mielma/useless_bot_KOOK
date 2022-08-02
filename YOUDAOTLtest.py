import json
import sys
import aiohttp
import uuid
import hashlib
import time
from imp import reload

reload(sys)

with open('D:\\code\\kookbot\\kook_bot\\config\\translate.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

app_key = config['app_key']
app_sercet = config['app_sercet']
url = 'https://openapi.youdao.com/api'

def encrypt(signStr):
    hash_algorithm = hashlib.sha256()
    hash_algorithm.update(signStr.encode('utf-8'))
    return hash_algorithm.hexdigest()


def truncate(q):
    if q is None:
        return None
    size = len(q)
    return q if size <= 20 else q[0:10] + str(size) + q[size - 10:size]

async def do_request(data):
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    async with aiohttp.ClientSession() as session:
        async with session.post(url , data=data,headers=headers) as response:
            return response

def connect():
    q = "You may not control all the events that happen to you, but you can decide not to be reduced by them."

    data = {}
    data['from'] = 'en'
    data['to'] = 'zh-CHS'
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

    response = do_request(data)
    contentType = response.headers['Content-Type']
    if contentType == "audio/mp3":
        millis = int(round(time.time() * 1000))
        filePath = "合成的音频存储路径" + str(millis) + ".mp3"
        fo = open(filePath, 'wb')
        fo.write(response.content)
        fo.close()
    else:
        print(response.content)


if __name__ == '__main__':
    connect()
