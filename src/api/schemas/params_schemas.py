from typing import Optional

from pydantic import BaseModel


class CreateParams(BaseModel):
    description: Optional[str] = None
    user_id: Optional[int] = None


class GetParams(BaseModel):
    id: int
    description: Optional[str] = None
