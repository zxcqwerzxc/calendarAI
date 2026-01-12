from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.db.postgres.session import Base


class Params(Base):
    __tablename__ = 'params'
    __table_args__ = {'comment': 'Параметры пользователей'}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    description: Mapped[str] = mapped_column(comment="описание задачи")

    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))