"""CRUD ops for Tasks"""

from typing import List
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from ...logger import logger
from .. import models
from ...basemodels import tasks as tasks_bm


def create_item(
    session: Session, request: tasks_bm.TaskCreateRequest
) -> tasks_bm.TaskResponse:
    """
    To create new task
    Args:
        session (Session): DB Session
        request (tasks_bm.TaskCreateRequest): Request data

    Returns:
        tasks_bm.TaskResponse: Task details
    """

    try:
        new_task = models.Task(**request.model_dump())
        session.add(new_task)
        session.commit()
    except IntegrityError as e:
        session.rollback()
        logger.error("Error - %s", e)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Duplicate title..."
        ) from e
    return new_task


def get_items(
    session: Session, params: tasks_bm.Pagination
) -> tuple[int, List[tasks_bm.TaskResponse]]:
    """
    Fetch tasks

    Args:
        session (Session): DB Session
        params (tasks_bm.Pagination): Parameters

    Returns:
        tuple[int, List[tasks_bm.TaskResponse]]: Response
    """
    query = session.query(models.Task)
    total = query.count()
    offset = (params.page_no - 1) * params.page_size
    records = query.offset(offset).limit(params.page_size).all()

    return total, records


def update_item(
    session: Session, task_id: int, request: tasks_bm.TaskUpdateRequest
) -> tasks_bm.TaskResponse:
    """
    Update status of a task

    Args:
        session (Session): DB Session
        task_id (int): Task ID
        request (tasks_bm.TaskUpdateRequest): Status

    Raises:
        HTTPException: 404 not found

    Returns:
        tasks_bm.TaskResponse: Response
    """
    record = session.query(models.Task).filter(models.Task.id == task_id).first()

    if not record:
        message = "Task not found"
        logger.error("Error - %s for ID - %s", message, task_id)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=message)

    record.status = request.status

    session.commit()
    session.refresh(record)
    return record


def delete_item(session: Session, task_id: int) -> None:
    """
    Delete a task

    Args:
        session (Session): DB Session
        task_id (int): Task ID

    Raises:
        HTTPException: 404 not found
    """
    record = session.query(models.Task).filter(models.Task.id == task_id).first()

    if not record:
        message = "Task not found"
        logger.error("Error - %s for ID - %s", message, task_id)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=message)

    session.delete(record)
    session.commit()
