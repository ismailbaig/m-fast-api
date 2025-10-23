from bson import ObjectId
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
from db_mongo.get_data import get_single_student_info, get_all_student_details
from db_mongo.register_and_login import check_login_user_name, check_login_user_pd, insert_register_user
from models.register_model import RegisterModel
# from db_mongo.insert_data import insert_studentdetails, user_json
from login.login import get_current_user
from models.schemas import UserLogin, UserResponse
from models.tokenResponse import TokenResponse
from login import jwt_auth

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

# Then define your endpoints
@app.get("/")
async def base_endpoint():
    return {"msg": "Hello from FastAPI!"}

@app.get("/getallstudents")
async def get_all_students_info():
    all_student_details = await get_all_student_details()
    return all_student_details

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    single_student_info = await get_single_student_info(user_id)
    if "error" in single_student_info:
        raise HTTPException(status_code=404, detail=single_student_info["error"])
    return single_student_info

@app.get("/add/student")
async def add_student():
   # inserted_id = await insert_studentdetails(user_json)
    return {"message": "User inserted successfully", "id":14}

@app.post("/reg/user")
async def register_user(registeruser: RegisterModel):
    inserted_id = await insert_register_user(registeruser)
    if inserted_id == -1:
        return {"error": "User Already existes. Check again !!!", "id": inserted_id}
    return {"message": "Registerd User inserted successfully", "id": inserted_id}


# Login user
@app.post("/api/login", response_model=TokenResponse, tags=["Authentication"])
async def login_user(credentials: UserLogin):
    """
    Login with username and password to receive an authentication token.

    - **username/email**: The username/email of the user.
    - **password**: The password of the user.

    Returns a JWT token upon successful authentication.

    """
    user = await check_login_user_name(credentials.username)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Invalid credentials"
        )
    
    user = await check_login_user_pd(credentials.password)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Invalid credentials"
        )

    token = jwt_auth.generate_token(user_id=user.user_id, username=user.username)

    return TokenResponse(
        message="Login successful",
        user=UserResponse(
            user_id=user.user_id,
            username=user.username,
            email=user.email
        ),
        access_token=token, token_type="bearer"
        )


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

