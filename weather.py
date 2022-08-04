import aiohttp
import json
# import asyncio

with open("D:\\code\\kookbot\\kook_bot\\config\\config.json", 'r', encoding='utf-8') as f:
    config = json.load(f)

async def ohweather():
    lat1 = config['the_latitude']
    lon1 = config['the_longitude']
    headers ={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62'}
    url = f'https://api.open-meteo.com/v1/forecast?latitude={lat1}&longitude={lon1}&hourly=relativehumidity_2m,apparent_temperature'
    # now_hour = datetime.datetime.now().hour
    async with aiohttp.ClientSession() as session:
        async with session.get(url,headers=headers) as response:
            # print(json.loads(await response.text())['translation'][1:-1]," !    !!!!!")
            print("!weather debug:!   ",json.loads(await response.text()))
            return json.loads(await response.text())

# loop = asyncio.get_event_loop()
# loop.run_until_complete(ohweather())