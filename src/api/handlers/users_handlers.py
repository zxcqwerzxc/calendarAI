from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.handlers.tasks_handlers import task_router
from src.api.schemas.common_schemas import MessageResponse
from src.api.schemas.users_schemas import CreateUsers, UpdateUsers
from src.db.postgres.session import get_db
from src.services.tasks_services import TasksService
from src.services.users_services import UsersService


user_router = APIRouter()


@user_router.post('/', summary="Создать пользователя")
async def create_users(
        body: CreateUsers,
        service: UsersService = Depends(),
        db: AsyncSession = Depends(get_db)
):
    await service.create_users(body, db)
    return MessageResponse(message="Пользователь успешно создан")


@user_router.put('/{user_id}', summary="Обновить пользователя")
async def upgrade_users(
        body: UpdateUsers,
        service: UsersService = Depends(),
        db: AsyncSession = Depends(get_db)
):
    await service.update_users(body, db)
    return MessageResponse(message="Пользователь успешно обновлен")

@task_router.get('/{user_id}', summary= "Получить пользователя")
async def get_users(
        user_id: int,
        service: UsersService = Depends(),
        db: AsyncSession = Depends(get_db)
):
    return await service.get_user(user_id,db)

@user_router.delete('/{user_id}', summary="Удалить пользователя")
async def delete_users(
        user_id: int,
        service: UsersService = Depends(),
        db: AsyncSession = Depends(get_db)
):
    await service.delete_users(user_id, db)
    return MessageResponse(message='Пользователь успешно удалено')

@user_router.get('/{user_id}', summary="Получить пользователя")
async def get_task(
        user_id: int,
        service: UsersService = Depends(),
        db: AsyncSession = Depends(get_db)
):
    return await service.get_user(user_id,db)
