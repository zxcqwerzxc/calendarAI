from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.postgres.models.users import Users


class UsersRepository:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def create_users(self, data):
        new_user = Users(
            login=data.login,
            password=data.password
        )
        self._session.add(new_user)
        await self._session.commit()
        await self._session.refresh(new_user)
        return new_user

    async def update_users(self, data):
        stmt = select(Users).where(Users.id == data.id)
        result = await self._session.execute(stmt)
        user = result.scalars().first()

        if user:
            if data.login is not None:
                user.login = data.login
            if data.password is not None:
                user.password = data.password

            await self._session.commit()
            await self._session.refresh(user)

async def delete_users(self, user_id):
        query = (
            delete(Users)
            .where(Users.id == user_id)
        )
        await self._session.execute(query)
        await self._session.commit()
