import asyncio
from pyrogram import idle
from AIMentionBot import app
from AIMentionBot.database import db

async def main():
    await db.connect()
    await app.start()
    print("✅ AI Mention Bot Started!")
    await idle()
    await app.stop()

if __name__ == "__main__":
    asyncio.run(main())
