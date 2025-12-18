import datetime
import uuid
from tokenize import String

from sqlalchemy import Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship, composite
from src.db.postgres.session import Base

class Users(Base):
    __tablename__= 'users'
    __table_args__ = {
        'comment': 'Пользователи'
    }

    id:Mapped[int]=mapped_column(primary_key=True,autoincrement=True)
    login:Mapped[str]= mapped_column(comment="логин пользователя")
    password:Mapped[int]= mapped_column(comment="пароль пользователя")

