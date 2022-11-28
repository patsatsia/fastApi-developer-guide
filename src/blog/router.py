from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from sqlalchemy.orm import Session

from src.blog import schemas, crud
from src.database import get_db

router = APIRouter()


@router.get("/blog/", response_model=schemas.BlogRetrieveList)
def retrieve_all_blogs(db: Session = Depends(get_db)):
    return {"blogs": crud.retrieve_blogs(db=db)}


@router.post("/blog/", response_model=schemas.BlogRetrieve, status_code=status.HTTP_201_CREATED)
def create_blog(blog_data: schemas.BlogCreate, db: Session = Depends(get_db)):
    return crud.create_blog(blog_data=blog_data, db=db)


@router.get("/blog/{blog_uuid}/", response_model=schemas.BlogRetrieve)
def retrieve_single_blog(blog_uuid: UUID, db: Session = Depends(get_db)):
    if blog := crud.retrieve_single_blog(blog_uuid=blog_uuid, db=db):
        return blog

    raise HTTPException(status_code=404, detail="Item not found")
