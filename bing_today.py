import aiohttp
from re import search
import time


data = str(time.localtime(time.time())[:3])
base = 'https://cn.bing.com'
async def get_bing_everyday_pic():
    headers1 = {
        'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
    }
    the_url = 'https://cn.bing.com/HPImageArchive.aspx?idx=0&n=1'
    async with aiohttp.ClientSession() as session:
        async with session.get(the_url,headers=headers1) as response:
            xml = await response.text('utf-8','ignore')
            print(type(xml))
            img_url = base + search(r'<url>(.*)</url>', xml).groups()[0]
            copyright_text = search(r'<copyright>(.*)</copyright>', xml).groups()[0]
            copyright_url = base + search(r'<copyrightlink>(.*)</copyrightlink>', xml).groups()[0]
            print(img_url,copyright_text,copyright_url)
            return (img_url,copyright_text,str(copyright_url))
