"""
from pydantic import BaseModel


class RegisterModel(BaseModel):

    firstName: str
    lastName: str
    email: str
    pd: str
    cpd: str
    mobile: str
    uniqueId: int
"""
from pydantic import BaseModel
from typing import Optional

class RegisterModel(BaseModel):
    name: str
    email: str  # Changed to regular string
    password: str
    phone: Optional[str] = None