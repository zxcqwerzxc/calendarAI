from typing import Dict

import psycopg
from fastapi import APIRouter, Depends, HTTPException
from langchain_postgres import PostgresChatMessageHistory
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from src.api.schemas.chats_schemas import GenerateMessage, MessageItem, ChatHistoryResponse
from src.config import POSTGRES_URL
from src.db.postgres.session import get_db
from src.services.chats_service import ChatsService

chat_router = APIRouter()


@chat_router.delete(
    "/history/{user_id}",
    summary="Удалить всю историю чата пользователя"
)
async def delete_user_chat_history(
        user_id: int,
        service: ChatsService = Depends(),
        db: AsyncSession = Depends(get_db)

):
    try:
        result = await service.delete_chat_history(user_id, db)
        return result

    except ValueError as e:
        raise HTTPException(
            status_code=
            status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Ошибка при удалении истории: {str(e)}"
        )

@chat_router.post('/generate', summary="Сгенерировать  сообщение", response_model=str)
async def create_params(
        body: GenerateMessage,
        service: ChatsService = Depends()
):
    response = await service.generate_message(body)
    return response

@chat_router.get("/messages", summary="Получить историю чата", response_model=ChatHistoryResponse)
async def get_chat_history(
    user_id: int,
    service: ChatsService = Depends()
):
    messages = await service.get_chat_messages(user_id)
    return ChatHistoryResponse(messages=messages)
