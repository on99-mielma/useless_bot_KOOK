from calendar import c
from dataclasses import dataclass
from pydoc import cli
from yaml import KeyToken
import bing_today
from weather import *
import random
import re
from ast import Await
from pickle import NONE
#from asyncio import FastChildWatcher
from tkinter import RIGHT
from tokenize import Ignore
from turtle import right
from typing import Type
from unittest import async_case, result
from wsgiref import headers
from khl import *
import json
import logging
from khl.command import *
from datetime import datetime
from khl.card import *
from matplotlib import container
from sqlalchemy import true
from sympy import RR, Mod
import aiohttp
from translate import *
import hex_random_color


with open('D:\\code\\kookbot\\kook_bot\\config\\config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

master_id = config['master_id']
# init Bot
bot = Bot(token=config['token'])
Botoken = config['token']


""" # prefix 修改
bot.command.update_prefixes('-') """

#########机器人启动状态修改################
@bot.task.add_date()
async def startup_tasks():
    print('启动...')
    await bot.update_listening_music('WORKING NOW', 'on99', 'cloudmusic')

# 当前游戏状态修改
@bot.command(name='fake_start_game')
async def fsg(msg: Message):
    if msg.author_id != master_id:
        return
    games = await bot.list_game()
    the_game = str(config['diy_game_o'])
    game = next(filter(lambda g: g.name == the_game, games), None)
    if game is None:
        game = await bot.create_game(the_game)
    await bot.update_playing_game(game)

# 删除游戏状态
@bot.command(name='fake_stop_game')
async def status_delete(msg: Message, d: int):
    if msg.author_id != master_id:
        return
    url = "https://www.kookapp.cn/api/v3/game/delete-activity"
    headers = {f'Authorization': f"Bot {Botoken}"}
    params = {"data_type": d}
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=params, headers=headers) as response:
            return json.loads(await response.text())
""" async def fstopg():
    await bot.stop_playing_game() """


@bot.command(name='fake_stop_game_1')
async def fake_De(msg: Message):
    if msg.author_id != master_id:
        return
    await bot.stop_playing_game()


# 歌曲状态修改
@bot.command(name='fake_start_song')
async def fss(msg: Message):
    if msg.author_id != master_id:
        return
    await bot.update_listening_music('Now Not Home', 'on99', 'qqmusic')

# 歌曲状态停止
@bot.command(name='fake_stop_song')
async def fstopsong(msg: Message):
    if msg.author_id != master_id:
        return
    await bot.stop_listening_music()

# /hello
@bot.command(name='hello')
async def hello_reply(msg: Message):
    print(re.__file__)
    await msg.ctx.channel.send('hi! nice to see Ya!')

# hi#
@bot.command(rules=[Rule.is_bot_mentioned(bot)])
async def hi(msg: Message, mention_str: str):
    print(msg.author)
    print(msg.id)
    print(msg.channel_type)
    print(mention_str)
    await msg.reply(f'hi ! I am  {mention_str}.')
    """ await msg.reply(f'{ret['message']}') """


#########################失败#####################################################
# 敏感词机器人尝试
""" def is_not_good_language(keyword: str):
    the_language_list = ["操","肏","fuck",
                        "cunt","dumb","asshole",
                        "vagina","妈的","gofuckyourself"]
    def func(msg:Message):
        TLL_len = the_language_list.__len__
        for i in range(TLL_len):
            if(msg.content.find(the_language_list[i])!=-1):
                return True
        return False
    return func

@bot.command(rules=[is_not_good_language])
async def check(msg:Message, comment:str):
    if comment==NONE or comment=='':
        await msg.reply(f'you can input the sentences after /check like \'/check fuckyou\' please don\'t input the space in the sentences')
    else:
        await msg.reply(f'嘿！ \" {comment} \" 这句话有敏感词哦') """
################################################################


