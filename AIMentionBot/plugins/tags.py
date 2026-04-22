import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from AIMentionBot.helpers import get_all_members, get_admin_members, tag_users, is_admin
from AIMentionBot import state

# ─── Jokes list ───────────────────────────────────────────────
JOKES = [
    "Teacher: Kal school aana. Student: Kyun? Teacher: Kal exam hai. Student: To kya hua, main toh waise bhi nahi aata 😂",
    "Ek aadmi dukaan mein gaya: Bhai ek kilo santra dena. Dukandaar: Santre nahi hain. Aadmi: Koi baat nahi, apple dena. Dukandaar: Apple bhi nahi. Aadmi: Acha kela dena. Dukandaar: KUCH BHI NAHI HAI! Aadmi: To phir khali dukaan kyun kholi? 😆",
    "Wife: Suno ji, aaj bahut boring din tha. Husband: Haan, main bhi ghar pe hi tha 🥲",
    "Padhai karo bolte hain, padhai karo bolte hain... baat kya hai? 😂",
    "Result aaya, papa ne pucha number kitne aaye? Maine bola 'teen' — unhone socha 300, main bol raha tha 3 subjects pass hue 😅",
]

_joke_index = {}

def next_joke(chat_id):
    idx = _joke_index.get(chat_id, 0)
    joke = JOKES[idx % len(JOKES)]
    _joke_index[chat_id] = idx + 1
    return joke


# ─── /tagall ──────────────────────────────────────────────────
@Client.on_message(filters.command("tagall") & filters.group)
async def tagall(client: Client, message: Message):
    if state.is_running(message.chat.id):
        return await message.reply("⚠️ Pehle wali tagging chal rahi hai! `/stop` karo pehle.")
    members = await get_all_members(client, message.chat.id)
    if not members:
        return await message.reply("❌ Members nahi mile.")
    await message.reply(f"🔥 **Tagall shuru!** Total: `{len(members)}`")
    asyncio.create_task(tag_users(client, message, members, prefix="🔥 Sabko bulaya ja raha hai!"))


# ─── /hitag ───────────────────────────────────────────────────
@Client.on_message(filters.command("hitag") & filters.group)
async def hitag(client: Client, message: Message):
    if state.is_running(message.chat.id):
        return await message.reply("⚠️ Pehle wali tagging chal rahi hai!")
    members = await get_all_members(client, message.chat.id)
    if not members:
        return await message.reply("❌ Members nahi mile.")
    await message.reply(f"🇮🇳 **Hindi Tag shuru!** Total: `{len(members)}`")
    asyncio.create_task(tag_users(client, message, members, prefix="🇮🇳 Yaar log! Idhar aao, kuch zaroori baat karni hai!"))


# ─── /entag ───────────────────────────────────────────────────
@Client.on_message(filters.command("entag") & filters.group)
async def entag(client: Client, message: Message):
    if state.is_running(message.chat.id):
        return await message.reply("⚠️ Pehle wali tagging chal rahi hai!")
    members = await get_all_members(client, message.chat.id)
    if not members:
        return await message.reply("❌ Members nahi mile.")
    await message.reply(f"🇬🇧 **English Tag shuru!** Total: `{len(members)}`")
    asyncio.create_task(tag_users(client, message, members, prefix="🇬🇧 Hey everyone! Come on over, something important!"))


# ─── /gmtag ───────────────────────────────────────────────────
@Client.on_message(filters.command("gmtag") & filters.group)
async def gmtag(client: Client, message: Message):
    if state.is_running(message.chat.id):
        return await message.reply("⚠️ Pehle wali tagging chal rahi hai!")
    members = await get_all_members(client, message.chat.id)
    if not members:
        return await message.reply("❌ Members nahi mile.")
    await message.reply(f"☀️ **Good Morning Tag shuru!** Total: `{len(members)}`")
    asyncio.create_task(tag_users(client, message, members, prefix="☀️ Good Morning dosto! Uthho, naya din shuru ho gaya!"))


# ─── /gntag ───────────────────────────────────────────────────
@Client.on_message(filters.command("gntag") & filters.group)
async def gntag(client: Client, message: Message):
    if state.is_running(message.chat.id):
        return await message.reply("⚠️ Pehle wali tagging chal rahi hai!")
    members = await get_all_members(client, message.chat.id)
    if not members:
        return await message.reply("❌ Members nahi mile.")
    await message.reply(f"🌙 **Good Night Tag shuru!** Total: `{len(members)}`")
    asyncio.create_task(tag_users(client, message, members, prefix="🌙 Good Night dosto! So jao, kal phir milenge!"))


# ─── /jtag ────────────────────────────────────────────────────
@Client.on_message(filters.command("jtag") & filters.group)
async def jtag(client: Client, message: Message):
    if state.is_running(message.chat.id):
        return await message.reply("⚠️ Pehle wali tagging chal rahi hai!")
    members = await get_all_members(client, message.chat.id)
    if not members:
        return await message.reply("❌ Members nahi mile.")
    joke = next_joke(message.chat.id)
    await message.reply(f"😂 **Joke Tag shuru!** Total: `{len(members)}`")
    asyncio.create_task(tag_users(client, message, members, custom_text=f"😂 {joke}", prefix=""))


# ─── /vctag ───────────────────────────────────────────────────
@Client.on_message(filters.command("vctag") & filters.group)
async def vctag(client: Client, message: Message):
    if state.is_running(message.chat.id):
        return await message.reply("⚠️ Pehle wali tagging chal rahi hai!")
    members = await get_all_members(client, message.chat.id)
    if not members:
        return await message.reply("❌ Members nahi mile.")
    await message.reply(f"🎙️ **VC Invite Tag shuru!** Total: `{len(members)}`")
    asyncio.create_task(tag_users(client, message, members, prefix="🎙️ Bhai VC join karo! Sab aa jao!"))
