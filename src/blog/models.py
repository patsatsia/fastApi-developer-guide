from uuid import uuid4

from src.database import Base
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID


class Blog(Base):
    __tablename__ = 'blog'

    uuid = Column(UUID, default=lambda: str(uuid4()), primary_key=True, index=True, nullable=False)
    title = Column(String(64), index=True)
    text = Column(String(2048))
