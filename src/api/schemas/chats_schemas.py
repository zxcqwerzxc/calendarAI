from datetime import datetime
from typing import List

from pydantic import BaseModel


class GenerateMessage(BaseModel):
    message: str
    user_id: int

class MessageItem(BaseModel):
    role: str
    content: str


class ChatHistoryResponse(BaseModel):
    messages: List[MessageItem]