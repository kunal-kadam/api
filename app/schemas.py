from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

from pydantic.types import conint

class UserOut(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True

class UserCreate(BaseModel):

    first_name: str
    last_name: str
    has_vehicle: int
    is_driver: bool
    phone_number: int
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str

