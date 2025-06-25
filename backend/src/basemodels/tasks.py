"""Basemodels for Tasks"""

from datetime import datetime
from typing import List, Literal
from pydantic import BaseModel, Field


class Pagination(BaseModel):
    """Pagination"""

    page_no: int = Field(description="Page number", default=1, ge=1)
    page_size: int = Field(description="Page size", default=10, ge=1, le=50)


class TaskBase(BaseModel):
    """TaskBase"""

    title: str = Field(
        description="Title of the task",
        examples=["Medicines", "Homework"],
        min_length=1,
    )
    description: str = Field(
        description="Description of the task",
        examples=["Take your medicines", "Do your homework"],
        min_length=1,
    )


class Status(BaseModel):
    """Status"""

    status: Literal["pending", "completed"] = Field(
        description="Status of the task", examples=["pending", "completed"]
    )


class TaskCreateRequest(TaskBase):
    """TaskCreateRequest"""


class TaskUpdateRequest(Status):
    """TaskUpdateRequest"""


class TaskResponse(TaskBase, Status):
    """TaskResponse"""

    id: int = Field(description="Task ID")
    created_at: datetime = Field(description="Task creation date")


class PaginatedTaskResponse(BaseModel):
    """PaginatedTaskResponse"""

    total: int = Field(description="Total number of task records", examples=[100])
    records: List[TaskResponse] = Field(description="Task details")
