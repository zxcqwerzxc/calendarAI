from pydantic import BaseModel
from typing import Optional

class CreateUsers(BaseModel):
    login: str
    password: str

class UpdateUsers(BaseModel):
    id: int
    login: Optional[str]= None
    password: Optional[str] =None

class GetUser(BaseModel):
    id: int
    login: Optional[str] = None
    password: Optional[str] = None


