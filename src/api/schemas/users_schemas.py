from pydantic import BaseModel
from typing import Optional

class CreateUsers(BaseModel):
    login: str
    password: str

class UpdateUsers(BaseModel):
    login: Optional[str]= None
    password: Optional[str] =None


