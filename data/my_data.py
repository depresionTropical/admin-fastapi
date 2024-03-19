from models.post import Post
from uuid import uuid1
posts = [
    {
    "id": uuid1().int,
    "title": "First Post",
    "content": "This is the content of the first post",
    "published": True,
    "rating": 4
    }
]
