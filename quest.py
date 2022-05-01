######
# autodefender.py
# automatically respond to forays on ChatWars
######

import time
from telethon import TelegramClient, events
import emoji
import random
import datetime
import asyncio 

# add your own details here ...
api_id = 17356283
api_hash = 'c66e4cba1efe2a4fb6348d18dc22dafe'

# ... and here
phone = '+5353252471'
session_file = 'Infinite_ashes'
rss=65
TRADER = "^You defended villagers well. In exchange for your help, local trader offered you a deal you can't refuse. " \
         "He is going to buy some of your resources for whole 2💰 per item. However, he is leaving to distant lands " \
         "and his caravan can only carry (?P<Carry>\\d{1,4})."

client = TelegramClient(session_file, api_id, api_hash, sequential_updates=True)

@client.on(events.NewMessage(chats = '@chtwrsbot', incoming=True))

async def handle_new_message(event):

            if "Item used: Vial of Rage" in event.raw_text:
                t = random.random() *2 +2
                print(datetime.datetime.now(), 'waiting', t, 'sec')
                await asyncio.sleep(t)
                await client.send_message('@chtwrsbot', '/use_p02')

            if "Item used: Potion of Rage" in event.raw_text:
                t = random.random() *2 +3
                print(datetime.datetime.now(), 'waiting', t, 'sec')
                await asyncio.sleep(t)
                await client.send_message('@chtwrsbot', '/use_p03')

            if "Item used: Duality Vial" in event.raw_text:
                t = random.random() *2 +2
                print(datetime.datetime.now(), 'waiting', t, 'sec')
                await asyncio.sleep(t)
                await client.send_message('@chtwrsbot', '/use_p38')

            if "Item used: Duality Potion" in event.raw_text:
                t = random.random() *2 +3
                print(datetime.datetime.now(), 'waiting', t, 'sec')
                await asyncio.sleep(t)
                await client.send_message('@chtwrsbot', '/use_p39')

            if "/g_hire" in event.raw_text:
                expresion = event.raw_text
                localizador = expresion.find('/g_hire')
                t = random.random() *1
                print(datetime.datetime.now(), 'waiting', t, 'sec')
                await asyncio.sleep(t)
                await client.send_message('@chtwrsbot', expresion[localizador:])

            if "You were strolling around" in event.raw_text:
                t = random.random() *2 *30
                print(datetime.datetime.now(), 'waiting', t, 'sec')
                await asyncio.sleep(t)
                await event.click(text='🧹Intervene')

#SETSU
@client.on(events.NewMessage(chats = '@sawamura_setsu', incoming=True))

async def handle_new_message(event):
            if "You met" in event.raw_text:
                expresion = event.raw_text
                localizador = expresion.find('/fight_')
                t = 1
                print(datetime.datetime.now(), 'waiting', t, 'sec')
                await asyncio.sleep(t)
                await client.send_message('@chtwrsbot', expresion[localizador:])

#jose
@client.on(events.NewMessage(chats = '@Berkelio', incoming=True))

async def handle_new_message(event):
            if "/fight" in event.raw_text:
                expresion = event.raw_text
                localizador = expresion.find('/fight_')
                t = random.random() 
                print(datetime.datetime.now(), 'waiting', t, 'sec')
                await asyncio.sleep(t)
                await client.send_message('@chtwrsbot', expresion[localizador:])

#Hector
@client.on(events.NewMessage(chats = '@FleitesM', incoming=True))

async def handle_new_message(event):
            if "You met" in event.raw_text:
                expresion = event.raw_text
                localizador = expresion.find('/fight_')
                t = random.random() *1
                print(datetime.datetime.now(), 'waiting', t, 'sec')
                await asyncio.sleep(t)
                await client.send_message('@chtwrsbot', expresion[localizador:])

#ANGRYBIRD
@client.on(events.NewMessage(chats = '@birds2angry_bot', incoming=True))

async def handle_new_message(event):
            if "You met" in event.raw_text:
                expresion = event.raw_text
                localizador = expresion.find('/fight_')
                t = random.random() 
                print(datetime.datetime.now(), 'waiting', t, 'sec')
                
                await client.send_message('@chtwrsbot', expresion[localizador:])


#Fullmercenary
@client.on(events.NewMessage(chats = '@VolundurShopBot', incoming=True))

async def handle_new_message(event):

            if "Fullmercenary" in event.raw_text:
                t = 1
                print(datetime.datetime.now(), 'waiting', t, 'sec')
                await asyncio.sleep(t)
                await client.send_message('@chtwrsbot', '/use_wng_call_0')

            if "Fullmercenary" in event.raw_text:
                t = 2
                print(datetime.datetime.now(), 'waiting', t, 'sec')
                await asyncio.sleep(t)
                await client.send_message('@chtwrsbot', '/use_wng_call_1')

            if "Fullmercenary" in event.raw_text:
                t = 3
                print(datetime.datetime.now(), 'waiting', t, 'sec')
                await asyncio.sleep(t)
                await client.send_message('@chtwrsbot', '/use_wng_call_2')



@client.on(events.NewMessage(chats = '@chtwrsbot', incoming=True, pattern=TRADER))

async def handler_trader(event: events.NewMessage.Event):
                await asyncio.sleep(random.randint(5, 10))
                carry = int(event.pattern_match.group(1))
                trade = '/sc_{}_{}'.format(rss, carry)
                await client.send_message('@chtwrsbot', message=trade)

client.start(phone)
client.run_until_disconnected()
