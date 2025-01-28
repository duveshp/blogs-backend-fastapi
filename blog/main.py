# from fastapi import Depends, FastAPI,UploadFile,File

# from .dependencies import get_query_token, get_token_header
# from .routers import items, users
# import shutil
# import os
# from .database import engine, SessionLocal
# from sqlmodel import Session,SQLModel
# from .models import FileRecord


# app = FastAPI()

# SQLModel.metadata.create_all(engine)

# app.include_router(users.router)
# app.include_router(items.router)


# UPLOAD_DIR = "uploaded_files"
# os.makedirs(UPLOAD_DIR, exist_ok=True)

# @app.get("/")
# async def root():
#     return {"message": "Hello Bigger Applications!"}

# @app.post("/upload/")
# async def upload_file(file: UploadFile = File(...), db: SessionLocal = SessionLocal()):
#     file_location = os.path.abspath(os.path.join(UPLOAD_DIR, file.filename))
    
#     with open(file_location, "wb") as buffer:
#         shutil.copyfileobj(file.file, buffer)
    
#     file_record = FileRecord(filename=file.filename, filepath=file_location)
#     db.add(file_record)
#     db.commit()
#     db.refresh(file_record)
    
#     return {"filename": file.filename, "filepath": file_location}

# # from fastapi import FastAPI,HTTPException
# # from . import schemas,models
# # from .database import engine, SessionLocal
# # from sqlmodel import SQLModel

# # # models.Base.metadata.create_all(bind=engine)
# # SQLModel.metadata.create_all(engine)

# # app = FastAPI()

# # @app.post('/blog')
# # def createBlog(request:schemas.OpsBlogs, session:SessionLocal) -> models.Blog2:
# #     new_blog = models.Blog2(title=request.title,body=request.body,published_at=request.published_at)
# #     session.add(new_blog)
# #     session.commit()
# #     session.refresh(new_blog)
# #     return new_blog

# # @app.get("/blog/{blog_id}")
# # def read_hero(hero_id: int, session: SessionLocal) -> models.Blog2:
# #     blog = session.get(models.Blog2, hero_id)
# #     if not blog:
# #         raise HTTPException(status_code=404, detail="Hero not found")
# #     return blog


from fastapi import FastAPI,HTTPException
from blog.mlmodels.model import detect_anomaly 

app = FastAPI()

@app.post("/predict")
async def predict():
    # Convert the incoming data to a list
    #feature_list = [features.feature1, features.feature2, features.feature3]
    
    # Get the prediction from the model
    result = detect_anomaly()
    
    return result

