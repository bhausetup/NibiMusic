import asyncio
import random
from NibiMusic.config import BOT_USERNAME, OWNER_USERNAME, UPDATE_CHANNEL, SUPPORT_GROUP
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


PIYA_IMG = (
"https://telegra.ph/file/0c42c9de2c368b5f691ec.jpg",
"https://telegra.ph/file/b94d7b607054eb0993b93.jpg",
"https://telegra.ph/file/b3a574c42856ad52b0cda.jpg",
"https://telegra.ph/file/af86d5810fbfe32552c7d.jpg",
"https://telegra.ph/file/72fc4ed0b02894736b3b7.jpg",
"https://telegra.ph/file/8c378ce31064792bc8ed8.jpg",
"https://telegra.ph/file/b178b6057234ceaf8e7fb.jpg",

)





START_TEXT = """
ʜɪ ɢᴜʏꜱ, ɪ ᴀᴍ ᴠᴇʀʏ ʜɪɢʜʟʏ ᴀ.ɪ ᴀᴅᴠᴀɴᴄᴇᴅ ɴᴇxᴛ ɢᴇɴᴇʀᴀᴛɪᴏɴ ᴠᴄ ʙᴏᴛ.
ɪ' ᴍ ᴠᴇʀʏ ғᴀꜱᴛ ᴀɴᴅ ᴍᴏʀᴇ ᴇꜰꜰɪᴄɪᴇɴᴛ ɪ ᴘʀᴏᴠɪᴅᴇ ᴀᴡᴇꜱᴏᴍᴇ ꜱᴏᴜɴᴅ ǫᴜᴀʟɪᴛʏ !
"""

    
   

@Client.on_message(filters.command(["start"], prefixes=["/", "!"]))
async def start_(client: Client, message: Message):
    await message.reply_photo(
        random.choice(NIBI_IMG),
        caption=(START_TEXT),
    reply_markup=InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("🔞 ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ 🔞", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
            InlineKeyboardButton("🍂 sᴜᴘᴘᴏʀᴛ", url="https://t.me/{SUPPORT_GROUP}"),
            InlineKeyboardButton("🌾 ᴜᴘᴅᴀᴛᴇs", url="https://t.me/{UPDATE_CHANNEL}")
        ],
        [
            InlineKeyboardButton("🧰 ᴄᴏᴍᴍᴀɴᴅs", callback_data="help_cmd"),
            InlineKeyboardButton("🎓 ᴍᴀɪɴᴛᴀɪɴᴇʀ", url="https://t.me/{OWNER_USERNAME}"),
        ]
   
     ]
  ),
)
    
    
@Client.on_message(filters.command(["repo", "source"]))
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/0c42c9de2c368b5f691ec.jpg",
        caption=f"""ʜᴇʀᴇ ɪs ᴛʜᴇ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ғᴏʀᴋ ᴀɴᴅ ɢɪᴠᴇ sᴛᴀʀs ✨""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " ʀᴇᴘᴏ 🥺", url=f"https://github.com/bhausetup/piyamusic"
                    )
                ]
            ]
        ),
    )
