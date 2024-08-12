from fastapi import FastAPI, Response, status ,HTTPException, Depends
from fastapi.params import Body  
from pydantic import BaseModel   
from typing import Optional, List     
from random import randrange     
import psycopg2 
from psycopg2.extras import RealDictCursor
import time                        
from app import models, schemas, utils
from app.database import SessionLocal, engine, get_db
from sqlalchemy.orm import Session 
# from app.schemas import PostCreate
# from passlib.context import CryptContext  # type: ignore
from app.routers import auth, post, user 

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
        
while (True):

    try:
        conn = psycopg2.connect(
            host = 'localhost', 
            database = 'fastapi', 
            user = 'postgres', 
            password = 'krutarth1112', 
            cursor_factory = RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was succesful!")
        break 

    except Exception as error:
        print("Unable to connect to database!\n")
        print("Error : ", error)
        time.sleep(2)

# def find_post(id):
#     for p in my_posts:
#         if p["id"]==id:
#             return p

# def find_index_post(id):
#     for i,p in enumerate(my_posts):
#         if p['id']==id:
#             return i 

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)


# Root 
@app.get("/")
def root():
    return {"message": "Welcome to my API"}
