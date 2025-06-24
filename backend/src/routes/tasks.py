"""Routes for Tasks"""

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from ..db_operations import get_db
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
    new_task = tasks_crud.create_item(session, request)
    return new_task


