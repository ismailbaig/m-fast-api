from pydantic import BaseModel


class RegisterModel(BaseModel):

    firstName: str
    lastName: str
    email: str
    pd: str
    cpd: str
    mobile: str
    uniqueId: int