from fastapi import FastAPI
from fastapi.params import Body 
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None
    

my_posts = [{"title": "Everyday Cooking","content": "Top 10 recipes","published": "True","rating": "3", "id": 2}]


@app.get("/")
async def root():
    return {"message": "Welcome to Facebook API"}

@app.post("/createposts")
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 10000000)
    return {"data": post_dict}


@app.get("/posts")
def get_posts():
    return {"data": my_posts}