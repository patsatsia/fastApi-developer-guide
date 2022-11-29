from pydantic import BaseModel


class User(BaseModel):
    username: str
    email: str


class UserOut(User):
    id: int


class UserAuth(BaseModel):
    email: str
    password: str
