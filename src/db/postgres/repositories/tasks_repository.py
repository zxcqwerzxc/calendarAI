from sqlalchemy import delete, select, and_

from contextlib import AbstractContextManager
from typing import Callable

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from src.api.schemas.tasks_schemas import CreateTasks
from src.db.postgres.models.tasks import Tasks
from src.db.postgres.models.users import Users
from datetime import datetime


class TasksRepository:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def create_task(self, data):
        new_task = Tasks(
            description=data.description,
            status=data.status,
            title=data.title,
            due_date=data.due_date,
            created_at=data.created_at,
            priority=data.priority
        )
        self._session.add(new_task)
        await self._session.commit()
        await self._session.refresh(new_task)
        return new_task

    async def update_tasks(self, task_id, data):
        stmt = select(Tasks).where(Tasks.id == task_id)
        result = await self._session.execute(stmt)
        task = result.scalars().first()

        if task:
            if data.description is not None:
                task.description = data.description
            if data.status is not None:
                task.status = data.status
            if data.title is not None:
                task.title = data.title
            if data.due_date is not None:
                task.due_date = data.due_date
            if data.priority is not None:
                task.priority = data.priority
            await self._session.commit()

    async def delete_tasks(self, task_id):
        query = (
            delete(Tasks)
            .where(Tasks.id == task_id)
        )
        await self._session.execute(query)
        await self._session.commit()

    async def get_task(self, task_id):
        query = (
            select(Tasks)
            .where(Tasks.id == task_id)
        )
        result = await self._session.execute(query)
        task = result.scalar_one_or_none()

        return task

    async def get_tasks(self, date_from: datetime, date_to: datetime):
        query = (
            select(Tasks)
            .where(
                and_(Tasks.task_date >= date_from, Tasks.task_date <= date_to))
        )
        result = await self._session.execute(query)
        tasks = result.scalars().all()
        return tasks
