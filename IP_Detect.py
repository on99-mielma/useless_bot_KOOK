import aiohttp
import json
# import asyncio

async def The_ip_Detect(ip='1.1.1.1'):
    base_url = 'http://realip.cc/?ip={ip}'.format(ip=ip)
    headers ={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62'}
    async with aiohttp.ClientSession() as session:
        async with session.get(base_url,headers=headers) as response:
            print(json.loads(await response.text()))
            return json.loads(await response.text())



# loop = asyncio.get_event_loop()
# loop.run_until_complete(The_ip_Detect('asfjsdlkfjlsdfds'))