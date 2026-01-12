
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.schemas.common_schemas import MessageResponse
from src.api.schemas.params_schemas import CreateParams
from src.db.postgres.session import get_db
from src.services.params_services import ParamsService

params_router= APIRouter()

@params_router.post('', summary="Создать описание")
async def create_params(
        body:CreateParams,
        service: ParamsService = Depends(),
        db: AsyncSession = Depends(get_db)
):
    await service.upsert_params(body,db)
    return MessageResponse(message="Параметр успешно создан")

@params_router.get('/{params_id}', summary="Получить параметр")
async def get_task(
        user_id: int,
        service: ParamsService = Depends(),
        db: AsyncSession = Depends(get_db)
):
    result = await service.get_params(user_id, db)
    return result