######################
# 删除消息检测 或是说撤回检测
@bot.on_event(EventTypes.DELETED_MESSAGE)
async def delete_catcher_on99(b: Bot, event: Event):
    print("detect delete!")
    wansee = event.body
    """ for key,value in wansee.items():
        print('{key1}:{value1}'.format(key1=key,value1=value)) """  # 查询用
    the_log_channel = config['the_log_channel']
    channel = await b.fetch_public_channel(the_log_channel)
    delete_at = datetime.fromtimestamp(event.body["created_at"] / 1000)
    # await b.send(channel, f'_一_条_信_息_被_删_除_ \t § 内容是:{event.body["content"]} \t § 此信息创建时间是: {delete_at} |····')
    cm = CardMessage()
    c1 = Card(Module.Header('被删除信息汇总'), color='7c00ff')
    c1.append(Module.Divider())
    c1.append(Module.Section(Element.Text(
        f'::内容::\n {event.body["content"]}', Types.Text.KMD)))
    c1.append(Module.Divider())
    c1.append(Module.Context(f'::消息原频道::\n {event.body["channel_id"]}'))
    c1.append(Module.Divider())
    c1.append(Module.Context(f'::创建时间::\n {delete_at}'))
    c1.append(Module.Divider())
    c1.append(Module.Context(f'::msg_id::\n {event.body["msg_id"]}'))
    cm.append(c1)
    await b.send(channel, cm)


###########################
@bot.command()
async def help9(msg: Message):
    cm = CardMessage()
    c1 = Card(Module.Header('简简单单菜单'), color='ff00f0')
    c1.append(Module.Context(
        '随便介绍介绍咯 \n 想看看自己的代码阅读能力而已 虽然这个东西制作起来十分的简单 但是我只是想试试而已'))
    # c1.append(Module.Divider())
    # c1.append()
    """ Element.Text('想看看自己的代码阅读能力而已 虽然这个东西制作起来十分的简单 但是我只是想试试而已') """
    """ c1.append(Module.ActionGroup(
        Element.Text('本人小破站地址捏'),
        Element.Button('点我直达','https://space.bilibili.com/13460134',Types.Click.LINK,theme=Types.Theme.INFO)
    )) """
    c1.append(Module.Divider())
    c1.append(Module.Section('本人小破站地址捏', Element.Button(
        '点我直达', 'https://space.bilibili.com/13460134', Types.Click.LINK, theme=Types.Theme.INFO), RIGHT))
    cm.append(c1)

    """ c2 = Card(Module.ActionGroup(
        Element.Button('/hello','/hello',Types.Click.RETURN_VAL,Types.Theme.INFO)
    )) """
    c2 = Card(Module.Header('详细'), color='76FF00')
    c2.append(Module.Divider())
    """ c2.append(Module.ActionGroup(
        Element.Button('/hello','/hello',Types.Click.RETURN_VAL,Types.Theme.INFO)
    )) """
    c2.append(Module.Divider())
    c2.append(Module.Context('Have a good night OvO'))
    cm.append(c2)

    c3 = Card(Module.File(Types.File.AUDIO, "http://music.163.com/song/media/outer/url?id=1824020873.mp3",
              title='Beautiful World (Da Capo Version)', cover='http://p1.music.126.net/l3G4LigZnOxFE9lB4bz_LQ==/109951165791860501.jpg?param=177y177'))
    cm.append(c3)

    await msg.reply(cm)
    # await msg.ctx.channel.send(cm)


""" {
        "type": "audio",
        "title": "?",
        "src": "https://music.163.com/#/song?id=518895995&userid=366870386",
        "cover": "https://img.kaiheila.cn/assets/2021-01/rcdqa8fAOO0hs0mc.jpg"
} """


""" @bot.command()
async def card(msg: Message):
    c = Card(Module.Header('CardMessage'), Module.Section('convenient to convey structured information'))
    cm = CardMessage(c)  # Card can not be sent directly, need to wrapped with a CardMessage
    await msg.reply(cm) """

##make some fun
@bot.command(regex='^(on99)$')
async def stuai(msg:Message, *args):
    if msg.author_id != master_id:
        return
    print(args)
    await msg.reply("我在")


# 正则测试 是否能跳过prefix  测试结果：能
@bot.command(regex='^(helpme)$')
async def help19(msg: Message, *args):
    print(*args)
    print(msg.author_id)
    cm = CardMessage()
    c1 = Card(Module.Header('简简单单菜单'), color='ff00f0')
    c1.append(Module.Context(
        '随便介绍介绍咯 \n 想看看自己的代码阅读能力而已 虽然这个东西制作起来十分的简单 但是我只是想试试而已'))
    # c1.append(Module.Divider())
    # c1.append()
    """ Element.Text('想看看自己的代码阅读能力而已 虽然这个东西制作起来十分的简单 但是我只是想试试而已') """
    """ c1.append(Module.ActionGroup(
        Element.Text('本人小破站地址捏'),
        Element.Button('点我直达','https://space.bilibili.com/13460134',Types.Click.LINK,theme=Types.Theme.INFO)
    )) """
    c1.append(Module.Divider())
    c1.append(Module.Section('本人小破站地址捏', Element.Button(
        '点我直达', 'https://space.bilibili.com/13460134', Types.Click.LINK, theme=Types.Theme.INFO), RIGHT))
    cm.append(c1)


