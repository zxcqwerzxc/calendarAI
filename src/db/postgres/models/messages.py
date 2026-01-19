from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.db.postgres.session import Base


class Messages(Base):
    __tablename__ = 'messages'
    __table_args__ = {'comment': 'Сообщения пользователей'}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    massage: Mapped[str] = mapped_column(comment="сообщения задачи")
    created_at: Mapped[datetime] = mapped_column(comment="время сообщения")

    session_id: Mapped[int] = mapped_column(ForeignKey('users.id'))