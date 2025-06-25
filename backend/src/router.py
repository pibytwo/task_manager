"""Main router"""

from fastapi import APIRouter

from .routes.tasks import task_router

app_router = APIRouter(prefix="/api/v1")

app_router.include_router(task_router)


@app_router.get("/health_check", tags=["Health Check"])
def health_check():
    """
    Health check API
    """
    return "Ok"
