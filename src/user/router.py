from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from src.core.authentication import get_hashed_password
from src.database import get_db
from src.main import app
from src.user import schemas, crud


@app.post('/user/register/', response_model=schemas.UserOut)
def create_user(data: schemas.UserAuth, db: Session = Depends(get_db)):
    user = crud.retrieve_user_with_email(db=db, email=data.email)

    if user is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with given email already exist"
        )

    return crud.create_user(db=db, user_data={
        'email': data.email,
        'password': get_hashed_password(data.password),
    })
