from pydantic import BaseModel, Field


class UserLogin(BaseModel):
    username: str = Field(..., description="The username or email of the user")
    password: str = Field(..., description="The password of the user")

    class Config:
        json_schema_extra = {
            "example": {
                "username": "john_doe",
                "password": "strongpassword123"
            }
        }

class UserResponse(BaseModel):
    """ Schema for user response """
    user_id: str
    username: str
    email: str

    class Config:
        json_schema_extra = {
            "example": {
                "user_id": "609c5f2e8f1b2c0015b8e4d1",
                "username": "john_doe",
                "email": "john_doe@gmail.com"
            }
        }