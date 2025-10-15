from motor.motor_asyncio import AsyncIOMotorClient
from utility.utility import serialize_doc
from models.register_model import RegisterModel



client = AsyncIOMotorClient("mongodb://localhost:27017")
db = client["mschooldb"]
collection = db["registerdetails"]

async def insert_register_user(registeredUserDetails: RegisterModel):
    user = await collection.find_one({"email": registeredUserDetails.email})
    if user:
        return {
            "already": True,
            "inserted": False
        }
    result =  await collection.insert_one(registeredUserDetails.dict())
    return  {
                "already": False,
                "inserted": True
            }