# 22222222222222222222222222222222222222222222222222222222222222222222
    c2 = Card(Module.Header('详细'), color='76FF00')
    c2.append(Module.Divider())
    c2.append(Module.ActionGroup(
        Element.Button('/hello', '/hello',
                       Types.Click.RETURN_VAL, Types.Theme.INFO),
        Element.Button('/roll', '/roll 最小值 最大值 roll的个数(默认为1)',
                       Types.Click.RETURN_VAL, Types.Theme.SUCCESS)
    ))
    c2.append(Module.Divider())
    c2.append(Module.Context('Have a good night OvO'))
    cm.append(c2)

    c3 = Card(Module.File(Types.File.AUDIO, "http://music.163.com/song/media/outer/url?id=1824020873.mp3",
              title='Beautiful World (Da Capo Version)', cover='http://p1.music.126.net/l3G4LigZnOxFE9lB4bz_LQ==/109951165791860501.jpg?param=177y177'))
    cm.append(c3)

    await msg.reply(cm)

# ActonGroup 实验到实践
@bot.command(regex='(.|/|§){1}(choice){1}')
async def button_act(msg: Message , *args):
    if msg.author_id != master_id:
        return
    await msg.reply(
        CardMessage(
            Card(
                Module.Header('NOW IT IS A CHOICE ABOUT REALITY OR LALALAND'),
                Module.Context('Take a pill, take the choice'),
                Module.ActionGroup(
                    # RETURN_VAL type(default): send an event when clicked, see print_btn_value() defined at L58
                    Element.Button('Truth',value='red',theme=Types.Theme.DANGER,click=Types.Click.RETURN_VAL),
                    Element.Button('Wonderland',value='blue', theme=Types.Theme.INFO, click=Types.Click.RETURN_VAL)
                    # Element.Button('exp','https://www.bilibili.com',Types.Click.LINK),
                    # Element.Button('exp2','https://www.bilibili.com',theme=Types.Theme.INFO)
                    ),
                Module.Divider(),
                Module.Context(Element.Text("好好学习吧 滚去[LeetCode](https://leetcode.cn/)",type=Types.Text.KMD)),color=(await hex_random_color.get_random_hex_color()))))


from khl import api
@bot.on_event(EventTypes.MESSAGE_BTN_CLICK)
async def help_rollback_hello(b: Bot, e: Event):
    print("以下为后台打印")
    # for key, value in e.body.items():
    #     print('{key1}:{value1}'.format(key1=key, value1=value))
    print("/////")
    print(e.extra)
    the_value = str(e.extra['body']['value'])
    if the_value in ['red' , 'blue','back']:
        user_id = e.extra['body']['user_id']
        channel_id = e.extra['body']['target_id']
        msg_id = e.extra['body']['msg_id']
        the_pic = e.extra['body']['user_info']['avatar']
        await bot.client.gate.exec_req(api.Message.update(msg_id=msg_id,content=json.dumps(the_answer(the_value,the_pic))))
        return
    channel = await b.fetch_public_channel(e.body['target_id'])
    button_value_info = e.body['value']
    await b.send(channel, f'{button_value_info}', temp_target_id=e.body['user_id'])

