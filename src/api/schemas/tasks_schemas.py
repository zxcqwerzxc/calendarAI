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
    task_time: Optional[datetime] = None
    task_date: Optional[date] = None



class GetTasks(BaseModel):
    tasks: Optional[List[GetShortedTask]] = None


from pydantic import BaseModel, Field
from typing import Optional, Literal
from datetime import date, time

class TaskOut(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    priority: Literal[1, 2, 3]
    due_date: Optional[date] = None      # если у вас есть отдельно дата
    due_time: Optional[str] = None        # строка "14:30" или None
    status: Optional[bool] = None         # завершена / нет

    class Config:
        from_attributes = True

