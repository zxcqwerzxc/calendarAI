from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from src.api.schemas.users_schemas import CreateUsers, UpdateUsers, GetUser
from src.db.postgres.models.users import Users
from src.db.postgres.repositories.users_repository import UsersRepository
from src.services.security import get_password_hash, verify_password


class UsersService:
    async def create_users(self, data: CreateUsers, db_session: AsyncSession):
        user_repository = UsersRepository(db_session)
        hashed_password = get_password_hash(data.password)
        user_data = {
            "login": data.login,
            "password": hashed_password
        }
        user = await user_repository.create_users(user_data)
        return user

    async def update_users(self, data: UpdateUsers, db_session: AsyncSession):
        user_repository = UsersRepository(db_session)
        if data.password:
            data.password = get_password_hash(data.password)

        else:

            data_dict = data.dict(exclude_unset=True, exclude_none=True)
            data_dict.pop('password', None)
        user = await user_repository.update_users(data)
        return user

    async def delete_users(self, user_id, db_session: AsyncSession):
        user_repository = UsersRepository(db_session)
        task = await user_repository.delete_users(user_id)

    async def get_user(self, user_id, db_session: AsyncSession):
        user_repository = UsersRepository(db_session)
        user_data = await user_repository.get_user(user_id)

        return GetUser(
            id=user_data.id,
            login=user_data.login,
            password=user_data.password
        )

    async def get_by_login(self, db: AsyncSession, login: str) -> Optional[Users]:
        stmt = select(Users).where(Users.login == login)
        result = await db.execute(stmt)
        return result.scalar_one_or_none()

    async def authenticate(self, db: AsyncSession, login: str, password: str) -> Optional[Users]:
        user = await self.get_by_login(db, login)
        if not user:
            return None
        if not verify_password(password, user.password):
            return None
        return user
