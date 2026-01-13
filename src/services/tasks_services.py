from sqlalchemy.ext.asyncio import AsyncSession

from src.api.schemas.tasks_schemas import CreateTasks, UpdateTasks, GetTask, GetTasks, GetShortedTask
from src.db.postgres.repositories.tasks_repository import TasksRepository


class TasksService:

    async def create_tasks(self, data: CreateTasks, db_session: AsyncSession):
        task_repository = TasksRepository(db_session)
        task = await task_repository.create_task(data)
        return task

    async def update_tasks(self, task_id, data: UpdateTasks, db_session: AsyncSession):
        task_repository = TasksRepository(db_session)
        task = await task_repository.update_tasks(task_id, data)
        return task

    async def delete_task(self, task_id, db_session: AsyncSession):
        task_repository = TasksRepository(db_session)
        task = await task_repository.delete_tasks(task_id)

    async def get_task(self, task_id, db_session: AsyncSession):
        task_repository = TasksRepository(db_session)
        task_data = await task_repository.get_task(task_id)

        return GetTask(
            id=task_data.id,
            description=task_data.description,
            status=task_data.status,
            title=task_data.title,
            due_date=task_data.due_date,
            created_at=task_data.created_at,
            priority=task_data.priority
        )

    async def get_tasks(self, db_session: AsyncSession, date_from, date_to, user_id):
        task_repository = TasksRepository(db_session)
        task_data = await task_repository.get_tasks(date_from, date_to, user_id)

        return GetTasks(
            tasks=[
                GetShortedTask(
                    id=task.id,
                    task_date=task.task_date,
                    title=task.title,
                    task_time=task.created_at,
                    priority=task.priority
                )
                for task in task_data
            ]
        )
