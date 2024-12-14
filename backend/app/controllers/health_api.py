import logging
from fastapi import APIRouter

router = APIRouter(tags=["health-api"])
logger = logging.getLogger(__name__)

@router.get("/ready")
async def ready():
    return {"message": "service is ready to process requests"}

@router.get("/live")
async def live():
    return {"message": "service is live"}