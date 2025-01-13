from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return 'Hello Duvesh..'


#QueryParams
@app.get('/blog')
def getQueryParams(limit):
    return {'data': f'{limit} blogs published..'}

@app.get('/blog/defaultvalues')
def getQueryParams(limit = 10, published: bool = True):
    if published:
        return {'data': f'{limit} blogs published..'}
    else:
        return {'data': f'{limit} blogs published and unpublished..'}
    

#if even one param is defined with default value, all the params inside brckt needs a default value

@app.get('/blog/optionalValues')
def getQueryParams(limit = 10, published: bool = True, sort: Optional[str]= None):
    if published:
        return {'data': f'{limit} blogs published..{sort}'}
    else:
        return {'data': f'{limit} blogs published and unpublished.{sort}'}


#PathParams

@app.get('/blog/{id}') 
def getPathParams(id:int):  #add :int for data type strict validation
    return {'data':id}