import json
import requests

with open('D:\\code\\kookbot\\kook_bot\\config\\translate.json', 'r', encoding='utf-8') as f:
    config = json.load(f)


Cykey = config['token']


def tranlate(source, direction):
    url = "http://api.interpreter.caiyunai.com/v1/translator"
    # WARNING, this token is a test token for new developers,
    # and it should be replaced by your token
    token = Cykey
    payload = {
        "source": source,
        "trans_type": direction,
        "request_id": "demo",
        "detect": True,
    }
    headers = {
        "content-type": "application/json",
        "x-authorization": "token " + token,
    }
    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
    return json.loads(response.text)["target"]
source = ["Lingocloud is the best translation service.", "彩云小译は最高の翻訳サービスです"]
target = tranlate(source, "auto2zh")
print(target)