from datetime import timedelta
def the_answer(ans:str,url:str=None) -> CardMessage:
    now_time = datetime.now()
    delta = timedelta(seconds=20)
    now_time = now_time + delta
    cm = CardMessage()
    if ans in ['red']:
        c1 = Card(Module.Header("You choose the reality"),
              Module.Divider(),
              Module.Section(Element.Text("World will be destoried in under countdown",type=Types.Text.KMD),Element.Button('Re',value='back',theme=Types.Theme.PRIMARY,click=Types.Click.RETURN_VAL),mode=Types.SectionMode.RIGHT),
              Module.Countdown(end=now_time,mode=Types.CountdownMode.SECOND),color=(hex_random_color.get_random_hex_color_no_await()))
        cm.append(c1)
        return cm
    elif ans in ['blue']:
        c1 = Card(Module.Header("You choose the lalaland"),
              Module.Divider(),
              Module.Section(Element.Text("There will be a sweet dream here for you",type=Types.Text.KMD),Element.Button('Re',value='back',theme=Types.Theme.PRIMARY,click=Types.Click.RETURN_VAL),mode=Types.SectionMode.RIGHT),color=(hex_random_color.get_random_hex_color_no_await()))
        c2 = Card(Module.ImageGroup(Element.Image(src=url,size=Types.Size.LG)),color=(hex_random_color.get_random_hex_color_no_await()))
        cm.append(c1)
        cm.append(c2)
        return cm
    elif ans in ['back']:
        cm = CardMessage(
            Card(
                Module.Header('NOW IT IS A CHOICE ABOUT REALITY OR LALALAND'),
                Module.Context('Take a pill, take the choice'),
                Module.ActionGroup(
                    # RETURN_VAL type(default): send an event when clicked, see print_btn_value() defined at L58
                    Element.Button('Truth',value='red',theme=Types.Theme.DANGER,click=Types.Click.RETURN_VAL),
                    Element.Button('Wonderland',value='blue', theme=Types.Theme.INFO, click=Types.Click.RETURN_VAL)
                    # Element.Button('exp','https://www.bilibili.com',Types.Click.LINK),
                    # Element.Button('exp2','https://www.bilibili.com',theme=Types.Theme.INFO)
                    ),
                Module.Divider(),
                Module.Context(Element.Text("好好学习吧 滚去[LeetCode](https://leetcode.cn/)",type=Types.Text.KMD)),color=(hex_random_color.get_random_hex_color_no_await())))
        return cm
    return cm
#########################################################################

###############################################################
""" @bot.command(rules=[Rule.is_mention_all])
async def yes(msg: Message, mention_str: str):
    print(mention_str)
    await msg.reply(f'为什么你要{mention_str}') """


afk_status_check = False
#正则检测 某个人被@ \(met\)#######↓这串数字是我的id也就是我上面设定的master_id########################
@bot.command(regex=f'(.*)\(met\){master_id}\(met\)(.*)')
async def checkYat9(msg: Message, *args):
    print(*args)
    if afk_status_check:
        await msg.ctx.channel.send(f'别@这人了他不在')


# 上面的开关
@bot.command(name='AFKON')
async def afk_on(msg: Message):
    if msg.author_id != master_id:
        return
    global afk_status_check
    afk_status_check = True


@bot.command(name='AFKOFF')
async def afk_on(msg: Message):
    if msg.author_id != master_id:
        return
    global afk_status_check
    afk_status_check = False
#######################################


####################翻译#####################
async def translate(msg: Message, *args):
    print("arg: ", args)
    word = " ".join(args)
    print("word: ", word)
    cm = CardMessage()
    if is_CN(word):
        c1 = Card(Module.Section(Element.Text(f"**翻译结果:** {await caiyunTL(word,'auto2en')}", Types.Text.KMD)), Module.Context('来自：彩云小译，翻译成英文'))
    else:
        c1 = Card(Module.Section(Element.Text(f"**翻译结果:** {await caiyunTL(word,'auto2zh')}", Types.Text.KMD)), Module.Context('来自：彩云小译，翻译成中文'))

    cm.append(c1)
    await msg.reply(cm)


@bot.command(name='TL', aliases=['tl', 'translate', '翻译'])  # aliases是别名的意思
async def translate1(msg: Message, *args):
    await translate(msg, ' '.join(args))


########################有道##########################
async def translate_youdao(msg: Message, *args):
    print("arg: ", args)
    word = " ".join(args)
    print("word: ", word)
    cm = CardMessage()
    c1 = Card(Module.Section(Element.Text(f"**翻译结果:** {await youdaoTL(word,'zh-CHS')}", Types.Text.KMD)), Module.Context('来自：有道翻译自动检测 中文和英文以外的不确定'))

    cm.append(c1)
    await msg.reply(cm)


@bot.command(name='youdao')
async def translate_2(msg: Message, *args):
    await translate_youdao(msg, ' '.join(args))


