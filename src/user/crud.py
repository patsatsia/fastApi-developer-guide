from sqlalchemy.orm import Session

from src.user import models


def retrieve_user_with_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, user_data: dict):
    user = models.User(**user_data)
    db.add(user)
    db.commit()

    db.refresh(user)
    return user
