from fastapi import APIRouter, Depends, status

from app.config import get_settings, Settings


router = APIRouter()

@router.get("/ping", status_code=status.HTTP_200_OK)
async def pong(settings: Settings = Depends(get_settings)):
    return {
        "ping": "pong!",
        "environment": settings.environment,
        "testing": settings.testing
    }