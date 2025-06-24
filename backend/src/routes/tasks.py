"""Routes for Tasks"""

from fastapi import APIRouter, Depends, status, Path
from sqlalchemy.orm import Session

from ..db_operations import get_db
from ..logger import logger
from ..basemodels import tasks as tasks_bm
from ..db_operations.crud_ops import tasks as tasks_crud

task_router = APIRouter(prefix="/tasks", tags=["Task Manager"])


# Create a Task
@task_router.post(
    "", response_model=tasks_bm.TaskResponse, status_code=status.HTTP_201_CREATED
)
def create_new_task(
    request: tasks_bm.TaskCreateRequest, session: Session = Depends(get_db)
):
    """
    Create new task
    """
    logger.info("Input: request - %s", request)
    new_task = tasks_crud.create_item(session, request)
    return new_task


# Fetch tasks
@task_router.get(
    "", response_model=tasks_bm.PaginatedTaskResponse, status_code=status.HTTP_200_OK
)
def fetch_tasks(
    params: tasks_bm.Pagination = Depends(), session: Session = Depends(get_db)
):
    """
    Fetch tasks
    """
    total, records = tasks_crud.get_items(session, params)
    response = {"total": total, "records": records}

    return response


# Update a Task
@task_router.put(
    "/{task_id}",
    response_model=tasks_bm.TaskResponse,
)
def update_task(
    request: tasks_bm.TaskUpdateRequest,
    task_id: int = Path(description="Task ID"),
    session: Session = Depends(get_db),
):
    """
    Update task status
    """
    logger.info("Input: request - %s, task_id - %s", request, task_id)
    record = tasks_crud.update_item(session, task_id, request)
    return record


# Delete a Task
@task_router.delete("/{task_id}")
def delete_task(
    task_id: int = Path(description="Task ID"),
    session: Session = Depends(get_db),
):
    """
    Delete a task
    """
    logger.info("Input: task_id - %s", task_id)
    tasks_crud.delete_item(session, task_id)

    return {"message": "Task deleted successfully"}
