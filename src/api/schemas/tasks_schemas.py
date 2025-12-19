from datetime import datetime
from typing import Optional, List

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


class GetTask(BaseModel):
    id: int
    description: Optional[str] = None
    status: Optional[bool] = None
    title: Optional[str] = None
    due_date: Optional[datetime] = None
    created_at: Optional[datetime] = None
    priority: Optional[int] = None

class GetShortedTask(BaseModel):
    title: Optional[str] = None
    priority: Optional[int] = None
    created_at: Optional[datetime] = None
    task_date: Optional[datetime] = None



class GetTasks(BaseModel):
    tasks: Optional[List[GetShortedTask]] = None


