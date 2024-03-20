from typing import Optional
from pydantic import BaseModel


class Post(BaseModel):
    id : Optional[int]=None
    title: Optional[str] = None
    content: str
    published: bool = False
    rating : Optional[int]=None
