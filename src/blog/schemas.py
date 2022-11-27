from uuid import UUID

from pydantic import BaseModel, Field


class BlogBase(BaseModel):
    title: str = Field(max_length=64)
    text: str = Field(max_length=2048)

    class Config:
        orm_mode = True


class BlogCreate(BlogBase):
    pass


class BlogRetrieve(BlogBase):
    uuid: UUID


class BlogRetrieveList(BaseModel):
    blogs: list[BlogRetrieve] = []

    class Config:
        orm_mode = True
