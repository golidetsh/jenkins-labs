from fastapi import FastAPI
from fastapi.params import Body
from fastapi import FastAPI , Response, Depends, status, HTTPException 
from pydantic import BaseModel
from typing import Optional
from random import randrange
import psycopg2
import os
import logging
from psycopg2.extras import RealDictCursor
from time import sleep
from . import models
from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from .utils import PrometheusMiddleware, metrics

APP_NAME = os.environ.get("APP_NAME", "app")
EXPOSE_PORT = os.environ.get("EXPOSE_PORT", 8000)

# Creates tables in db
# models.Base.metadata.create_all(bind=engine)


app = FastAPI()
app.add_middleware(PrometheusMiddleware, app_name=APP_NAME)
app.add_route("/metrics", metrics)


class EndpointFilter(logging.Filter):
    # Uvicorn endpoint access log filter
    def filter(self, record: logging.LogRecord) -> bool:
        return record.getMessage().find("GET /metrics") == -1


# Filter out /endpoint
logging.getLogger("uvicorn.access").addFilter(EndpointFilter())

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True

# @app.get("/sqlalchemy")
# def test_db(db: Session = Depends(get_db)):
   
#     posts = db.query(models.Post).all()

#     return {"data": "success"}


# while True:

    # try:
    #     conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres',
    #                          password='abc123', cursor_factory=RealDictCursor)
    #     cursor = conn.cursor()
    #     print("Database connected successfully")
    #     break
    # except Exception as error:
    #     print("Database connection was not successful")
    #     print("Error: ", error)
    #     sleep(2)


my_posts = [{"title": "Everyday Cooking","content": "Top 10 recipes","published": "True","rating": "3", "id": 2}]


@app.get("/")
async def root():
    logging.error("landing page")
    return {"message": "Welcome to Facebook API"}


# @app.post("/createposts", status_code=status.HTTP_201_CREATED)
# def create_posts(post: Post):
#     cursor.execute("""INSERT INTO posts (title, content, published) VALUES(%s, %s, %s) RETURNING  
#                    * """,
#                    (post.title, post.content, post.published))
    
#     new_post = cursor.fetchone()

#     conn.commit()
#     return {"data": new_post}



# @app.get("/posts")
# def get_posts(db: Session = Depends(get_db)):

#     # cursor.execute("""SELECT * FROM posts""")
#     # posts = cursor.fetchall()
#     posts = db.query(models.Post).all()

#     return {"data": posts}




# def find_post(id):
#     for p in my_posts:
#         if p["id"] == id:
#          return p



# @app.get("/posts/{id}")
# def get_post(id: int, response: Response):
#     cursor.execute("""SELECT * FROM posts WHERE id = %s""", (str(id),))
#     post = cursor.fetchone()

#     if not post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
#                             detail =f"Post with id {id} was not found")
#     return {"Post detail" : post }


# @app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
# def get_post(id: int):
#     cursor.execute("""DELETE FROM posts WHERE id = %s returning *""", (str(id),))
#     deleted_post = cursor.fetchone()
#     conn.commit()

#     if deleted_post == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
#                             detail =f"Post with id {id} does not exist")
#     return Response(status_code=status.HTTP_204_NO_CONTENT)

# @app.put("/posts/{id}")
# def update_post(id: int, post: Post):

#     cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s  RETURNING *""", (post.title,
#     post.content, post.published, str(id)))
#     updated_post = cursor.fetchone()
#     conn.commit()

#     if updated_post == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
#                             detail =f"Post with id {id} does not exist")
#     return {"data" : updated_post }


