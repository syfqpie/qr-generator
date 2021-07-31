from . import config
from fastapi import APIRouter

from routers import items, micros

router = APIRouter()
settings = config.settings

@router.get("/")
def home():
    return {"message": "Hello World"}

router.include_router(
    items.router,
    prefix="/items",
    tags=["items"]
)
router.include_router(
    micros.router,
    prefix="/services",
    tags=["services"]
)