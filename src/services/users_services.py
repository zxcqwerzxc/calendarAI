from sqlalchemy.ext.asyncio import AsyncSession

from src.api.schemas.users_schemas import CreateUsers, UpdateUsers, GetUser
from src.db.postgres.repositories.users_repository import UsersRepository


class UsersService:
    async def create_users(self,data:CreateUsers,db_session: AsyncSession):
        user_repository= UsersRepository(db_session)
        user = await user_repository.create_users(data)
        return user

    async def update_users(self, data:UpdateUsers, db_session: AsyncSession):
        user_repository= UsersRepository(db_session)
        user = await user_repository.update_users(data)
        return user

    async def delete_users(self,  user_id, db_session:AsyncSession):
        user_repository = UsersRepository(db_session)
        task = await user_repository.delete_users(user_id)

    async def get_user(self, user_id, db_session:AsyncSession):
        user_repository = UsersRepository(db_session)
        user_data = await user_repository.get_user(user_id)

        return GetUser(
            id=user_data.id,
            login=user_data.login,
            password=user_data.password
        )


