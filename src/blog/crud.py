from uuid import UUID

from sqlalchemy.orm import Session

from src.blog import models, schemas
from src.core.pagination import PaginationQueryParams


def retrieve_blogs(db: Session, page_params: PaginationQueryParams):
    return db.query(models.Blog).offset(page_params.offset).limit(page_params.limit).all()


def retrieve_single_blog(blog_uuid: UUID, db: Session):
    return db.query(models.Blog).filter(models.Blog.uuid == str(blog_uuid)).first()


def create_blog(blog_data: schemas.BlogCreate, db: Session):
    blog = models.Blog(title=blog_data.title, text=blog_data.text)
    db.add(blog)
    db.commit()

    db.refresh(blog)
    return blog
