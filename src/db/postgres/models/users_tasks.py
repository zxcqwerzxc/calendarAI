import datetime
from sqlalchemy import ForeignKey, String, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.db.postgres.session import Base


class UsersTasks(Base):
    __tablename__ = 'users_tasks'

    __table_args__ = {
        'comment': 'Действия связанные с пользователями'
    }

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    user_id:Mapped[int] = mapped_column(
        ForeignKey('user.id'),
        comment="ссылка на айди пользователя"    )
    tasks_id: Mapped[int] = mapped_column(
        ForeignKey('tasks.id'),
        comment="ссылка на айди задания"
    )