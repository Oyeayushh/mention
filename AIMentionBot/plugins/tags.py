import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from AIMentionBot.helpers import get_all_members, tag_users
from AIMentionBot import state

JOKES = [
    "ᴛᴇᴀᴄʜᴇʀ: ᴄᴏᴍᴇ ᴛᴏᴍᴏʀʀᴏᴡ. sᴛᴜᴅᴇɴᴛ: ᴡʜʏ? ᴛᴇᴀᴄʜᴇʀ: ᴇxᴀᴍ ʜᴀɪ. sᴛᴜᴅᴇɴᴛ: ᴛᴏ ᴋʏᴀ ʜᴜᴀ, ᴍᴀɪɴ ᴛᴏʜ ᴡᴀɪsᴇ ʙʜɪ ɴᴀʜɪ ᴀᴀᴛᴀ 😂",
    "ᴀ ᴍᴀɴ ᴡᴇɴᴛ ᴛᴏ ᴀ sʜᴏᴘ: ɢɪᴠᴇ ᴍᴇ 1ᴋɢ ᴏʀᴀɴɢᴇs. sʜᴏᴘᴋᴇᴇᴘᴇʀ: ɴᴏ ᴏʀᴀɴɢᴇs. ᴍᴀɴ: ᴏᴋ ᴀᴘᴘʟᴇs. sʜᴏᴘᴋᴇᴇᴘᴇʀ: ɴᴏ ᴀᴘᴘʟᴇs. ᴍᴀɴ: ᴏᴋ ʙᴀɴᴀɴᴀs. sʜᴏᴘᴋᴇᴇᴘᴇʀ: ɴᴏᴛʜɪɴɢ ᴀᴛ ᴀʟʟ! ᴍᴀɴ: ᴛʜᴇɴ ᴡʜʏ ᴅɪᴅ ʏᴏᴜ ᴏᴘᴇɴ ᴛʜᴇ sʜᴏᴘ? 😆",
    "ᴡɪꜰᴇ: ᴛᴏᴅᴀʏ ᴡᴀs ꜱᴏ ʙᴏʀɪɴɢ. ʜᴜꜱʙᴀɴᴅ: ʏᴇᴀʜ, ɪ ᴡᴀs ʜᴏᴍᴇ ᴛᴏᴏ 🥲",
    "ᴇᴠᴇʀʏᴏɴᴇ ꜱᴀʏꜱ ꜱᴛᴜᴅʏ ʜᴀʀᴅ... ʙᴜᴛ ᴡʜᴀᴛ'ꜱ ᴛʜᴇ ᴘᴏɪɴᴛ ʀɪɢʜᴛ? 😂",
    "ʀᴇꜱᴜʟᴛ ᴄᴀᴍᴇ, ᴅᴀᴅ ᴀꜱᴋᴇᴅ ʜᴏᴡ ᴍᴀɴʏ ᴍᴀʀᴋꜱ. ɪ ꜱᴀɪᴅ 'ᴛʜʀᴇᴇ' — ʜᴇ ᴛʜᴏᴜɢʜᴛ 300, ɪ ᴍᴇᴀɴᴛ 3 ꜱᴜʙᴊᴇᴄᴛꜱ ᴘᴀꜱꜱᴇᴅ 😅",
]

_joke_index = {}

def next_joke(chat_id: int) -> str:
    idx = _joke_index.get(chat_id, 0)
    joke = JOKES[idx % len(JOKES)]
    _joke_index[chat_id] = idx + 1
    return joke


async def _run_tag(client, message, members, prefix, custom_text=None):
    """asyncio.create_task ke bajaaye seedha await — loop issue fix."""
    await tag_users(client, message, members, custom_text=custom_text, prefix=prefix)


# ─── /tagall ──────────────────────────────────────────────────
@Client.on_message(filters.command("tagall") & filters.group)
async def tagall(client: Client, message: Message):
    if state.is_running(message.chat.id):
        return await message.reply("⚠️ **ᴛᴀɢɢɪɴɢ ᴀʟʀᴇᴀᴅʏ ʀᴜɴɴɪɴɢ!** ᴜꜱᴇ `/stop` ꜰɪʀꜱᴛ.")
    members = await get_all_members(client, message.chat.id)
    if not members:
        return await message.reply("❌ **ɴᴏ ᴍᴇᴍʙᴇʀꜱ ꜰᴏᴜɴᴅ.**")
    await message.reply(f"🔥 **ᴛᴀɢᴀʟʟ ꜱᴛᴀʀᴛᴇᴅ!** ᴛᴏᴛᴀʟ: `{len(members)}`")
    await _run_tag(client, message, members, prefix="🔥 ʜᴇʏ ᴇᴠᴇʀʏᴏɴᴇ, ᴄᴏᴍᴇ ʜᴇʀᴇ!")


# ─── /hitag ───────────────────────────────────────────────────
@Client.on_message(filters.command("hitag") & filters.group)
async def hitag(client: Client, message: Message):
    if state.is_running(message.chat.id):
        return await message.reply("⚠️ **ᴛᴀɢɢɪɴɢ ᴀʟʀᴇᴀᴅʏ ʀᴜɴɴɪɴɢ!**")
    members = await get_all_members(client, message.chat.id)
    if not members:
        return await message.reply("❌ **ɴᴏ ᴍᴇᴍʙᴇʀꜱ ꜰᴏᴜɴᴅ.**")
    await message.reply(f"🇮🇳 **ʜɪɴᴅɪ ᴛᴀɢ ꜱᴛᴀʀᴛᴇᴅ!** ᴛᴏᴛᴀʟ: `{len(members)}`")
    await _run_tag(client, message, members, prefix="🇮🇳 ʏᴀᴀʀ ʟᴏɢ! ɪᴅʜᴀʀ ᴀᴀᴏ, ᴋᴜᴄʜ ᴢᴀʀᴏᴏʀɪ ʙᴀᴀᴛ ʜᴀɪ!")


