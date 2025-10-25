from pydantic import BaseModel


class RegisterModel(BaseModel):

    firstName: str
    lastName: str
    userName: str
    email: str
    pd: str
    cpd: str
    mobile: str
    role: str