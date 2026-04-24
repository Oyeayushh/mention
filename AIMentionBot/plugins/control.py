from pyrogram import Client, filters
from pyrogram.types import Message
from AIMentionBot.helpers import is_admin
from AIMentionBot import state


@Client.on_message(filters.command("stop") & filters.group)
async def stop_cmd(client: Client, message: Message):
    if not await is_admin(client, message.chat.id, message.from_user.id):
        return await message.reply("❌ **ᴀᴅᴍɪɴꜱ ᴏɴʟʏ!**")

    if not state.is_running(message.chat.id) and not state.is_paused(message.chat.id):
        return await message.reply("ℹ️ **ɴᴏ ᴛᴀɢɢɪɴɢ ɪꜱ ʀᴜɴɴɪɴɢ.**")

    state.set_state(message.chat.id, "stopped")
    state.clear_state(message.chat.id)
    await message.reply("⛔ **ᴛᴀɢɢɪɴɢ ꜱᴛᴏᴘᴘᴇᴅ!**")


@Client.on_message(filters.command("pause") & filters.group)
async def pause_cmd(client: Client, message: Message):
    if not await is_admin(client, message.chat.id, message.from_user.id):
        return await message.reply("❌ **ᴀᴅᴍɪɴꜱ ᴏɴʟʏ!**")

    if not state.is_running(message.chat.id):
        return await message.reply("ℹ️ **ɴᴏᴛʜɪɴɢ ᴛᴏ ᴘᴀᴜꜱᴇ.**")

    state.set_state(message.chat.id, "paused")
    await message.reply("⏸ **ᴛᴀɢɢɪɴɢ ᴘᴀᴜꜱᴇᴅ!** ᴜꜱᴇ `/resume` ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ.")


@Client.on_message(filters.command("resume") & filters.group)
async def resume_cmd(client: Client, message: Message):
    if not await is_admin(client, message.chat.id, message.from_user.id):
        return await message.reply("❌ **ᴀᴅᴍɪɴꜱ ᴏɴʟʏ!**")

    if not state.is_paused(message.chat.id):
        return await message.reply("ℹ️ **ᴛᴀɢɢɪɴɢ ɪꜱ ɴᴏᴛ ᴘᴀᴜꜱᴇᴅ.**")

    state.set_state(message.chat.id, "running")
    await message.reply("▶️ **ᴛᴀɢɢɪɴɢ ʀᴇꜱᴜᴍᴇᴅ!**")