""" #实时翻译栏位
ListTL = ['0','0','0']

#查看目前占用的翻译容量
def checkTL():
    sum = 0
    for i in ListTL:
        if i!='0':
            sum+=1
    return sum

@bot.command()
async def CheckTL(msg:Message):
    global ListTL
    await msg.reply(f"目前已使用栏位:{checkTL()}/{len(ListTL)}")

# 关闭所有栏位的实时翻译（避免有些人用完不关）
@bot.command()
async def ShutdownTL(msg:Message):
    if msg.author.id != master_id:
        return#这条命令只有bot的作者可以调用 
    global ListTL
    if checkTL()==0:
        await msg.reply(f"实时翻译栏位为空: {checkTL()}/{len(ListTL)}")
        return
    i=0
    while i< len(ListTL):
        if(ListTL[i])!='0': #不能对0的频道进行操作
            channel = await bot.fetch_public_channel(ListTL[i]) 
            await bot.send(channel,"不好意思，已经清空了实时翻译的栏位！")
            ListTL[i] = '0'
        i+=1
    await msg.reply(f"实时翻译栏位已清空！目前为: {checkTL()}/{len(ListTL)}")

# 开启实时翻译功能
@bot.command(name='TLON',aliases=['tlon'])
async def TLON(msg: Message):
    #print(msg.ctx.channel.id)
    global ListTL
    if checkTL() == len(ListTL):
        await msg.reply(f"目前栏位: {checkTL()}/{len(ListTL)}，已满！")
        return
    #发现bug，同一个频道可以开启两次实时翻译，需要加一个判断
    if msg.ctx.channel.id in ListTL:
         await msg.reply(f"本频道已经开启了实时翻译功能，请勿重复操作!")
         return
    i=0
    while i< len(ListTL):
        if ListTL[i] == '0':
            ListTL[i] = msg.ctx.channel.id
            break
        i+=1
    ret = checkTL()
    await msg.reply(f"Real-Time Translation ON\n现在会实时翻译本频道的对话啦！\n目前栏位: {ret}/{len(ListTL)}，使用`/TLOFF`可关闭实时翻译")

# 关闭实时翻译功能
@bot.command(name='TLOFF',aliases=['tloff'])
async def TLOFF(msg: Message):
    global ListTL
    i=0
    while i< len(ListTL):
        if ListTL[i] == msg.ctx.channel.id:
            ListTL[i] = '0'
            await msg.reply(f"Real-Time Translation OFF！目前栏位: {checkTL()}/{len(ListTL)}")
            return
        i+=1
    await msg.reply(f"本频道并没有开启实时翻译功能！目前栏位: {checkTL()}/{len(ListTL)}")
 """

##########################################
@bot.command(name='ser_get_all_info')
async def SGAI(msg: Message):
    if msg.author_id != master_id:
        return
    url = "https://www.kookapp.cn/api/v3/guild/user-list"
    headers = {f'Authorization': f"Bot {Botoken}"}
    the_guild_id = config['the_guild_id']
    params = {"guild_id": the_guild_id}
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, headers=headers) as response:
            sgai_res = await response.text()
            print(type(sgai_res))
            info_to_json = json.loads(sgai_res)
            print(type(info_to_json))
            get_a_id = info_to_json['data']['items']
            for u in get_a_id:
                print(u)
            return get_a_id


async def SGAI2(msg: Message):
    if msg.author_id != master_id:
        return
    url = "https://www.kookapp.cn/api/v3/guild/user-list"
    headers = {f'Authorization': f"Bot {Botoken}"}
    the_guild_id = config['the_guild_id']
    params = {"guild_id": the_guild_id}
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, headers=headers) as response:
            sgai_res = await response.text()
            # print(type(sgai_res))
            info_to_json = json.loads(sgai_res)
            # print(type(info_to_json))
            get_a_id = info_to_json['data']['items']
            """ for u in get_a_id:
                print(u) """
            return get_a_id

