from datetime import datetime, time,date
from typing import Optional, List

from pydantic import BaseModel

class CreateTasks(BaseModel):
    description: Optional[str] = None
    status: Optional[bool] = None
    title:  Optional[str]= None
    due_time: Optional[time]=None
    task_date: Optional[date] = None
    created_at: Optional[datetime]= None
    priority: Optional[int]= None
    user_id: Optional[int]= None

class UpdateTasks(BaseModel):
    description: Optional[str]= None
    status: Optional[bool]= None
    title:  Optional[str] = None
    due_time: Optional[time] = None
    priority: Optional[int] = None


class GetTask(BaseModel):
    id: int
    description: Optional[str] = None
    status: Optional[bool] = None
    title: Optional[str] = None
    due_time: Optional[time] = None
    created_at: Optional[datetime] = None
    priority: Optional[int] = None

class GetShortedTask(BaseModel):
    id: int
    title: Optional[str] = None
    priority: Optional[int] = None
    created_at: Optional[datetime] = None
    task_date: Optional[date] = None



class GetTasks(BaseModel):
    tasks: Optional[List[GetShortedTask]] = None


