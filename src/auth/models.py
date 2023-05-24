from datetime import datetime

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

from src.database import Base


class User(SQLAlchemyBaseUserTable[int], Base):
    """Create user table in the database"""
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(length=255), nullable=False)
    registered_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