import re
@bot.command(name='get')
async def gettttter(msg: Message, men_str: str):
    if msg.author_id != master_id:
        return
    id_dict = await SGAI2(msg)
    stwqtr = men_str
    result = re.match('\(met\)(\d+?)\(met\)', stwqtr)
    # print(result)
    # print(result.group(1))
    if result is None:
        await msg.reply('未检测到@行为')
        return
    finallllll_result = result.group(1)
    for u in id_dict:
        if u['id'] == finallllll_result:
            glo_u = u
            break
    cm = CardMessage()
    c1 = Card(Module.Header('LIST'), color=(await hex_random_color.get_random_hex_color()))
    c1.append(Module.Divider())
    str_id = "(spl){}(spl)".format(str(glo_u['id']))
    role_all_ids_1 = 0
    for role_all_id in glo_u['roles']:
        role_all_ids_1 |= role_all_id
    role_f_all_ids = bin(role_all_ids_1)[2:]
    color_tmp_id = hex(glo_u['color'])[2:]
    color_id1 = color_tmp_id.zfill(6)
    joined_at = glo_u['joined_at']
    active_time = glo_u['active_time']
    when_join = datetime.fromtimestamp(int(joined_at) / 1000)
    last_active_1 = datetime.fromtimestamp(int(active_time) / 1000)
    c1.append(Module.Section(Element.Text(
        f"🆔::\t{str_id}\nUsername::\t{glo_u['username']}\nNickname::\t{glo_u['nickname']}\nSuffix::\t{glo_u['identify_num']}\nAuthority::\t{role_f_all_ids}\nRole Color::\t{color_id1}\nLast active::\t{last_active_1}\nWhen joined::\t{when_join}", Types.Text.KMD)))
    cm.append(c1)
    online_pd_true = '🟢'
    online_pd_false = '🔴'
    bot_pd_true = '🤖'
    bot_pd_false = '😀'
    c2 = Card(Module.Header('Status'), color=(await hex_random_color.get_random_hex_color()))
    c2.append(Module.Divider())
    c2.append(Module.Section(Element.Text(
        f"Online status ==> {online_pd_true if glo_u['online'] else online_pd_false}\nKind ==> {bot_pd_true if glo_u['bot'] else bot_pd_false}\nMobile_verified ==> {online_pd_true if glo_u['mobile_verified'] else online_pd_false}\nIs_master ==> {online_pd_true if glo_u['is_master'] else online_pd_false}", Types.Text.KMD)))
    cm.append(c2)
    c3 = Card(Module.Header('Other Messages'), color=(await hex_random_color.get_random_hex_color()))
    banner_pd = False
    # if len(glo_u['avatar']) > 0:
    #     c3.append(Module.Context('Avatar\t'))
    #     c3.append(Module.Divider())
    #     c3.append(Module.ImageGroup(Element.Image(src=glo_u['avatar'],size='mg')))
    #     c3.append(Module.Divider())
    if len(glo_u['banner']) > 0:
        # c3.append(Module.Context('Banner\t'))
        # c3.append(Module.Divider())
        # c3.append(Module.ImageGroup(Element.Image(src=glo_u['banner'],size='lg')))
        banner_pd = True
        # c3.append(Module.Divider())
    if banner_pd:
        c3.append(Module.ImageGroup(Element.Image(src=glo_u['banner'], size=Types.Size.LG), Element.Image(
            src=glo_u['avatar'], size=Types.Size.SM)))
    else:
        c3.append(Module.ImageGroup(Element.Image(
            src=glo_u['avatar'], size=Types.Size.SM)))
    c3.append(Module.Divider())
    c3.append(Module.Context('banner and avatar'))
    cm.append(c3)
    await msg.reply(cm)


# 开黑啦的时间串的转换
@bot.command(name='timeTL')
async def timeTL(msg: Message, comment: str):
    if msg.author_id != master_id:
        return
    data = comment
    result = re.match('^\d{1,}$', data)
    if result is None:
        return
    the_ans = datetime.fromtimestamp(int(data) / 1000)
    cm = CardMessage()
    c1 = Card(Module.Context(f'结果：  {the_ans}'), color='62FF00')
    cm.append(c1)
    await msg.reply(cm)

# roll点模块
@bot.command()
async def roll(msg: Message, t_min: int, t_max: int, n: int = 1):
    result = [random.randint(t_min, t_max) for i in range(n)]
    await msg.reply(f'Result :  {result}')


# 爬虫 chrome 用的headers
# import time
@bot.command(name='on99_home_weather')
async def ohweather_in(msg: Message):
    if msg.author_id != master_id:
        return
    # headers ={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62'}
    # url = 'https://api.open-meteo.com/v1/forecast?latitude=22.4938&longitude=113.4320&hourly=temperature_2m,relativehumidity_2m,apparent_temperature'
    now_hour = datetime.now().hour
    weather_result_json = await ohweather()
    cm = CardMessage()
    c1 = Card(Module.Section(Element.Text(f"**温度:** {weather_result_json['hourly']['apparent_temperature'][now_hour%24]}", Types.Text.KMD)),
              Module.Divider(),
              Module.Section(Element.Text(
                  f"**湿度:** {weather_result_json['hourly']['relativehumidity_2m'][now_hour%24]}", Types.Text.KMD)),
              Module.Context('爬自国外网站，不准也正常'))

    cm.append(c1)
    await msg.reply(cm)


