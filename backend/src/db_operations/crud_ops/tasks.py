"""CRUD ops for Tasks"""

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
