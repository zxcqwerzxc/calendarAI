from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.db.postgres.session import Base


class Users(Base):
    __tablename__ = 'users'
    __table_args__ = {'comment': 'Пользователи'}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    login: Mapped[str] = mapped_column(comment="логин пользователя")
    password: Mapped[str] = mapped_column(comment="пароль пользователя")

    assigned_tasks: Mapped[list["Tasks"]] = relationship(      # ← строка "Tasks" — всё ок
        secondary="users_tasks",
        back_populates="assigned_users"
    )