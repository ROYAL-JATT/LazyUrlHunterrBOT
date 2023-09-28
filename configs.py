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
    ABOUT_BOT_TEXT = """<b> <a href='https://t.me/MOVIES_VILLA_UPDATE'>GɪᴛHᴜʙ ᴄᴏᴅᴇ</a> is an open source project.

    Devs: 
        <a href='https://t.me/ROYAL_GAGAN_DEEP_SINGH_MEHRA'>❤️ Oɴᴡᴇʀ ❤️</a>
    
    
🤖 Mʏ Nᴀᴍᴇ: <a href='https://t.me/Official_Movies_Group'>Mdisk Search Robot</a>

📝 Lᴀɴɢᴜᴀɢᴇ: <a href='https://www.python.org'>Python V3</a>

📚 Lɪʙʀᴀʀʏ: <a href='https://docs.pyrogram.org'>Pyrogram</a>

📡 Sᴇʀᴠᴇʀ: <a href='https://heroku.com'>Heroku</a>

📡 Sᴇʀᴠᴇʀ 2: <a href='https://heroku.com'>koyeb</a> <i>comming soon</i>

👨‍💻 Dᴇᴠᴇʟᴏᴘᴇʀ Cʜᴀɴɴᴇʟ: <a href='https://t.me/LazyDeveloper'>LazyDeveloper</a></b>
"""

    ABOUT_HELP_TEXT = """<b>💋 Developer : <a href='https://t.me/LazyDeveloper'>LazyDeveloper</a>

If You Want Your Own Bot Like This Then You Can Contact Our Developer.</b>
"""

    HOME_TEXT = """
<b>Hello Baby ! {}😅,

I'm the one and only fastest URL finder BOT. Add me to any Group and Give me Hunting rights !!

I will be only yours if you will restrict adding me to other groups.
Go to @BotFather to change settings.

Don't be sad ! Your all urls are in safe Hand.

»»» <b>Happy Hunting</b> «««

🔺Thank You <a href='https://t.me/LazyDeveloper'>LazyDeveloper</a>🔺 </b>
"""


    START_MSG = """
<b>Hello Baby ! {}😅,

I'm the one and only fastest URL & post finder BOT. Add me to any Group and Give me Hunting rights !!

Don't be sad ! Your all urls are in safe Hand.</b>

   »»»» <b>Happy Hunting</b> ««««

💸<b>Donate us to Keep service Alive.💸</b>
»» A small amount of ₹5 - ₹20 - ₹50 - ₹100 will be great help !
🔺 Thank You 🔺 
"""

