from functools import wraps

from sqlalchemy.ext.asyncio import AsyncSession

from src.api.schemas.tasks_schemas import CreateTasks, UpdateTasks
from src.db.postgres.repositories.tasks_repository import TasksRepository


class TasksService:

    async def create_tasks(self, data: CreateTasks, db_session: AsyncSession):
        task_repository = TasksRepository(db_session)
        task = await  task_repository.create_task(data)
        return task

    async def update_tasks(self,data:UpdateTasks,db_session:AsyncSession):
        task_repository= TasksRepository(db_session)
        task = await task_repository.update_tasks(data)
        return task

    async def delete_task(self,  task_id, db_session:AsyncSession):
        task_repository = TasksRepository(db_session)
        task = await task_repository.delete_tasks(task_id)