"""Basemodels for Tasks"""

from datetime import datetime
from typing import Literal
from pydantic import BaseModel, Field


class Pagination(BaseModel):
    """Pagination"""

    offset: int = Field(description="Offset", default=0)
    page_size: int = Field(description="Page size", default=10, ge=1, le=50)


class TaskBase(BaseModel):
    """TaskBase"""

    title: str = Field(
        description="Title of the task", examples=["Medicines", "Homework"]
    )
    description: str = Field(
        description="Description of the task",
        examples=["Take your medicines", "Do your homework"],
    )


class Status(BaseModel):
    """Status"""

    status: Literal["pending", "completed"] = Field(
        description="Status of the task", examples=["pending", "completed"]
    )


class TaskCreateRequest(TaskBase):
    """TaskCreateRequest"""





class TaskResponse(TaskBase, Status):
    """TaskResponse"""

    id: int = Field(description="Task ID")
    created_at: datetime = Field(description="Task creation date")



