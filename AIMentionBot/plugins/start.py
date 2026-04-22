from pyrogram import Client, filters
from pyrogram.types import Message
from AIMentionBot.database import db


@Client.on_message(filters.command("start") & filters.private)
async def start(client: Client, message: Message):
    await db.add_user(message.from_user.id)
    await message.reply(
        "**🤖 AI Mention Bot**\n\n"
        "Mujhe apne group mein add karo aur admin bana do!\n\n"
        "**Tag Commands:**\n"
        "`/tagall` — Sabko tag karo 🔥\n"
        "`/all` or `@all` — Sabko tag karo\n"
        "`/admin` or `@admin` — Sirf admins ko tag karo\n"
        "`/hitag` — Hindi mein tag karo 🇮🇳\n"
        "`/entag` — English mein tag karo 🇬🇧\n"
        "`/gmtag` — Good Morning tag ☀️\n"
        "`/gntag` — Good Night tag 🌙\n"
        "`/jtag` — Joke tag karo 😂\n"
        "`/vctag` — VC Invite tag 🎙️\n\n"
        "**Control (Admins):**\n"
        "`/stop` — Tagging band karo\n"
        "`/pause` — Pause karo\n"
        "`/resume` — Resume karo\n\n"
        "**Tips 💡**\n"
        "• Sab commands auto-stop hoti hain complete hone par\n"
        "• `/stop` se kabhi bhi cancel karo\n"
        "• Best performance ke liye mujhe admin banao!\n\n"
        "/help se poori commands dekho",
        disable_web_page_preview=True,
    )


@Client.on_message(filters.command("help"))
async def help_cmd(client: Client, message: Message):
    await message.reply(
        "**📋 AI Mention Bot — Full Commands**\n\n"
        "**🏷️ Tag Commands:**\n"
        "`/hitag` — Tag all members in Hindi 🇮🇳\n"
        "`/entag` — Tag all members in English 🇬🇧\n"
        "`/gmtag` — Good Morning tag ☀️\n"
        "`/gntag` — Good Night tag (Hinglish) 🌙\n"
        "`/tagall` — General tag, all members 🔥\n"
        "`/jtag` — Joke tag, all members 😂\n"
        "`/vctag` — VC Invite tag 🎙️ Online members first!\n\n"
        "**💬 Mention Commands:**\n"
        "`/admin` or `@admin` — Tag only admins (6 per msg)\n"
        "`/all` or `@all` — Tag all members (6 per msg)\n"
        "  _Supports custom messages: `/admin plz join vc`_\n\n"
        "**⏸ Control Commands** _(Admins only)_\n"
        "`/stop` — Stop ongoing tagging\n"
        "`/pause` — Pause tagging temporarily\n"
        "`/resume` — Resume paused tagging\n\n"
        "**👑 Owner Commands:**\n"
        "`/broadcast <msg>` — Broadcast to all users & groups\n"
        "`/stats` — View bot usage statistics\n\n"
        "**💡 Tips:**\n"
        "• All tagging cmds auto-stop when complete\n"
        "• Use `/stop` anytime to cancel tagging\n"
        "• Add me as admin for best performance!",
        disable_web_page_preview=True,
    )


@Client.on_message(filters.group & ~filters.bot)
async def track_group(client: Client, message: Message):
    await db.add_group(message.chat.id)
    if message.from_user:
        await db.add_user(message.from_user.id)
