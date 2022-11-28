from fastapi import FastAPI
from src.blog.router import router as blog_router
from src.config import settings
from src.database import Base, engine

Base.metadata.create_all(engine)

app = FastAPI(title=settings.APP_NAME)

app.include_router(blog_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
