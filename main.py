from fastapi import FastAPI
from fastapi.params import Body
from uuid import uuid1

# import models
from models.post import Post

# import data
from data.my_data import posts as my_posts

# create an instance of FastAPI
app = FastAPI()

# create a route
@app.get("/")
async def root():
  return {"message": "Hello World"}

@app.get("/posts")
def get_post():
  return {"data": my_posts}

@app.get("/posts/{post_id}")
def get_post_by_id(post_id: int):
  # return {"id": post_id}
  post = find_post(post_id)
  return {"data": post}

def find_post(post_id: int):
  return next((post for post in my_posts if post["id"] == post_id), None)
  

@app.post("/posts")
def create_post(post : Post):
  post_dict = post.dict()
  post_dict["id"] = uuid1().int
  my_posts.append(post_dict)
  return {"message": "Post is created successfully"}