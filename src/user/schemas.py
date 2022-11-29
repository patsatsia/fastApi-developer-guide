from pydantic import BaseModel


class User(BaseModel):
    username: str
    email: str

    class Config:
        orm_mode = True


class UserOut(User):
    id: int


class UserAuth(User):
    password: str


class UserLogin(UserAuth):
    pass


class UserTokens(BaseModel):
    access_token: str
    refresh_token: str
