#!/usr/bin/env python3
# (c) https://t.me/TelethonChat/37677
# This Source Code Form is subject to the terms of the GNU
# General Public License, v.3.0. If a copy of the GPL was not distributed with this
# file, You can obtain one at https://www.gnu.org/licenses/gpl-3.0.en.html.

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

print("Yukki Spam Bot Telethon String Generator")
print("")
API_KEY = "5445895"
API_HASH = "b104f43c21861654005fa97c96a8a06f"

while True:
    try:
        with TelegramClient(StringSession(), API_KEY, API_HASH) as client:
            print("")
            session = client.session.save()
            client.send_message("me", f"`{session}`")
            print(
                "Your Telethon String session has been successfully stored in your telegram, Please check your Telegram Saved Messages"
            )
            print("")
    except:
        print("")
        print("Wrong phone number \n make sure its with correct  country code")
        print("")
        continue
    break
