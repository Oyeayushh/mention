from pyrogram import Client, filters
from pyrogram.types import Message
from AIMentionBot.helpers import is_admin
from AIMentionBot import state


@Client.on_message(filters.command("stop") & filters.group)
async def stop_cmd(client: Client, message: Message):
    if not await is_admin(client, message.chat.id, message.from_user.id):
        return await message.reply("❌ Sirf admins ye command use kar sakte hain!")

    if not state.is_running(message.chat.id) and not state.is_paused(message.chat.id):
        return await message.reply("ℹ️ Koi tagging chal nahi rahi.")

    state.set_state(message.chat.id, "stopped")
    state.clear_state(message.chat.id)
    await message.reply("⛔ **Tagging stop kar di gayi!**")


@Client.on_message(filters.command("pause") & filters.group)
async def pause_cmd(client: Client, message: Message):
    if not await is_admin(client, message.chat.id, message.from_user.id):
        return await message.reply("❌ Sirf admins ye command use kar sakte hain!")

    if not state.is_running(message.chat.id):
        return await message.reply("ℹ️ Koi tagging chal nahi rahi pause karne ke liye.")

    state.set_state(message.chat.id, "paused")
    await message.reply("⏸ **Tagging pause kar di gayi!** Resume ke liye `/resume` karo.")


@Client.on_message(filters.command("resume") & filters.group)
async def resume_cmd(client: Client, message: Message):
    if not await is_admin(client, message.chat.id, message.from_user.id):
        return await message.reply("❌ Sirf admins ye command use kar sakte hain!")

    if not state.is_paused(message.chat.id):
        return await message.reply("ℹ️ Tagging pause nahi hai.")

    state.set_state(message.chat.id, "running")
    await message.reply("▶️ **Tagging resume kar di gayi!**")
