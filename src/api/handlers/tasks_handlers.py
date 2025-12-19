from typing import Optional

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.schemas.common_schemas import MessageResponse
from src.api.schemas.tasks_schemas import CreateTasks, UpdateTasks, GetTask, GetTasks
from src.db.postgres.session import get_db
from src.services.tasks_services import TasksService
from datetime import datetime
from typing import Optional, List

task_router = APIRouter()


@task_router.post('/', summary='Создать задачу')
async def create_task(
        body: CreateTasks,
        service: TasksService = Depends(),
        db: AsyncSession = Depends(get_db)
):
    await service.create_tasks(body, db)
    return MessageResponse(message='Задание успешно создано')


@task_router.put('/{task_id}', summary='Обновить задание')
async def get_tasks(
        task_id: int,
        body: UpdateTasks,
        service: TasksService = Depends(),
        db: AsyncSession = Depends(get_db)
):
    await service.update_tasks(task_id, body, db)
    return MessageResponse(message='Задание успешно получено')


@task_router.delete('/{task_id}', summary="Удалить задачу")
async def delete_tasks(
        task_id: int,
        service: TasksService = Depends(),
        db: AsyncSession = Depends(get_db)
):
    await service.delete_task(task_id, db)
    return MessageResponse(message='Задание успешно удалено')


@task_router.get('/{task_id}', summary="Получить задание")
async def get_task(
        task_id: int,
        service: TasksService = Depends(),
        db: AsyncSession = Depends(get_db)
):
   result = await service.get_task(task_id, db)
   return result


@task_router.get('s', summary="Получить задание на промежуток",response_model= GetTasks)
async def get_tasks(
        date_from: Optional[datetime] = None,
        date_to: Optional[datetime] = None,
        service: TasksService = Depends(),
        db: AsyncSession = Depends(get_db)
):
    result = await service.get_tasks(db,date_from,date_to)
    return result
