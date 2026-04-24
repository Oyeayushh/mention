from pyrogram import Client, filters
from pyrogram.types import Message
from AIMentionBot.database import db


@Client.on_message(filters.command("start") & filters.private)
async def start(client: Client, message: Message):
    await db.add_user(message.from_user.id)
    await message.reply(
        "** ᴀɪ ᴍᴇɴᴛɪᴏɴ ʙᴏᴛ**\n\n"
        "ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ & ᴍᴀᴋᴇ ᴍᴇ ᴀᴅᴍɪɴ!\n\n"
        "** ᴛᴀɢ ᴄᴏᴍᴍᴀɴᴅꜱ:**\n"
        "`/tagall` — ᴛᴀɢ ᴀʟʟ ᴍᴇᴍʙᴇʀꜱ \n"
        "`/all` ᴏʀ `@all` — ᴛᴀɢ ᴀʟʟ\n"
        "`/admin` ᴏʀ `@admin` — ᴛᴀɢ ᴀᴅᴍɪɴꜱ ᴏɴʟʏ\n"
        "`/hitag` — ʜɪɴᴅɪ ᴛᴀɢ \n"
        "`/entag` — ᴇɴɢʟɪꜱʜ ᴛᴀɢ \n"
        "`/gmtag` — ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ ᴛᴀɢ \n"
        "`/gntag` — ɢᴏᴏᴅ ɴɪɢʜᴛ ᴛᴀɢ \n"
        "`/jtag` — ᴊᴏᴋᴇ ᴛᴀɢ \n"
        "`/vctag` — ᴠᴄ ɪɴᴠɪᴛᴇ ᴛᴀɢ 🎙️\n\n"
        "** ᴄᴏɴᴛʀᴏʟ** _(ᴀᴅᴍɪɴꜱ)_:\n"
        "`/stop` — ꜱᴛᴏᴘ ᴛᴀɢɢɪɴɢ\n"
        "`/pause` — ᴘᴀᴜꜱᴇ\n"
        "`/resume` — ʀᴇꜱᴜᴍᴇ\n\n"
        "ᴜꜱᴇ `/help` ꜰᴏʀ ꜰᴜʟʟ ᴄᴏᴍᴍᴀɴᴅ ʟɪꜱᴛ",
        disable_web_page_preview=True,
    )


@Client.on_message(filters.command("help"))
async def help_cmd(client: Client, message: Message):
    await message.reply(
        "** ᴀɪ ᴍᴇɴᴛɪᴏɴ ʙᴏᴛ — ᴄᴏᴍᴍᴀɴᴅꜱ**\n\n"
        "** ᴛᴀɢ ᴄᴏᴍᴍᴀɴᴅꜱ:**\n"
        "`/hitag` — ᴛᴀɢ ᴀʟʟ ɪɴ ʜɪɴᴅɪ ꜱᴛʏʟᴇ \n"
        "`/entag` — ᴛᴀɢ ᴀʟʟ ɪɴ ᴇɴɢʟɪꜱʜ \n"
        "`/gmtag` — ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ ᴛᴀɢ \n"
        "`/gntag` — ɢᴏᴏᴅ ɴɪɢʜᴛ ᴛᴀɢ \n"
        "`/tagall` — ɢᴇɴᴇʀᴀʟ ᴛᴀɢ ᴀʟʟ \n"
        "`/jtag` — ᴊᴏᴋᴇ ᴛᴀɢ \n"
        "`/vctag` — ᴠᴄ ɪɴᴠɪᴛᴇ ᴛᴀɢ 🎙️\n\n"
        "** ᴍᴇɴᴛɪᴏɴ:**\n"
        "`/admin` ᴏʀ `@admin` — ᴛᴀɢ ᴀᴅᴍɪɴꜱ\n"
        "`/all` ᴏʀ `@all` — ᴛᴀɢ ᴀʟʟ ᴍᴇᴍʙᴇʀꜱ\n"
        "  _ᴄᴜꜱᴛᴏᴍ ᴍꜱɢ: `/all ᴄᴏᴍᴇ ᴏɴʟɪɴᴇ`_\n\n"
        "** ᴄᴏɴᴛʀᴏʟ** _(ᴀᴅᴍɪɴꜱ ᴏɴʟʏ)_:\n"
        "`/stop` — ꜱᴛᴏᴘ ᴏɴɢᴏɪɴɢ ᴛᴀɢɢɪɴɢ\n"
        "`/pause` — ᴘᴀᴜꜱᴇ ᴛᴀɢɢɪɴɢ\n"
        "`/resume` — ʀᴇꜱᴜᴍᴇ ᴛᴀɢɢɪɴɢ\n\n"
        "** ᴏᴡɴᴇʀ:**\n"
        "`/broadcast <msg>` — ʙʀᴏᴀᴅᴄᴀꜱᴛ\n"
        "`/stats` — ʙᴏᴛ ꜱᴛᴀᴛꜱ",
        disable_web_page_preview=True,
    )


@Client.on_message(filters.group & ~filters.bot)
async def track_group(client: Client, message: Message):
    await db.add_group(message.chat.id)
    if message.from_user:
        await db.add_user(message.from_user.id)
