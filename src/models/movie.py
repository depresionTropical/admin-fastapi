from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, validator


class Movie_update(BaseModel):
  title: str 
  director: str = Field(min_length=5, max_length=15, default='Director')
  category: str = Field(min_length=5, max_length=15, default='Drama')
  year: int = Field(ge=1900, le=datetime.today().year, default=2022)

  model_config={
    'json_schema_extra':{
      'example':{
        'title': 'Update Movie',
        'director': 'Update Director',

        'year': 2022
      }
    }
  }

  @validator('title')
  def validate_title(cls, v):
    if len(v) < 5:
      raise ValueError('Title must be at least 5 characters')
    if len(v) > 15:
      raise ValueError('Title must be at most 15 characters')
    return v

class Movie(Movie_update):
  id: int
  model_config={
    'json_schema_extra':{
      'example':{
        'id': 1,
        'title': 'New Movie',
        'director': 'Director',
        'category': 'Drama',
        'year': 2022
      }
    }
  }

