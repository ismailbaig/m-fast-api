from pydantic import BaseModel

class UserResponse(BaseModel):
    """
    Schema for user information in the token response.
    """
    user_id: str
    username: str
    email: str

    class Config:
        json_schema_extra = {
            "example": {
                "user_id": "123e4567-e89b-12d3-a456-426614174000",
                "username": "john_doe",
                "email": "john@example.com"
            }
        }

class TokenResponse(BaseModel):
    """
    Schema for the token response after successful authentication.
    """
    message: str
    user: UserResponse
    token: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "message": "Login successful",
                "user": {
                    "user_id": "123e4567-e89b-12d3-a456-426614174000",
                    "username": "john_doe",
                    "email": "john@example.com"
                },
                "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
            }
        }