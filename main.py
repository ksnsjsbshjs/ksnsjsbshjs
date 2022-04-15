from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pytz import timezone
from random import choice
from datetime import datetime
from re import match
from pyrogram.raw.functions.account import UpdateProfile
from pyrogram import Client, idle
from pyrogram.types import Message
from pyrogram.filters import command, edited
timeN, timeB = False, False
main = '9876543210'
dots = ['•',
       '⁃', 
       '⦾',
       '⁍',
       '‣',
       '¤'
]
fonts = [
    '❾➇➆➅➄➃➂❷❶⓪',
    '➒➑➐➏➎➍➌➋➊⓿',
    '𝟫𝟪𝟩𝟨𝟧𝟦𝟥𝟤𝟣𝟢',
    '𝟿𝟾𝟽𝟼𝟻𝟺𝟹𝟸𝟷𝟶',
    '𝟡𝟠𝟟𝟞𝟝𝟜𝟛𝟚𝟙𝟘',
    '𝟵𝟴𝟳𝟲𝟱𝟰𝟯𝟮𝟭𝟬',
    '𝟗𝟖𝟕𝟔𝟓𝟒𝟑𝟐𝟏𝟎',
    '９８７６５４３２１０',
    'ၦᲖᒣᦆƼᔰᗱᒿ᧒ᦲ',
    '68ㄥގ9ㄣƐᄅ⇂0',
    '₉₈₇₆₅₄₃₂₁₀',
    '⁹⁸⁷⁶⁵⁴³²¹⁰',
    '⑨⑧⑦⑥⑤④③②①⓪',
    '९𝟠7ϬƼ५Ӡϩ𝟙⊘'
]
def creatTime():
    time = datetime.now(timezone('Asia/Tehran')).strftime(f'%H{choice(dots)}%M')
    time = time.translate(time.maketrans(main, choice(fonts)))
    return time
app = Client('myAcc', 14027438, '9c9527c9c3e59853818ba0b0e2486737', phone_number='989303689793') #PhoneNumber
time = int()
def changeTime():
    global time
    minute = datetime.now().minute
    if time != minute:
        timeFont = creatTime() 
        try:
            app.send(UpdateProfile(last_name=timeFont if timeN else None, about=timeFont if timeB else None))
        except ConnectionError:
            pass
    time = minute
with app:
    mention = app.get_me().mention
help = f"""**Hi {mention} 🖐🏻
  • TimeName: [./]timename <on|off>
  • TimeBio: [./]timebio <on|off>**"""
isOn = '• {} is {}'
@app.on_message(edited)
def editedMessage(_, m: Message):
    pass
@app.on_message(command(['help'], prefixes=['.', '/']))
def helpMenu(_, m: Message):
    m.edit(help)
@app.on_message(command('timename', prefixes=['.', '/']))
def timeName(app, m: Message):
    global timeN
    command = m.command
    try:
        if match(r"(?i)on", command[1]):
            timeN = True
        else:
            timeN = False
        m.edit(isOn.format('Time in Name', 'on' if timeN else 'off'))
    except IndexError:
        m.edit(help)
@app.on_message(command('timebio', prefixes=['.', '/']))
def timeBio(app, m: Message):
    global timeB
    command = m.command
    try:
        if match(r"(?i)on", command[1]):
            timeB = True
        else:
            timeB = False
        m.edit(isOn.format('Time in Bio', 'on' if timeN else 'off'))
    except IndexError:
        m.edit(help)

scduler = AsyncIOScheduler()
scduler.add_job(changeTime, 'interval', seconds=1)
scduler.start()
app.start(), print('started...'), idle(), app.stop()
