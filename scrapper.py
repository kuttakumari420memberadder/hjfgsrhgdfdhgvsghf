import os
import time
from telethon.sync import TelegramClient
from telethon import TelegramClient,events,sync
from telethon.sessions import StringSession
from telethon import functions,types
from telethon.sync import TelegramClient
from telethon import functions, types
api_id = "5860415"
api_hash = "3d153613fe2bc0903bffb82df03a36ae"
chan = "hindi_english_chatting_group"
chann = "boyz_girls_chatting"
count = 0

while True:
    try:
        name = str(count)
        agent = open("agent"+name+".txt")
        agent_session = agent.read()
        agent.close()
    except:
        count = 0
    count2 = 0
    string_session = str(agent_session)
    client = TelegramClient(StringSession(string_session), api_id, api_hash)
    client.start()
    for user in client.iter_participants(chan):
        if count2 == 12:
            break
        else:
            try:
                userinfo = client(functions.users.GetFullUserRequest(
                    id=user.username
                ))
                try: 
                    result = client(functions.contacts.AddContactRequest(
                        id=user.username,
                        first_name=userinfo.user.first_name,
                        last_name=userinfo.user.last_name,
                        phone = "+91 ",
                        add_phone_privacy_exception=False
                    ))

                    try:
                        scrap = client(functions.channels.InviteToChannelRequest(
                            channel=chann,
                            users=[user.username]
                        ))
                        count2 = count2+1
                        print("member added")
                    except:
                        pass
                except:
                    pass
            except:
                pass
    count = count+1    
print(count*12," Members Scrapped Successfully.")