# ─── /entag ───────────────────────────────────────────────────
@Client.on_message(filters.command("entag") & filters.group)
async def entag(client: Client, message: Message):
    if state.is_running(message.chat.id):
        return await message.reply("⚠️ **ᴛᴀɢɢɪɴɢ ᴀʟʀᴇᴀᴅʏ ʀᴜɴɴɪɴɢ!**")
    members = await get_all_members(client, message.chat.id)
    if not members:
        return await message.reply("❌ **ɴᴏ ᴍᴇᴍʙᴇʀꜱ ꜰᴏᴜɴᴅ.**")
    await message.reply(f"🇬🇧 **ᴇɴɢʟɪꜱʜ ᴛᴀɢ ꜱᴛᴀʀᴛᴇᴅ!** ᴛᴏᴛᴀʟ: `{len(members)}`")
    await _run_tag(client, message, members, prefix="🇬🇧 ʜᴇʏ ᴇᴠᴇʀʏᴏɴᴇ! ᴄᴏᴍᴇ ᴏɴ ᴏᴠᴇʀ, ꜱᴏᴍᴇᴛʜɪɴɢ ɪᴍᴘᴏʀᴛᴀɴᴛ!")


# ─── /gmtag ───────────────────────────────────────────────────
@Client.on_message(filters.command("gmtag") & filters.group)
async def gmtag(client: Client, message: Message):
    if state.is_running(message.chat.id):
        return await message.reply("⚠️ **ᴛᴀɢɢɪɴɢ ᴀʟʀᴇᴀᴅʏ ʀᴜɴɴɪɴɢ!**")
    members = await get_all_members(client, message.chat.id)
    if not members:
        return await message.reply("❌ **ɴᴏ ᴍᴇᴍʙᴇʀꜱ ꜰᴏᴜɴᴅ.**")
    await message.reply(f"☀️ **ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ ᴛᴀɢ ꜱᴛᴀʀᴛᴇᴅ!** ᴛᴏᴛᴀʟ: `{len(members)}`")
    await _run_tag(client, message, members, prefix="☀️ ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ ᴇᴠᴇʀʏᴏɴᴇ! ʀɪꜱᴇ & ꜱʜɪɴᴇ, ɴᴇᴡ ᴅᴀʏ ʜᴀꜱ ʙᴇɢᴜɴ!")


# ─── /gntag ───────────────────────────────────────────────────
@Client.on_message(filters.command("gntag") & filters.group)
async def gntag(client: Client, message: Message):
    if state.is_running(message.chat.id):
        return await message.reply("⚠️ **ᴛᴀɢɢɪɴɢ ᴀʟʀᴇᴀᴅʏ ʀᴜɴɴɪɴɢ!**")
    members = await get_all_members(client, message.chat.id)
    if not members:
        return await message.reply("❌ **ɴᴏ ᴍᴇᴍʙᴇʀꜱ ꜰᴏᴜɴᴅ.**")
    await message.reply(f"🌙 **ɢᴏᴏᴅ ɴɪɢʜᴛ ᴛᴀɢ ꜱᴛᴀʀᴛᴇᴅ!** ᴛᴏᴛᴀʟ: `{len(members)}`")
    await _run_tag(client, message, members, prefix="🌙 ɢᴏᴏᴅ ɴɪɢʜᴛ ᴇᴠᴇʀʏᴏɴᴇ! ʀᴇꜱᴛ ᴡᴇʟʟ, ꜱᴇᴇ ʏᴏᴜ ᴛᴏᴍᴏʀʀᴏᴡ!")


# ─── /jtag ────────────────────────────────────────────────────
@Client.on_message(filters.command("jtag") & filters.group)
async def jtag(client: Client, message: Message):
    if state.is_running(message.chat.id):
        return await message.reply("⚠️ **ᴛᴀɢɢɪɴɢ ᴀʟʀᴇᴀᴅʏ ʀᴜɴɴɪɴɢ!**")
    members = await get_all_members(client, message.chat.id)
    if not members:
        return await message.reply("❌ **ɴᴏ ᴍᴇᴍʙᴇʀꜱ ꜰᴏᴜɴᴅ.**")
    joke = next_joke(message.chat.id)
    await message.reply(f"😂 **ᴊᴏᴋᴇ ᴛᴀɢ ꜱᴛᴀʀᴛᴇᴅ!** ᴛᴏᴛᴀʟ: `{len(members)}`")
    await _run_tag(client, message, members, custom_text=f"😂 {joke}", prefix="")


# ─── /vctag ───────────────────────────────────────────────────
@Client.on_message(filters.command("vctag") & filters.group)
async def vctag(client: Client, message: Message):
    if state.is_running(message.chat.id):
        return await message.reply("⚠️ **ᴛᴀɢɢɪɴɢ ᴀʟʀᴇᴀᴅʏ ʀᴜɴɴɪɴɢ!**")
    members = await get_all_members(client, message.chat.id)
    if not members:
        return await message.reply("❌ **ɴᴏ ᴍᴇᴍʙᴇʀꜱ ꜰᴏᴜɴᴅ.**")
    await message.reply(f"🎙️ **ᴠᴄ ɪɴᴠɪᴛᴇ ᴛᴀɢ ꜱᴛᴀʀᴛᴇᴅ!** ᴛᴏᴛᴀʟ: `{len(members)}`")
    await _run_tag(client, message, members, prefix="🎙️ ʜᴇʏ! ᴊᴏɪɴ ᴛʜᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ɴᴏᴡ, ᴇᴠᴇʀʏᴏɴᴇ ᴄᴏᴍᴇ!")
