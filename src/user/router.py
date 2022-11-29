from fastapi import Depends, HTTPException
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from starlette import status

from src.core.authentication import get_hashed_password, verify_password, get_jwt_tokens
from src.database import get_db
from src.user import schemas, crud

router = APIRouter()


@router.post('/user/register/', response_model=schemas.UserOut)
def create_user(user_data: schemas.UserAuth, db: Session = Depends(get_db)):
    user = crud.retrieve_user_with_email(db=db, email=user_data.email)

    if user is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with given email already exist"
        )

    return crud.create_user(db=db, user_data={
        'email': user_data.email,
        'username': user_data.username,
        'password': get_hashed_password(user_data.password),
    })


@router.post('/user/login/', response_model=schemas.UserTokens)
def login_user(credentials: schemas.UserLogin, db: Session = Depends(get_db)):
    user = crud.retrieve_user_with_email(db=db, email=credentials.email)

    if not user or not verify_password(password=credentials.password, hashed_pass=user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with given credentials does not exist"
        )

    return get_jwt_tokens(subject=user.email)
