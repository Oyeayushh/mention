import asyncio
from pyrogram import Client
from pyrogram.enums import ChatMemberStatus, ChatMembersFilter
from config import Config
from AIMentionBot import state


async def is_admin(client: Client, chat_id: int, user_id: int) -> bool:
    try:
        member = await client.get_chat_member(chat_id, user_id)
        return member.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER,
        )
    except Exception:
        return False


async def get_all_members(client: Client, chat_id: int) -> list:
    members = []
    try:
        async for member in client.get_chat_members(chat_id):
            if not member.user.is_bot and not member.user.is_deleted:
                members.append(member.user)
    except Exception:
        pass
    return members


async def get_admin_members(client: Client, chat_id: int) -> list:
    admins = []
    try:
        async for member in client.get_chat_members(
            chat_id, filter=ChatMembersFilter.ADMINISTRATORS
        ):
            if not member.user.is_bot:
                admins.append(member.user)
    except Exception:
        pass
    return admins


async def tag_users(
    client: Client,
    message,
    users: list,
    custom_text: str = None,
    prefix: str = "👋",
):
    chat_id = message.chat.id
    batch = Config.BATCH_SIZE
    state.set_state(chat_id, "running")

    for i in range(0, len(users), batch):
        # Pause check
        while state.is_paused(chat_id):
            await asyncio.sleep(1)

        if not state.is_running(chat_id):
            break

        chunk = users[i: i + batch]
        mentions = " ".join(
            f"[{u.first_name}](tg://user?id={u.id})" for u in chunk
        )

        # Text build karo — prefix aur custom_text dono optional
        parts = []
        if prefix:
            parts.append(prefix)
        if custom_text:
            parts.append(custom_text)
        parts.append(mentions)
        text = "\n\n".join(parts)

        try:
            await message.reply(text, disable_web_page_preview=True)
        except Exception:
            pass

        await asyncio.sleep(1.5)

    state.clear_state(chat_id)
