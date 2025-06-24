"""DB Models"""

import enum
from sqlalchemy import Column, Integer, String, DateTime, Enum, func

from .db_connection import Base, engine


class TaskStatus(str, enum.Enum):
    """
    Enum for task status
    """

    pending = "pending"
    completed = "completed"


class Task(Base):
    """
    SQLAlchmey model for Task table
    """

    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, unique=True)  # Assuming title will be unique
    description = Column(String, nullable=False)
    status = Column(Enum(TaskStatus), nullable=False, default=TaskStatus.pending)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


Base.metadata.create_all(bind=engine)
