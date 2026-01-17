import psycopg
from fastapi import APIRouter, Depends
from langchain_postgres import PostgresChatMessageHistory
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.schemas.chats_schemas import GenerateMessage, MessageItem, ChatHistoryResponse
from src.config import POSTGRES_URL
from src.db.postgres.session import get_db
from src.services.chats_service import ChatsService

chat_router = APIRouter()

#todo: сделать эндпоинт на удлаение истории чата (с помощью sqlalchemy)

@chat_router.post('/generate', summary="Сгенерировать  сообщение", response_model=str)
async def create_params(
        body: GenerateMessage,
        service: ChatsService = Depends()
):
    response = await service.generate_message(body)
    return response

@chat_router.post('/messages', summary="Получить сообщения", response_model=ChatHistoryResponse)
async def create_params(
        user_id: int,
        service: ChatsService = Depends()
):
    #todo: переместить в сервис
    conn_info = POSTGRES_URL.replace("+asyncpg", "")
    sync_connection = psycopg.connect(conn_info)
    table_name = "messages"

    chat_history = PostgresChatMessageHistory(
        table_name,
        str(user_id),
        sync_connection=sync_connection
    )

    messages = chat_history.get_messages()
    sync_connection.close()

    formatted_messages = []
    for msg in messages:
        role = "user" if msg.type == "human" else "ai"
        formatted_messages.append(MessageItem(role=role, content=msg.content))

    return ChatHistoryResponse(messages=formatted_messages)


