# in & as LazyDeveloper
# Please Don't Remove Credit

from configs import Config
from pyrogram import Client, filters, idle
from pyrogram.errors import QueryIdInvalid
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, InlineQuery, InlineQueryResultArticle,InputTextMessageContent
from LazyDeveloper.forcesub import ForceSub
import asyncio

# Bot Client for Inline Search
Bot = Client(
    session_name=Config.BOT_SESSION_NAME,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN
)

# User Client for Searching in Channel.
User = Client(
    session_name=Config.USER_SESSION_STRING,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH
)

@Bot.on_message(filters.private & filters.command("start"))
async def start_handler(_, event: Message):
	await event.reply_photo("https://telegra.ph/file/3bb3f8144a129ffdd1f72.jpg",
                                caption=Config.START_MSG.format(event.from_user.mention),
                                reply_markup=InlineKeyboardMarkup([
                                    [InlineKeyboardButton("🔺 Dᴏɴᴀᴛᴇ ᴜs 🔺", url="https://t.me/movies_villa_backup")],
                                    [InlineKeyboardButton("⚡️ Oᴜʀ ᴄʜᴀɴɴᴇʟ ⚡️", url="https://t.me/+Uc5as8cTX_kzYmU9")],
                                    [InlineKeyboardButton("🤒Hᴇʟᴘ", callback_data="Help_msg"),
                                    InlineKeyboardButton("🦋Aʙᴏᴜᴛ", callback_data="About_msg")]]))

@Bot.on_message(filters.private & filters.command("help"))
async def help_handler(_, event: Message):

    await event.reply_text(Config.ABOUT_HELP_TEXT.format(event.from_user.mention),
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("Uᴘᴅᴀᴛᴇs", url="https://t.me/MOVIES_VILLA_UPDATE"),
             InlineKeyboardButton("Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ", url="https://t.me/Movies_villae"), 
             InlineKeyboardButton("Aʙᴏᴜᴛ", callback_data="About_msg")]
        ])
    )

@Bot.on_message(filters.incoming)
async def inline_handlers(_, event: Message):
    if event.text == '/start':
        return
    answers = f'**📂 Hᴜɴᴛs Fᴏʀ ➠ {event.text} \n⟥⟥⟥⟥⟥⟥⟥⟥⟥⟥⟥⟥⟥⟤\n🔊\n➠ Tʏᴘᴇ Oɴʟʏ Mᴏᴠɪᴇ Nᴀᴍᴇ Wɪᴛʜ Cᴏʀʀᴇᴄᴛ Sᴘᴇʟʟɪɴɢ. Dᴏɴᴛ ᴛʏᴘᴇ BʜᴇJᴏ, BʜᴇJ Dᴏ, sᴇɴᴅ ᴍᴇ ᴇᴛᴄ...✍️\n➠ Aᴅᴅ Yᴇᴀʀ Fᴏʀ Bᴇᴛᴛᴇʀ Rᴇsᴜʟᴛ.🗓️\n⟥⟥⟥⟥⟥⟥⟥⟥⟥⟥⟥⟥⟥⟤\n\n**'
    async for message in User.search_messages(chat_id=Config.CHANNEL_ID, limit=50, query=event.text):
        if message.text:
            thumb = None
            f_text = message.text
            msg_text = message.text.html
            if "|||" in message.text:
                f_text = message.text.split("|||", 1)[0]
                msg_text = message.text.html.split("|||", 1)[0]
            answers += f'**🎞 Mᴏᴠɪᴇ Tɪᴛʟᴇ ➠ ' + '' + f_text.split("\n", 1)[0] + '' + '\n\n📜 Dᴏᴡɴʟᴏᴀᴅ URLs ➠ ' + '' + f_text.split("\n", 2)[-1] + ' \n\n▰▱▰▱▰▱▰▱▰▱▰▱▰▱\nLɪɴᴋ Wɪʟʟ Aᴜᴛᴏ Dᴇʟᴇᴛᴇ Iɴ 𝟹𝟻Sᴇᴄ...⏰\n▰▱▰▱▰▱▰▱▰▱▰▱▰▱\n\n**'
    try:
        msg = await event.reply_text(answers)
        await asyncio.sleep(35)
        await event.delete()
        await msg.delete()
    except:
        print(f"[{Config.BOT_SESSION_NAME}] - Fᴀɪʟᴇᴅ ᴛᴏ Aɴsᴡᴇʀ - {event.from_user.first_name}")


@Bot.on_callback_query()
async def button(bot, cmd: CallbackQuery):
        cb_data = cmd.data
        if "About_msg" in cb_data:
            await cmd.message.edit(
			text=Config.ABOUT_BOT_TEXT,
			disable_web_page_preview=True,
			reply_markup=InlineKeyboardMarkup(
				[
					[
						InlineKeyboardButton("Uᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ", url="https://t.me/Punjabi_movies_villa")
					],
					[
						InlineKeyboardButton("Cᴏɴɴᴇᴄᴛ Aᴅᴍɪɴ", url="https://t.me/Bot_maker_786"),
						InlineKeyboardButton("🏠Hᴏᴍᴇ", callback_data="gohome")
					]
				]
			),
			parse_mode="html"
		)
        elif "Help_msg" in cb_data:
            await cmd.message.edit(
			text=Config.ABOUT_HELP_TEXT,
			disable_web_page_preview=True,
			reply_markup=InlineKeyboardMarkup(
				[
					[   InlineKeyboardButton("Hᴇʟᴘ", callback_data="Help_msg"),
						InlineKeyboardButton("Uᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ", url="https://t.me/MOVIES_VILLA_UPDATE")
					], 
                    [
						InlineKeyboardButton("Cᴏɴɴᴇᴄᴛ Aᴅᴍɪɴ", url="https://t.me/Bot_maker_786"),
						InlineKeyboardButton("🏠Hᴏᴍᴇ", callback_data="gohome")
					]
				]
			),
			parse_mode="html"
		)
        elif "gohome" in cb_data:
            await cmd.message.edit(
			text=Config.START_MSG.format(cmd.from_user.mention),
			disable_web_page_preview=True,
			reply_markup=InlineKeyboardMarkup(
				[
                    [
						InlineKeyboardButton("Hᴇʟᴘ", callback_data="Help_msg"),
						InlineKeyboardButton("Aʙᴏᴜᴛ", callback_data="About_msg")
					],
					[
						InlineKeyboardButton("Sᴜᴘᴘᴏʀᴛ Cʜᴀɴɴᴇʟ", url="https://t.me/Hindi_movies_villa"),
					]
				]
			),
			parse_mode="html"
		)

# Start Clients
Bot.start()
User.start()
# Loop Clients till Disconnects
idle()
# After Disconnects,
# Stop Clients
Bot.stop()
User.stop()
