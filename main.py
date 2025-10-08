from bson import ObjectId
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient


app = FastAPI()



# If you want to allow *all* origins (i.e. fully global)
origins = ["*"]

# Or better: specify the allowed origins
# origins = [
#     "http://localhost:3000",
#     "https://myfrontenddomain.com",
#     # etc.
# ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,    # if you use cookies, or Authorization headers
    allow_methods=["*"],        # GET, POST, etc.
    allow_headers=["*"],        # which headers the client can send
    # optionally: expose_headers, allow_origin_regex, max_age, etc.
)


# MongoDB connection
client = AsyncIOMotorClient("mongodb://localhost:27017")
db = client.mschooldb
collection = db.studentdetails

def serialize_doc(doc):
    doc["_id"] = str(doc["_id"])
    return doc

# Then define your endpoints
@app.get("/")
async def some_endpoint():
    return {"msg": "Hello from FastAPI!"}

@app.get("/getuserdetails")
async def get_user_details():
    users_cursor = collection.find()
    users = await users_cursor.to_list(length=100)
    return [serialize_doc(user) for user in users]

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    user = await collection.find_one({"user_id": user_id})
    if not user:
        return {"error": "User not found"}
    return serialize_doc(user)


# @app.get("/users/update/{user_id}")
# async def update_user(user_id: int):
#     """Update an existing user (replace fields given)."""
#     #  update_data = {k: v for k, v in user_data.dict().items() if v is not None}
#     result = await collection.update_one({"user_id": user_id}, 
#                                          {"$set": {"name": "Shaik Sameer 1"}})

#     if result.matched_count == 0:
#         raise HTTPException(status_code=404, detail="User not found")

#     updated_user = await collection.find_one({"user_id": user_id})
#     return serialize_doc(updated_user)

