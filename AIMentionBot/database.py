from motor.motor_asyncio import AsyncIOMotorClient
from config import Config

class Database:
    def __init__(self):
        self.client = None
        self.db = None

    async def connect(self):
        self.client = AsyncIOMotorClient(Config.MONGO_URI)
        self.db = self.client["AIMentionBot"]
        print("✅ MongoDB Connected!")

    # --- Stats ---
    async def add_user(self, user_id: int):
        await self.db.users.update_one(
            {"user_id": user_id},
            {"$set": {"user_id": user_id}},
            upsert=True
        )

    async def add_group(self, chat_id: int):
        await self.db.groups.update_one(
            {"chat_id": chat_id},
            {"$set": {"chat_id": chat_id}},
            upsert=True
        )

    async def total_users(self):
        return await self.db.users.count_documents({})

    async def total_groups(self):
        return await self.db.groups.count_documents({})

    async def get_all_users(self):
        return self.db.users.find({})

    async def get_all_groups(self):
        return self.db.groups.find({})

db = Database()
