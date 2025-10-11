from motor.motor_asyncio import AsyncIOMotorClient

# insert_data.py
# Sample JSON data
user_json = {
    "name": "Ismail Baig",
    "email": "ismail@example.com",
    "age": 29,
    "skills": ["Python", "FastAPI", "MongoDB"]
}

# MongoDB connection
client = AsyncIOMotorClient("mongodb://localhost:27017")
db = client["mschooldb"]
collection = db["studentdetails"]

def serialize_doc(doc):
    doc["_id"] = str(doc["_id"])
    return doc


# Function to insert data
async def insert_studentdetails(user_data: dict):
    result =  123 # await collection.insert_one(user_data)
    return str(result.inserted_id)
