from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class Movie_update(BaseModel):
  title: str = Field(min_length=5, max_length=15, default='New Movie')
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