@bot.command()
async def cat(msg: Message, chang: int, kuang: int):
    url = 'https://placekitten.com/{chang}/{kuang}'.format(
        chang=chang, kuang=kuang)
    cm = CardMessage()
    c1 = Card(Module.ImageGroup(Element.Image(src=url)))
    cm.append(c1)
    await msg.reply(cm)

# url_random ='https://picsum.photos/400/400?random=1'


@bot.command()
async def random_pic(msg: Message, chang: int, kuang: int, random_index: int = 2):
    url = 'https://picsum.photos/{chang}/{kuang}?random={random_index}'.format(
        chang=chang, kuang=kuang, random_index=random_index)
    cm = CardMessage()
    c1 = Card(Module.ImageGroup(Element.Image(src=url)))
    cm.append(c1)
    await msg.reply(cm)
################################################
# https://img.kookapp.cn/assets/2022-07/dyThqVClf21hc0u0.jpg
# D:\\DownLoad\\KoalaSleeping_ZH-CN8369657308_1920x1080.jpg
""" @bot.command(name = 'func_tip_1')
async def ft_1():
    channel_url = await bot.create_asset('D:\\DownLoad\\KoalaSleeping_ZH-CN8369657308_1920x1080.jpg')
    channel = await bot.fetch_public_channel('****************')
    # channel = bot.fetch_public_channel()
    await channel.send(channel_url,type=MessageTypes.IMG) """

###########每日新闻############

import re
@bot.command(name='today_news')
async def tn1(msg: Message):
    url = "https://www.163.com/dy/media/T1603594732083.html"
    headers1 = {
        'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
    }
    cm = CardMessage()
    c1 = Card(Module.Header('每日新闻'), color='f34543')
    cm.append(c1)
    c2 = Card(color='f2fa56')
    c3 = Card(Module.Context('消息来源：网易号资讯 内容作者:365资讯简报'), color='fe65a2')
    # c1.append(Module.Divider())
    # rsq = requests.get(url,headers=headers)
    # # print(rsq)
    # hot = rsq.content.decode('utf-8')
    # # print(hot)
    # today_url = re.findall('https://www.163.com/dy/article/.*\.html', hot)[0]
    # rsq = requests.get(today_url, headers=headers)
    # hot = rsq.content.decode('utf-8')
    # # print(hot)
    # news_list = re.findall('(?<=知晓天下事！<br/>).*(?=<br/></p><p class="f_center">)', hot)[0].split('<br/>')
    # msg = '\n'.join(news_list)
    # 上面这段注释源码来自与52pojie网

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers1) as response:
            hot = await response.text('utf-8', 'ignore')
            # print(hot)
            # print("?#$%^#$%$#%$#%#$%$#%")
            today_url = re.findall(
                'https://www.163.com/dy/article/.*\.html', hot)[0]
            # print(today_url)
            # print("?#$%^#$%$#%$#%#$%$#%")
            async with session.get(today_url, headers=headers1) as response:
                hot = await response.text('utf-8', 'ignore')
                # with open('D:\\code\\kookbot\\kook_bot\\config\\debug.txt','w',encoding='utf-8') as f:
                #     f.write(hot)
                #     f.close()
                # print(hot)
                news_list = re.findall('(?<=知晓天下事！<br/>).*(?=</p><p class="f_center">)', hot)[0].split('<br/>')
                msg1 = '\n'.join(news_list)
                n_size = len(news_list)
                # c2.append(Module.Section(Element.Text(f"{msg1}")))
                # c2.append(Module.Section(f"{msg1}"))
                c2.append(Module.Section(
                    Element.Text(f"{msg1}", Types.Text.KMD)))
                cm.append(c2)
                cm.append(c3)
                await msg.ctx.channel.send(cm)
                # await msg.reply(cm)
                # msg1 = '\n'.join(news_list)
                # print(type(msg1))
                # await msg.ctx.channel.send(f'{msg1}')
                # await msg.reply(f'{msg}')


