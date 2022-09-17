from fastapi import FastAPI, Depends
from app.config import get_setting, Settings

app = FastAPI()

@app.get("/ping")
async def pong(settings: Settings = Depends(get_setting)):
    return {"ping": "pong!",
            "environment": settings.environment,
            "testing": settings.testing}