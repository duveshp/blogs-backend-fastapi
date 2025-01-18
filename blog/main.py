from fastapi import Depends, FastAPI

from .dependencies import get_query_token, get_token_header
from .routers import items, users

app = FastAPI()


app.include_router(users.router)
app.include_router(items.router)



@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}

# from fastapi import FastAPI,HTTPException
# from . import schemas,models
# from .database import engine, SessionLocal
# from sqlmodel import SQLModel

# # models.Base.metadata.create_all(bind=engine)
# SQLModel.metadata.create_all(engine)

# app = FastAPI()

# @app.post('/blog')
# def createBlog(request:schemas.OpsBlogs, session:SessionLocal) -> models.Blog2:
#     new_blog = models.Blog2(title=request.title,body=request.body,published_at=request.published_at)
#     session.add(new_blog)
#     session.commit()
#     session.refresh(new_blog)
#     return new_blog

# @app.get("/blog/{blog_id}")
# def read_hero(hero_id: int, session: SessionLocal) -> models.Blog2:
#     blog = session.get(models.Blog2, hero_id)
#     if not blog:
#         raise HTTPException(status_code=404, detail="Hero not found")
#     return blog


