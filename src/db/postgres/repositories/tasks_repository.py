from sqlalchemy import delete, select, and_

from contextlib import AbstractContextManager
from typing import Callable

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from src.api.schemas.tasks_schemas import CreateTasks
from src.db.postgres.models.tasks import Tasks
from src.db.postgres.models.users import Users
from datetime import datetime

from src.db.postgres.models.users_tasks import UsersTasks


class TasksRepository:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def create_task(self, data):
        new_task=Tasks(
            description=data.description,
            status=data.status or False,
            title=data.title,
            due_time=data.due_time,
            created_at=data.created_at,
            priority=data.priority,
            task_date=data.task_date,
        )
        self._session.add(new_task)
        await self._session.commit()
        await self._session.refresh(new_task)

        link = UsersTasks(
            user_id=data.user_id,
            task_id=new_task.id
        )
        self._session.add(link)

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
            if data.due_time is not None:
                task.due_time = data.due_time
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

    async def get_tasks(self, date_from: datetime, date_to: datetime, user_id: int):
        query = (
            select(Tasks)
            .join(UsersTasks, UsersTasks.task_id == Tasks.id)
            .where(
                and_(
                    Tasks.task_date >= date_from,
                     Tasks.task_date <= date_to,
                    UsersTasks.user_id == user_id
                )
            )
        )
        result = await self._session.execute(query)
        tasks = result.scalars().all()
        return tasks
