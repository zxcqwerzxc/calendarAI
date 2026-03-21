from datetime import datetime, date
from typing import Optional, Dict, List

from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.schemas.common_schemas import MessageResponse
from src.api.schemas.tasks_schemas import CreateTasks, UpdateTasks, GetTasks
from src.db.postgres.session import get_db
from src.services.tasks_services import TasksService
from src.api.schemas.tasks_schemas import TaskOut

task_router = APIRouter()


@task_router.post('', summary='Создать задачу')
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


@task_router.get('', summary="Получить задание на промежуток", response_model=GetTasks)
async def get_tasks(
        user_id: int,
        date_from: Optional[datetime] = None,
        date_to: Optional[datetime] = None,
        service: TasksService = Depends(),
        db: AsyncSession = Depends(get_db)
):
    result = await service.get_tasks(db, date_from, date_to, user_id)
    return result

@task_router.get('/search/', summary="Поиск задач по названию")
async def search_tasks(
        user_id: int,
        query: str = Query(..., min_length=1, description="Поисковый запрос"),
        limit: int = Query(10, ge=1, le=100, description="Количество результатов"),
        service: TasksService = Depends(),
        db: AsyncSession = Depends(get_db)
):

    result = await service.search_tasks_by_title(db, user_id, query, limit)
    return result

