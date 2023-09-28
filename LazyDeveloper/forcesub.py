# in & as LazyDeveloper
# Please Don't Remove Credit

import asyncio
from configs import Config
from pyrogram import Client
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message


async def ForceSub(bot: Client, cmd: Message):
    try:
        user = await bot.get_chat_member(chat_id=(int(Config.UPDATES_CHANNEL) if Config.UPDATES_CHANNEL.startswith("-100") else Config.UPDATES_CHANNEL), user_id=cmd.from_user.id)
        if user.status == "kicked":
            await bot.send_message(
                chat_id=cmd.from_user.id,
                text="Hᴇʟʟᴏ ғʀɪᴇɴᴅ ! I ᴛʜɪɴᴋ ʏᴏᴜ ᴀʀᴇ Bᴀɴɴᴇᴅ ᴛᴏ ᴜsᴇ ᴍᴇ. Rᴇǫᴜᴇsᴛ ᴜɴʙᴀɴ ᴛᴏ [Oɴᴡᴇʀ](https://t.me/ROYAL_GAGAN_DEEP_SINGH_MEHRA).",
                parse_mode="markdown",
                disable_web_page_preview=True
            )
            return 400
    except UserNotParticipant:
        try:
            invite_link = await bot.create_chat_invite_link(chat_id=(int(Config.UPDATES_CHANNEL) if Config.UPDATES_CHANNEL.startswith("-100") else Config.UPDATES_CHANNEL))
        except FloodWait as e:
            await asyncio.sleep(e.x)
            invite_link = await bot.create_chat_invite_link(chat_id=(int(Config.UPDATES_CHANNEL) if Config.UPDATES_CHANNEL.startswith("-100") else Config.UPDATES_CHANNEL))
        except Exception as err:
            print(f"Uɴᴀʙʟᴇ Tᴏ Dᴏ Fᴏʀᴄᴇ Sᴜʙsᴄʀɪʙᴇ Tᴏ {Config.UPDATES_CHANNEL}\n\nError: {err}")
            return 200
        await bot.send_message(
            chat_id=cmd.from_user.id,
            text="**🔺 Jᴏɪɴ Uᴘᴅᴀᴛᴇ Cʜᴀɴɴᴇʟ 🔺**\n\n"
                 "⚔️ Oɴʟʏ Hᴜɴᴛᴇʀs ᴏғ ᴍʏ ᴄʜᴀɴɴᴇʟ ᴄᴀɴ ᴜsᴇ ᴍᴇ ⚔️",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔺 Jᴏɪɴ Uᴘᴅᴀᴛᴇ Cʜᴀɴɴᴇʟ 🔺", url=invite_link.invite_link)
                    ],
                    [
                        InlineKeyboardButton("🔄 Rᴇғʀᴇsʜ 🔄", callback_data="refreshForceSub")
                    ]
                ]
            ),
            parse_mode="markdown"
        )
        return 400
    except Exception:
        await bot.send_message(
            chat_id=cmd.from_user.id,
            text="I Dᴏɴ'ᴛ ʟɪᴋᴇ ᴏᴠᴇʀ sᴍᴀʀᴛɴᴇss ᴜsᴇʀ's ♥️.\n »» Jᴏɪɴ Cʜᴀɴɴᴇʟ ᴀɴᴅ ʙᴇ ᴀ Gᴏᴏᴅ ᴜsᴇʀ.",
            parse_mode="markdown",
            disable_web_page_preview=True
        )
        return 400
    return 200
