import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from config import Config
from AIMentionBot.database import db

owner_filter = filters.user(Config.OWNER_ID) & filters.private


@Client.on_message(filters.command("stats") & owner_filter)
async def stats(client: Client, message: Message):
    users = await db.total_users()
    groups = await db.total_groups()
    await message.reply(
        f"**📊 Bot Statistics**\n\n"
        f"👤 **Total Users:** `{users}`\n"
        f"👥 **Total Groups:** `{groups}`\n"
    )


@Client.on_message(filters.command("broadcast") & owner_filter)
async def broadcast(client: Client, message: Message):
    if len(message.command) < 2:
        return await message.reply("Usage: `/broadcast <message>`")

    text = message.text.split(None, 1)[1]
    status_msg = await message.reply("📡 **Broadcasting shuru hua...**")

    sent = 0
    failed = 0

    # Users ko broadcast
    async for user_doc in db.get_all_users():
        try:
            await client.send_message(user_doc["user_id"], text)
            sent += 1
        except Exception:
            failed += 1
        await asyncio.sleep(0.05)

    # Groups ko broadcast
    async for group_doc in db.get_all_groups():
        try:
            await client.send_message(group_doc["chat_id"], text)
            sent += 1
        except Exception:
            failed += 1
        await asyncio.sleep(0.05)

    await status_msg.edit(
        f"✅ **Broadcast Complete!**\n\n"
        f"✔️ Sent: `{sent}`\n"
        f"❌ Failed: `{failed}`"
    )
