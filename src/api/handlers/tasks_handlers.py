from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.schemas.common_schemas import MessageResponse
from src.api.schemas.tasks_schemas import CreateTasks, UpdateTasks
from src.db.postgres.session import get_db
from src.services.tasks_services import TasksService

task_router = APIRouter()

@task_router.post('/', summary='Создать задачу')
async def create_task(
        body: CreateTasks,
        service: TasksService = Depends(),
        db: AsyncSession = Depends(get_db)
):
    await service.create_tasks(body, db)
    return MessageResponse(message='Задание успешно создано')



@task_router.put('/', summary='Обновить задание')
async def get_tasks(
        body: UpdateTasks,
        service: TasksService= Depends(),
        db:AsyncSession= Depends(get_db)
):
 await service.get_tasks(body,db)
 return MessageResponse(message='Задание успешно получено')


@task_router.delete('/', summary="Удалить задачу")
async def delete_tasks(
        task_id: int,
        service: TasksService = Depends(),
        db:AsyncSession = Depends(get_db)
):
    await service.delete_task(task_id,db)
    return MessageResponse(message='Задание успешно удалено')

