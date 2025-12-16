from pydantic import BaseModel, Field, ConfigDict

class MessageResponse(BaseModel):
    message: str = Field(description='Ответ на запрос 200', example="ALL GOOD :)")