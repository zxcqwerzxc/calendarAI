from sqlalchemy import update, delete, select, desc, func
from contextlib import AbstractContextManager
from typing import Callable

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from src.api.schemas.tasks_schemas import CreateTasks
from src.db.postgres.models.tasks import Tasks


class TasksRepository:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def create_task(self,data):
        new_task= Tasks(
            description =data.description,
            status = data.status,
            title = data.title,
            due_date = data.due_date,
            created_at = data.created_at,
            priority = data.priority
        )
        self._session.add(new_task)
        await self._session.commit()
        await self._session.refresh(new_task)
        return new_task

    async def get_tasks(self,data):
        task = Tasks(
            description=data.description,
            status=data.status,
            title=data.title,
            due_date=data.due_date,
            priority=data.priority
        )
        self._session.add(task)
        await self._session.commit()
        await self._session.refresh(task)
        return task

    async def delete_tasks(self,task_id):
        query = (
            delete(Tasks)
            .where(Tasks.id == task_id)
        )
        await self._session.execute(query)
        await self._session.commit()

