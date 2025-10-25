from pydantic import BaseModel, Field


class UserLogin(BaseModel):
    userName: str = Field(..., description="The userName or email of the user")
    pd: str = Field(..., description="The password of the user")

    class Config:
        json_schema_extra = {
            "example": {
                "userName": "john_doe",
                "pd": "strongpassword123"
            }
        }

class UserResponse(BaseModel):
    """ Schema for user response """
    user_id: str
    userName: str
    email: str

    class Config:
        json_schema_extra = {
            "example": {
                "user_id": "609c5f2e8f1b2c0015b8e4d1",
                "userName": "john_doe",
                "email": "john_doe@gmail.com"
            }
        }