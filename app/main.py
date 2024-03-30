from fastapi import FastAPI
from fastapi.params import Body
from fastapi import FastAPI , Response, status, HTTPException 
from pydantic import BaseModel
from typing import Optional
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True

while True:

    try:
        conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres',
                             password='abc123', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connected successfully")
        break
    except Exception as error:
        print("Database connection was not successful")
        print("Error: ", error)
        sleep(2)


my_posts = [{"title": "Everyday Cooking","content": "Top 10 recipes","published": "True","rating": "3", "id": 2}]


@app.get("/")
async def root():
    return {"message": "Welcome to Facebook API"}

@app.post("/createposts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    cursor.execute("""INSERT INTO posts (title, content, published) VALUES(%s, %s, %s) RETURNING  
                   * """,
                   (post.title, post.content, post.published))
    
    new_post =cursor.fetchone()
    
    conn.commit()

    return {"data": new_post}


@app.get("/posts")
def get_posts():
    cursor.execute("""SELECT * FROM posts""")
    posts = cursor.fetchall()
    print(posts)
    return {"data": posts}


def find_post(id):
    for p in my_posts:
        if p["id"] == id:
         return p


@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail =f"Post with id {id} was not found")
    return {"Post detail" : post }