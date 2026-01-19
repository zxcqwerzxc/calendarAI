import uuid

import asyncpg
import psycopg
import psycopg2
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from langchain_postgres import PostgresChatMessageHistory
from sqlalchemy import delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.testing.pickleable import User

from src.api.schemas.chats_schemas import MessageItem
from src.config import OPENAI_API_BASE, OPENROUTER_LLM_MODEL, OPENAI_API_KEY, POSTGRES_URL
from src.db.postgres.models.messages import Messages
from src.db.postgres.repositories.chats_repository import MessagesRepository


class ChatsService:
    async def generate_message(self, body):
        user_message = body.message

        conn_info = POSTGRES_URL.replace("+asyncpg", "")
        sync_connection = psycopg.connect(conn_info)
        table_name = "messages"

        chat_history = PostgresChatMessageHistory(
            table_name,
            str(body.user_id),
            sync_connection=sync_connection
        )

        messages = chat_history.get_messages()

        prompt = ("ты мой друг собутыльник который живут "
                  "ради водки, придерживайся постоянно этой роли в разговоре со мной"
                  )

        llm = ChatOpenAI(
            model=OPENROUTER_LLM_MODEL,
            openai_api_base=OPENAI_API_BASE,
            openai_api_key=OPENAI_API_KEY
        )

        prompt_template = ChatPromptTemplate.from_messages([
            ("system", prompt),
            MessagesPlaceholder(variable_name="history"),
            ("human", "{input}")
        ])

        chain = prompt_template | llm

        ai_response = chain.invoke({
            "input": user_message,
            "history": messages
        })

        chat_history.add_messages([
            HumanMessage(content=user_message),
            AIMessage(content=ai_response.content),
        ])

        sync_connection.close()

        return ai_response.content

    async def get_chat_messages(self, user_id: int) -> list[MessageItem]:
        conn_info = POSTGRES_URL.replace("+asyncpg", "")
        with psycopg.connect(conn_info) as conn:
            history = PostgresChatMessageHistory(
                "messages",  # table_name — только позиционно
                str(user_id),  # session_id   — только позиционно
                sync_connection=conn
            )

            raw_messages = history.messages

        formatted = [
            MessageItem(
                role="user" if msg.type == "human" else "ai",
                content=msg.content
            )
            for msg in raw_messages
        ]

        return formatted

    async def delete_chat_history(self, user_id, db_session: AsyncSession):
        messages_repository = MessagesRepository(db_session)
        result = await messages_repository.delete_chat_history(user_id)
        return result

