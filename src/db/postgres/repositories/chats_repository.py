from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.postgres.models.messages import Messages
from src.db.postgres.models.users import Users


class MessagesRepository:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def delete_chat_history(self, user_id: int) -> dict:
        stmt = select(Users).where(Users.id == user_id)
        result = await self._session.execute(stmt)
        user_exists = result.scalar_one_or_none()

        if not user_exists:
            raise ValueError(f"Пользователь с ID {user_id} не найден")

        stmt = delete(Messages).where(Messages.session_id == user_id)
        result = await self._session.execute(stmt)
        deleted_count = result.rowcount

        await self._session.commit()

        return {
            "status": "success",
            "deleted_count": deleted_count
        }