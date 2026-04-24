import asyncio
import re
from pyrogram import Client, filters
from pyrogram.types import Message
from AIMentionBot.helpers import get_all_members, get_admin_members, tag_users
from AIMentionBot import state


# ─── /all or @all ─────────────────────────────────────────────
@Client.on_message(
    filters.group &
    (filters.command("all") | filters.regex(r"^@all\b"))
)
async def mention_all(client: Client, message: Message):
    if state.is_running(message.chat.id):
        return await message.reply("⚠️ **ᴛᴀɢɢɪɴɢ ᴀʟʀᴇᴀᴅʏ ʀᴜɴɴɪɴɢ!**")

    text = message.text or ""
    custom = re.sub(r"^(/all|@all)\s*", "", text).strip() or None

    members = await get_all_members(client, message.chat.id)
    if not members:
        return await message.reply("❌ **ɴᴏ ᴍᴇᴍʙᴇʀꜱ ꜰᴏᴜɴᴅ.**")

    await message.reply(f"🔥 **ᴛᴀɢɢɪɴɢ ᴇᴠᴇʀʏᴏɴᴇ!** ᴛᴏᴛᴀʟ: `{len(members)}`")
    await tag_users(client, message, members, custom_text=custom, prefix="📢")


# ─── /admin or @admin ─────────────────────────────────────────
@Client.on_message(
    filters.group &
    (filters.command("admin") | filters.regex(r"^@admin\b"))
)
async def mention_admins(client: Client, message: Message):
    if state.is_running(message.chat.id):
        return await message.reply("⚠️ **ᴛᴀɢɢɪɴɢ ᴀʟʀᴇᴀᴅʏ ʀᴜɴɴɪɴɢ!**")

    text = message.text or ""
    custom = re.sub(r"^(/admin|@admin)\s*", "", text).strip() or None

    admins = await get_admin_members(client, message.chat.id)
    if not admins:
        return await message.reply("❌ **ɴᴏ ᴀᴅᴍɪɴꜱ ꜰᴏᴜɴᴅ.**")

    await message.reply(f"👮 **ᴛᴀɢɢɪɴɢ ᴀᴅᴍɪɴꜱ!** ᴛᴏᴛᴀʟ: `{len(admins)}`")
    await tag_users(client, message, admins, custom_text=custom, prefix="👮")
