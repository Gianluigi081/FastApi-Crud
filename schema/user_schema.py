from pydantic import BaseModel
from typing import Optional

class UserSchema(BaseModel):
    id: Optional[str]
    email: str
    password: str

class DataUserSchema(BaseModel):
    email: str
    password: str