from fastapi import FastAPI
from fastapi.params import Body


app = FastAPI()

@app.get("/")
async def root():
  return {"message": "Hello World"}

@app.get("/post")
def get_post():
  return {"data": "This is a post"}

@app.post("/create-posts")
def create_post(play_load:  dict= Body(...)):
  print(play_load)
  return {"new_post": f"New post created with title: {play_load['title']}"}