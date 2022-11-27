from fastapi import APIRouter, Depends
from starlette import status
from sqlalchemy.orm import Session

from src.blog import schemas, models
from src.database import get_db

router = APIRouter()


@router.get("/blogs/", response_model=schemas.BlogRetrieveList)
def retrieve_all_blogs(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return {"blogs": blogs}


@router.post("/blogs/", response_model=schemas.BlogRetrieve, status_code=status.HTTP_201_CREATED)
def create_blog(blog_data: schemas.BlogCreate, db: Session = Depends(get_db)):
    blog = models.Blog(
        title=blog_data.title,
        text=blog_data.text,
    )
    db.add(blog)
    db.commit()

    db.refresh(blog)
    return blog
