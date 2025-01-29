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


import pandas as pd
import joblib
from fastapi import FastAPI, File, UploadFile
from blog.mlmodels.model import detect_anomaly  # Import anomaly detection function

app = FastAPI()

# Define the same columns used in training
COLUMNS_TO_KEEP = [
    'T_Q019_Q026_1', 'T_Q019_Q026_2', 'T_Q019_Q026_3',
    'T_Q019_Q026_4', 'T_Q019_Q026_5', 'T_Q019_Q026_6',
    'T_Q019_Q026_7', 'T_Q019_Q026_8'
]

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    # Read the uploaded CSV file
     # Read the uploaded CSV file
    df = pd.read_csv(file.file, encoding="latin1")

    # Ensure required columns exist (drop extra columns, fill missing ones)
    df = df[COLUMNS_TO_KEEP]

    # Perform anomaly detection for the entire dataset (batch processing)
    results = detect_anomaly(df)
    print(results)
    # Add results back to the DataFrame
    #df["anomaly_detected"] = [res["anomaly_detected"] for res in results]

    # Convert result to JSON
    #return df.to_dict(orient="records")
    return "DONE Processing"

