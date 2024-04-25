import logging

from fastapi import APIRouter

from src.routes.user import user

api_router = APIRouter()
logger = logging.getLogger()

API_VERSION = "API_VERSION_TO_REPLACE"

api_router.include_router(user.router, prefix="/user", tags=["Users"])


#Healthcheck
@api_router.get("/healthcheck", tags= ["API Health Check"])
async def api_health_check():
    return {"message": f"Fast API v {API_VERSION}"}
