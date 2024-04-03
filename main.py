from fastapi import FastAPI, Body
# response HTML
from fastapi.responses import HTMLResponse

# create an instance of the FastAPI class
app = FastAPI()

# list of movies
movies = [
    {
        'id': 1,
        'title': 'The Shawshank Redemption',
        'director': 'Frank Darabont',
        'category': 'drama',
        'year': 1994
    },
    {
        'id': 2,
        'title': 'The Godfather',
        'director': 'Francis Ford Coppola',
        'category': 'crime',
        'year': 1972
    },
    {
        'id': 3,
        'title': 'The Dark Knight',
        'director': 'Christopher Nolan',
        'category': 'action',
        'year': 2008
    }
]

# define root endpoint returns dictionary /


@app.get('/', tags=['Home'])
def home():
    return {'message': 'Welcome to the API'}

# define endpoint that returns a list of movies /movies


@app.get('/movies', tags=['Movies'])
def home():
    return movies

# define endpoint that return id /movies/{id}


@app.get('/movies/{id}', tags=['Movies'])
def get_movie(id: int):
    for movie in movies:
        if movie['id'] == id:
            return movie
    else:
        return {'message': 'Movie not found'}

# define endpoint that retrurn movie by category and year querry /movies?category=action


@app.get('/movies/', tags=['Movies'])
def get_movies(category: str, year: int):
    for movie in movies:
        if movie['category'] == category and movie['year'] == year:
            return movie
    else:
        return {'message': 'Movie not found'}


# define endpiont to intert new movie by id /movies/{id}
@app.post('/movies/', tags=['Movies'])
def create_movie(
    id: int = Body(),
    title: str = Body(),
    director: str = Body(),
    category: str = Body(),
    year: int = Body()):
    
    new_movie = {
        'id': id,
        'title': title,
        'director': director,
        'category': category,
        'year': year
    }
    movies.append(new_movie)
    return new_movie


# define endpoint to update by body data movie by id /movies/{id}
@app.put('/movies/{id}', tags=['Movies'])
def update_movie(
    id: int, 
    title: str = Body(), 
    director: str = Body(), 
    category: str = Body(), 
    year: int = Body()):

    for movie in movies:
        if movie['id'] == id:
            movie['title'] = title
            movie['director'] = director
            movie['category'] = category
            movie['year'] = year
            return movies
    else:
        return {'message': 'Movie not found'}
    
# define endpoint to delete movie by id /movies/{id}
@app.delete('/movies/{id}', tags=['Movies'])
def delete_movie(id: int):
    for movie in movies:
        if movie['id'] == id:
            movies.remove(movie)
            return {'message': 'Movie deleted'}
    else:
        return {'message': 'Movie not found'}