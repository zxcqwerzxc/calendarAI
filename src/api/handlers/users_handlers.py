from fastapi import APIRouter, Depends,HTTPException,Query, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.handlers.tasks_handlers import task_router
from src.api.schemas.common_schemas import MessageResponse
from src.api.schemas.users_schemas import CreateUsers, UpdateUsers
from src.db.postgres.session import get_db
from src.services.security import verify_password
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

@user_router.get('/{user_id}', summary= "Получить пользователя")
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



@user_router.get("/user/auth",
    summary="Простая аутентификация пользователя (login + password)",)
async def get_user_auth(
        login: str = Query(..., description="Логин пользователя"),
        password: str = Query(..., description="Пароль пользователя"),
        service: UsersService = Depends(),
        db: AsyncSession = Depends(get_db)
):
    user = await service.authenticate(db, login,password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Пользователь с таким логином не найден"
        )

    if not verify_password(password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверный пароль"
        )

    return {
        "status": "ok",
        "message": "Аутентификация успешна",
        "user_id": user.id,
        "login": user.login
    }
