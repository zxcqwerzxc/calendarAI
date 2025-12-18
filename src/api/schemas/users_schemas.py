from pydantic import BaseModel
from typing import Optional

class CreateUsers(BaseModel):
    login: str
    password: int

class UpdateUsers(BaseModel):
    id: int
    login: Optional[str]= None
    password: Optional[int] =None



