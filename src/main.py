from fastapi import FastAPI
from src.blog.router import router as blog_router
from src.database import Base, engine

Base.metadata.create_all(engine)

app = FastAPI()

app.include_router(blog_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
