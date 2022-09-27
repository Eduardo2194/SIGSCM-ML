from random import random
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Text
from datetime import datetime
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from uuid import uuid4 as uuid
import uvicorn
import random

app = FastAPI()

posts = []

mlresponse = random.randint(0,9)

# Post model
class ReqMl(BaseModel):
    fecha_inicio: str = datetime.now()
    fecha_fin: str = datetime.now()

# Post model
class Post(BaseModel):
    id: Optional[str]
    title: str
    author: str
    content: Text
    created_at: datetime =  datetime.now()
    published_at: Optional[datetime] 
    published: Optional[bool] = False


@app.post('/sigmcs-mlsecuence')
def save_post(post: ReqMl):
    posts.append(post.dict())
    return {"day1": random.randint(10,30), "day2": random.randint(10,30), "day3": random.randint(10,30), "day4": random.randint(10,30), "day5": random.randint(10,30), "day6": random.randint(10,30), "day7": random.randint(10,30)  }

"""
@app.get('/')
def read_root():
    return {"welcome": "Welcome to my API"}

@app.get('/posts')
def get_posts():
    return posts

@app.post('/posts')
def save_post(post: Post):
    post.id = str(uuid())
    posts.append(post.dict())
    return posts[-1]

@app.get('/posts/{post_id}')
def get_post(post_id: str):
    for post in posts:
        if post["id"] == post_id:
            return post
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete('/posts/{post_id}')
def delete_post(post_id: str):
    for index, post in enumerate(posts):
        if post["id"] == post_id:
            posts.pop(index)
            return {"message": "Post has been deleted succesfully"}
    raise HTTPException(status_code=404, detail="Item not found")

@app.put('/posts/{post_id}')
def update_post(post_id: str, updatedPost: Post):
    for index, post in enumerate(posts):
        if post["id"] == post_id:
            posts[index]["title"]= updatedPost.dict()["title"]
            posts[index]["content"]= updatedPost.dict()["content"]
            posts[index]["author"]= updatedPost.dict()["author"]
            return {"message": "Post has been updated succesfully"}
    raise HTTPException(status_code=404, detail="Item not found")
"""