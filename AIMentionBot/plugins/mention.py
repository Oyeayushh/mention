import asyncio
import re
from pyrogram import Client, filters
from pyrogram.types import Message
from AIMentionBot.helpers import get_all_members, get_admin_members, tag_users, is_admin
from AIMentionBot import state


def extract_custom_msg(text: str, command: str) -> str:
    """Extract custom message after command."""
    parts = text.split(None, 1)
    if len(parts) > 1:
        return parts[1]
    return None


# ─── /all or @all ─────────────────────────────────────────────
@Client.on_message(
    filters.group &
    (filters.command("all") | filters.regex(r"^@all\b"))
)
async def mention_all(client: Client, message: Message):
    if state.is_running(message.chat.id):
        return await message.reply("⚠️ Pehle wali tagging chal rahi hai!")

    text = message.text or ""
    # Extract custom message after @all or /all
    custom = re.sub(r"^(/all|@all)\s*", "", text).strip() or None

    members = await get_all_members(client, message.chat.id)
    if not members:
        return await message.reply("❌ Members nahi mile.")

    await message.reply(f"🔥 **Sabko tag kar raha hoon!** Total: `{len(members)}`")
    asyncio.create_task(
        tag_users(client, message, members, custom_text=custom, prefix="📢")
    )


# ─── /admin or @admin ─────────────────────────────────────────
@Client.on_message(
    filters.group &
    (filters.command("admin") | filters.regex(r"^@admin\b"))
)
async def mention_admins(client: Client, message: Message):
    if state.is_running(message.chat.id):
        return await message.reply("⚠️ Pehle wali tagging chal rahi hai!")

    text = message.text or ""
    custom = re.sub(r"^(/admin|@admin)\s*", "", text).strip() or None

    admins = await get_admin_members(client, message.chat.id)
    if not admins:
        return await message.reply("❌ Admins nahi mile.")

    await message.reply(f"👮 **Admins ko tag kar raha hoon!** Total: `{len(admins)}`")
    asyncio.create_task(
        tag_users(client, message, admins, custom_text=custom, prefix="👮")
    )
