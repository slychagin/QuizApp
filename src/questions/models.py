from datetime import datetime

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class Question(Base):
    """Create Questions table in the database"""
    __tablename__ = "questions"

    id: Mapped[int] = mapped_column(primary_key=True)
    question_id: Mapped[int] = mapped_column(nullable=False)
    question: Mapped[str] = mapped_column(String(length=1024), nullable=False)
    answer: Mapped[str] = mapped_column(String(length=255), nullable=False)
    created_at: Mapped[str] = mapped_column(String(length=20), nullable=False)
    air_date: Mapped[str] = mapped_column(String(length=20), nullable=False)
    add_to_db_date: Mapped[str] = mapped_column(
        default=datetime.strftime(datetime.utcnow(), "%Y-%m-%d %H:%M:%S")
    )
