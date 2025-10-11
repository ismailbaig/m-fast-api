from motor.motor_asyncio import AsyncIOMotorClient
from utility.utility import serialize_doc

# MongoDB connection
client = AsyncIOMotorClient("mongodb://localhost:27017")
db = client["mschooldb"]
collection = db["studentdetails"]


async def get_all_student_details():
    users_cursor = collection.find()
    users = await users_cursor.to_list(length=100)
    return [serialize_doc(user) for user in users]

async def get_single_student_info (user_id: int):
    user = await collection.find_one({"user_id": user_id})
    if not user:
        return {"error": "User not found"}
    return serialize_doc(user)
