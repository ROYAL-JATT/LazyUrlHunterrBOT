# in & as LazyDeveloper
# Please Don't Remove Credit

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "MdiskSearchBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -100))
    BOT_USERNAME = os.environ.get("BOT_USERNAME")
    BOT_OWNER = int(os.environ.get("BOT_OWNER"))
    DATABASE_URL = os.environ.get("DATABASE_URL")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    ABOUT_BOT_TEXT = """<b> <a href='https://t.me/MOVIES_VILLA_UPDATE'>GɪᴛHᴜʙ ᴄᴏᴅᴇ</a> ɪs ᴀɴ ᴏᴘᴇɴ sᴏᴜʀᴄᴇ ᴘʀᴏJᴇᴄᴛ.

    Devs: 
        <a href='https://t.me/ROYAL_GAGAN_DEEP_SINGH_MEHRA'>❤️ Oɴᴡᴇʀ ❤️</a>
    
    
🤖 Mʏ Nᴀᴍᴇ: <a href='https://t.me/Hindi_movies_villa'>Ipopcorn search Bot</a>

📝 Lᴀɴɢᴜᴀɢᴇ: <a href='https://www.python.org'>Pʏᴛʜᴏɴ V𝟹</a>

📚 Lɪʙʀᴀʀʏ: <a href='https://docs.pyrogram.org'>Pʏʀᴏɢʀᴀᴍ</a>

📡 Sᴇʀᴠᴇʀ: <a href='https://heroku.com'>Hᴇʀᴏᴋᴜ</a>

📡 Sᴇʀᴠᴇʀ 2: <a href='https://heroku.com'>ᴋᴏʏᴇʙ</a> <i>comming soon</i>

👨‍💻 Dᴇᴠᴇʟᴏᴘᴇʀ Cʜᴀɴɴᴇʟ: <a href='https://t.me/MOVIES_VILLA_UPDATE'>Mᴏᴠɪᴇs Vɪʟʟᴀ</a></b>
"""

    ABOUT_HELP_TEXT = """<b>👑 Dᴇᴠᴇʟᴏᴘᴇʀ : <a href='https://t.me/Bot_maker_786'>♥️👑Oɴᴡᴇʀ👑♥️</a>

Iғ Yᴏᴜ Wᴀɴᴛ Yᴏᴜʀ Oᴡɴ Bᴏᴛ Lɪᴋᴇ Tʜɪs Tʜᴇɴ Yᴏᴜ Cᴀɴ Cᴏɴᴛᴀᴄᴛ Oᴜʀ Dᴇᴠᴇʟᴏᴘᴇʀ.</b>
"""

    HOME_TEXT = """
<b>Hᴇʟʟᴏ Bᴀʙʏ ! ✨{}🎉,

I'ᴍ ᴛʜᴇ ᴏɴᴇ ᴀɴᴅ ᴏɴʟʏ ғᴀsᴛᴇsᴛ URL ғɪɴᴅᴇʀ BOT. Aᴅᴅ ᴍᴇ ᴛᴏ ᴀɴʏ Gʀᴏᴜᴘ ᴀɴᴅ Gɪᴠᴇ ᴍᴇ Hᴜɴᴛɪɴɢ ʀɪɢʜᴛs !!

I ᴡɪʟʟ ʙᴇ ᴏɴʟʏ ʏᴏᴜʀs ɪғ ʏᴏᴜ ᴡɪʟʟ ʀᴇsᴛʀɪᴄᴛ ᴀᴅᴅɪɴɢ ᴍᴇ ᴛᴏ ᴏᴛʜᴇʀ ɢʀᴏᴜᴘs.
Gᴏ ᴛᴏ @BᴏᴛFᴀᴛʜᴇʀ ᴛᴏ ᴄʜᴀɴɢᴇ sᴇᴛᴛɪɴɢs.

Dᴏɴ'ᴛ ʙᴇ sᴀᴅ ! Yᴏᴜʀ ᴀʟʟ ᴜʀʟs ᴀʀᴇ ɪɴ sᴀғᴇ Hᴀɴᴅ.
»»» <b>Hᴀᴘᴘʏ ♥️ ᴜsᴇʀ's</b> «««

🔺Tʜᴀɴᴋ Yᴏᴜ <a href='https://t.me/Punjabi_movies_villa'>Mᴏᴠɪᴇs Vɪʟʟᴀ</a>🔺 </b>
"""


    START_MSG = """
<b>Hᴇʟʟᴏ Bᴀʙʏ ! ✨{}🎉,

I'ᴍ ᴛʜᴇ ᴏɴᴇ ᴀɴᴅ ᴏɴʟʏ ғᴀsᴛᴇsᴛ URL & ᴘᴏsᴛ ғɪɴᴅᴇʀ BOT. Aᴅᴅ ᴍᴇ ᴛᴏ ᴀɴʏ Gʀᴏᴜᴘ ᴀɴᴅ Gɪᴠᴇ ᴍᴇ Hᴜɴᴛɪɴɢ ʀɪɢʜᴛs !!

Dᴏɴ'ᴛ ʙᴇ sᴀᴅ ! Yᴏᴜʀ ᴀʟʟ ᴜʀʟs ᴀʀᴇ ɪɴ sᴀғᴇ Hᴀɴᴅ.

   »»»» <b>Hᴀᴘᴘʏ Hᴜɴᴛɪɴɢ</b> ««««

💸<b>Dᴏɴᴀᴛᴇ ᴜs ᴛᴏ Kᴇᴇᴘ sᴇʀᴠɪᴄᴇ Aʟɪᴠᴇ.💸</b>
»» A sᴍᴀʟʟ ᴀᴍᴏᴜɴᴛ ᴏғ ₹𝟻 - ₹𝟸𝟶 - ₹𝟻𝟶 - ₹𝟷𝟶𝟶 ᴡɪʟʟ ʙᴇ ɢʀᴇᴀᴛ ʜᴇʟᴘ !
🔺 Tʜᴀɴᴋ Yᴏᴜ 🔺
"""

