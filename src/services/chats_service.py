import uuid

import asyncpg
import psycopg
import psycopg2
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from langchain_postgres import PostgresChatMessageHistory

from src.config import OPENAI_API_BASE, OPENROUTER_LLM_MODEL, OPENAI_API_KEY, POSTGRES_URL


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

        messages = chat_history.messages

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
