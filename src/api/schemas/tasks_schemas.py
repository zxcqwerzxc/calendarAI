from datetime import datetime
from typing import Optional

from pydantic import BaseModel

class CreateTasks(BaseModel):
    description: Optional[str] = None
    status: Optional[bool] = None
    title:  Optional[str]= None
    due_date: Optional[datetime]=None
    created_at: Optional[datetime]= None
    priority: Optional[int]= None

class UpdateTasks(BaseModel):
    description: Optional[str]= None
    status: Optional[bool]= None
    title:  Optional[str] = None
    due_date: Optional[datetime] = None
    priority: Optional[int] = None






