import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from SiestaRobot.events import register
from SiestaRobot import telethn as tbot


PHOTO = "https://telegra.ph/file/ae1dfcc5b4474d498c2df.jpg"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**Hɪ [{event.sender.first_name}](tg://user?id={event.sender.id}), I'ᴍ ɪᴄʜɪɢᴏ.** \n\n"
  TEXT += "× **I'ᴍ Wᴏʀᴋɪɴɢ Pʀᴏᴘᴇʀʟʏ** \n\n"
  TEXT += f"× **Mʏ Mᴀsᴛᴇʀ : [Asᴛᴀ](https://t.me/baby_hoi)** \n\n"
  TEXT += f"× **Lɪʙʀᴀʀʏ Vᴇʀsɪᴏɴ  :** `{telever}` \n\n"
  TEXT += f"× **Tᴇʟᴇᴛʜᴏɴ Vᴇʀsɪᴏɴ :** `{tlhver}` \n\n"
  TEXT += f"× **Pʏʀᴏɢʀᴀᴍ Vᴇʀsɪᴏɴ :** `{pyrover}` \n\n"
  TEXT += "**I ᴡᴏɴ' ᴛ ʟᴇᴀᴠᴇ ʏᴏᴜ sᴏ sᴏᴏɴ ʙᴀᴋᴀ!**"
  BUTTON = [[Button.url("Help", "https://t.me/ichigoxsinbot?start=help"), Button.url("Support", "https://t.me/ichigosupportchat")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
