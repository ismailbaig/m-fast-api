from motor.motor_asyncio import AsyncIOMotorClient
from utility.utility import serialize_doc
from models.register_model import RegisterModel
from fastapi.encoders import jsonable_encoder




client = AsyncIOMotorClient("mongodb://localhost:27017")
db = client["mschooldb"]
collection = db["registerdetails"]

async def insert_register_user(registeredUserDetails: RegisterModel):
    user = await collection.find_one({"email": registeredUserDetails.email})
    if user is not None:
        return str(-1)
    result =  await collection.insert_one(jsonable_encoder(registeredUserDetails))
    return str(result.inserted_id)

async def get_login_user (user_id: int):
    user = await collection.find_one({"uniqueId": user_id})
    if not user:
        return {"error": "User not found"}
    return serialize_doc(user)

async def check_login_user_name (email: str):
    user = await collection.find_one({"email": email})
    if not user:
        return None
    return serialize_doc(user)

async def check_login_user_pd (pd: str):
    user = await collection.find_one({"pd": pd})
    if not user:
        return None
    return serialize_doc(user)


