import logging

from fastapi import APIRouter

router = APIRouter()
logger = logging.getLogger()

@router.get(path="/")
def get_hello()-> str:
    return "Hello World!"