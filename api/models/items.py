import uuid
from datetime import datetime

from database import Base

from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import null


class Item(Base):
    __tablename__ = "items"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    name = Column(String, index=True)
    description = Column(String, index=True, nullable=True)
    is_active = Column(Boolean, index=True, default=True)
    created_at = Column(DateTime, default=datetime.now())
    modified_at = Column(DateTime, nullable=True)
