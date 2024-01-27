from fastapi import APIRouter
from routers import microserv


router = APIRouter()


@router.get("/")
def home():
    return {"detail": "Hello World"}


router.include_router(router=microserv.router, prefix="/services", tags=["services"])