####################bing每日壁纸#####################
@bot.command(name='today_bing')
async def tb1(msg: Message):
    img_url, copyright_text, copyright_url = await bing_today.get_bing_everyday_pic()
    cm = CardMessage()
    c1 = Card(Module.Header('必应每日壁纸'), color='1fff7e')
    # c1.append(Module.Divider)
    """ c1.append(Module.Section(f'必应今日壁纸:{copyright_text}', Element.Button(
        'This way', f'{img_url}', Types.Click.LINK, theme=Types.Theme.INFO), RIGHT)) """
    # c3 = Card(Module.Context(f'{copyright_url}'),color='e87d3a')
    c2 = Card(Module.Section(f'必应今日壁纸:\n {copyright_text}', Element.Button(
        'This way', img_url, Types.Click.LINK, theme=Types.Theme.INFO), RIGHT), color='e87d3a')
    c3 = Card(Module.Context(
        f'copyright_url: \n {copyright_url}'), color='ba9af0')
    c4 = Card(Module.File(Types.File.AUDIO, "http://music.163.com/song/media/outer/url?id=454231783.mp3",
              title='Beneath the Mask -rain-', cover='http://p2.music.126.net/FmuZirfGmg9FbMy3hkEqAA==/109951165567176149.jpg?param=130y130'), color='ed173e')
    cm.append(c1)
    cm.append(c2)
    cm.append(c3)
    cm.append(c4)
    await msg.ctx.channel.send(cm)

#################DNS DETECT#############################
import re
import Domain_Name_System_Detect
@bot.command(name='DNS',aliases=['dns'])
async def DNS_detect_bot(msg:Message,the_url:str):
    url = the_url
    print(url)
    if url.startswith('['):
        what_result = re.split("[\[\]\(\)]", str(url))
        if what_result is not None:
            url = what_result[1]
    cm = CardMessage()
    result = await Domain_Name_System_Detect.DNS_Detect(url)
    if result['code'] == 1:
        the_msg = result['msg']
        c1 = Card(Module.Header(f'Result:{the_msg}'),color=(await hex_random_color.get_random_hex_color()))
        c1.append(Module.Divider())
        c1.append(Module.Section(Element.Text(
        f'URL::\n{result["url"]}', Types.Text.KMD)))
        c1.append(Module.Divider())
        c1.append(Module.Section(Element.Text(
        f'Status\t==>\t {result["type"]}', Types.Text.KMD)))
        cm.append(c1)
    else:
        c2 = Card(Module.Header(f'Result:{result["msg"]}'),color=(await hex_random_color.get_random_hex_color()))
        cm.append(c2)
    await msg.ctx.channel.send(cm)

#####################ip########################
import re
import IP_Detect
@bot.command(name='ip',aliases=['IP','Ip','iP'])
async def ip_detecttt(msg:Message,ip_url:str):
    print(ip_url)
    result = await IP_Detect.The_ip_Detect(ip_url)
    cm = CardMessage()
    keyword1 = result['notice']
    the_re_result = re.search('(is\snot\sin\sthe\sdatabase)|(not\sappear\sto)',keyword1)
    if the_re_result is not None:
        c1 = Card(Module.Header(f'{keyword1}'),color=(await hex_random_color.get_random_hex_color()))
        c1.append(Module.Divider())
        c1.append(Module.Context(f'{result["provider"]}'))
        cm.append(c1)
        await msg.ctx.channel.send(cm)
        return
    
    c1 = Card(Module.Header('>>Result<<'),color=(await hex_random_color.get_random_hex_color()))
    the_xia = '⬇'
    c2 = Card(Module.Section(Element.Text(f'IP ⬇⬇⬇⬇⬇\n**{result["ip"]}**\n\nCONTINENT ⬇⬇⬇⬇⬇\n**{result["continent"]}**\n\nPROVINCE ⬇⬇⬇⬇⬇\n**{result["province"]}**\n\nCITY ⬇⬇⬇⬇⬇\n**{result["city"]}**\n\nISP ⬇⬇⬇⬇⬇\n**{result["isp"]}**\n\nTIME ZONE ⬇⬇⬇⬇⬇\n**{result["time_zone"]}**\n\nLATITUDE AND LONGITUDE ⬇⬇⬇⬇⬇\n**{result["latitude"]}**\t**{result["longitude"]}**\n\n(spl)^^(spl)',Types.Text.KMD)),color=(await hex_random_color.get_random_hex_color()))
    c2.append(Module.Divider())
    c2.append(Module.Context(f'{result["provider"]}'))
    cm.append(c1)
    cm.append(c2)
    await msg.ctx.channel.send(cm)

########test update cardmessage######


logging.basicConfig(level='INFO')
bot.run()
