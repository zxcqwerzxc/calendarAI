from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.postgres.session import Base


class UsersTasks(Base):
    __tablename__ = 'users_tasks'
    __table_args__ = {'comment': 'Связующая таблица пользователь ↔ задача'}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    task_id: Mapped[int] = mapped_column(ForeignKey('tasks.id'))

    user: Mapped["Users"] = relationship()
    task: Mapped["Tasks"] = relationship()