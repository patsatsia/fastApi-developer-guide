from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from sqlalchemy.orm import Session

from src.blog import schemas, models
from src.database import get_db

router = APIRouter()


@router.get("/blog/", response_model=schemas.BlogRetrieveList)
def retrieve_all_blogs(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return {"blogs": blogs}


@router.post("/blog/", response_model=schemas.BlogRetrieve, status_code=status.HTTP_201_CREATED)
def create_blog(blog_data: schemas.BlogCreate, db: Session = Depends(get_db)):
    blog = models.Blog(
        title=blog_data.title,
        text=blog_data.text,
    )
    db.add(blog)
    db.commit()

    db.refresh(blog)
    return blog


@router.get("/blog/{blog_uuid}/", response_model=schemas.BlogRetrieve)
def retrieve_single_blog(blog_uuid: UUID, db: Session = Depends(get_db)):
    if blog := db.query(models.Blog).get(str(blog_uuid)):
        return blog

    raise HTTPException(status_code=404, detail="Item not found")
