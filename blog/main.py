from fastapi import FastAPI
from . import schemas,models
from .database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post('/blog')
def createBlog(request:schemas.Blogs):
    return request