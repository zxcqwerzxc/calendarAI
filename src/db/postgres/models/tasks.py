from datetime import datetime, date

from sqlalchemy.orm import Mapped, mapped_column

from src.db.postgres.session import Base


class Tasks(Base):
    __tablename__= 'tasks'
    __table_args__ = {
        'comment': 'Задания пользователей'
    }

    id:Mapped[int]= mapped_column(primary_key=True,autoincrement=True)
    description:Mapped[str]= mapped_column(comment="описание задачи")
    status:Mapped[bool]= mapped_column(comment= "статус задачи")
    title:Mapped[str]= mapped_column(comment="заголовок задачи")
    due_date:Mapped[datetime]= mapped_column(comment="время конца задачи")
    created_at:Mapped[datetime]= mapped_column(comment="время начала задачи")
    priority:Mapped[int]= mapped_column(comment="приоритет задачи")