from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from .base import ControllerBase
from models.items import Item
from database.schemas import ItemCreate, ItemUpdate


class ItemController(ControllerBase[Item, ItemCreate, ItemUpdate]):
    pass
    # def create_with_owner(
    #     self, db: Session, *, obj_in: ItemCreate, owner_id: int
    # ) -> Item:
    #     obj_in_data = jsonable_encoder(obj_in)
    #     db_obj = self.model(**obj_in_data, owner_id=owner_id)
    #     db.add(db_obj)
    #     db.commit()
    #     db.refresh(db_obj)
    #     return db_obj

    # def get_multi_by_owner(
    #     self, db: Session, *, owner_id: int, skip: int = 0, limit: int = 100
    # ) -> List[Item]:
    #     return (
    #         db.query(self.model)
    #         .filter(Item.owner_id == owner_id)
    #         .offset(skip)
    #         .limit(limit)
    #         .all()
    #     )


items = ItemController(Item)