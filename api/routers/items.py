import uuid
import controllers

from typing import List
from fastapi.routing import APIRouter
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import schemas
from utils.utils import get_db

router = APIRouter()

@router.post("/", summary="Create item", description="Create an item", response_model=schemas.Item)
def create_item(item: schemas.ItemBase, db: Session = Depends(get_db)):
    try:
        return controllers.items.create(obj_in=item, db=db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/", summary="Get items", description="Get all items", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return controllers.items.get_multi(skip=skip, limit=limit, db=db)

@router.get("/{item_id}", summary="Get item", description="Get an item", response_model=schemas.Item)
def read_item(item_id, db: Session = Depends(get_db)):
    try:
        return controllers.items.get(id=uuid.UUID(item_id).hex, db=db)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))