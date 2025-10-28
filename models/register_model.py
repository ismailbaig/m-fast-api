from pydantic import BaseModel, EmailStr


class RegisterModel(BaseModel):

    firstName: str
    lastName: str
    userName: str
    email: str
    pd: str
    cpd: str
    mobile: str
    role: str
    
class LoginModel(BaseModel):
    email: EmailStr
    pd: str