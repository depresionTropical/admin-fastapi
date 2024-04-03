from fastapi import FastAPI,Path, Query
# response HTML
from fastapi.responses import HTMLResponse
# import model data
from Models.movie import Movie, Movie_update

# create an instance of the FastAPI class
app = FastAPI()

# list of movies
movies: list[Movie] = []

# define root endpoint returns dictionary /


@app.get('/', tags=['Home'])
def home():
    return {'message': 'Welcome to the API'}

# define endpoint that returns a list of movies /movies


@app.get('/movies', tags=['Movies'])
def get_movies() -> list[Movie]:
    return [movie.model_dump() for movie in movies]

# define endpoint that return id /movies/{id}


@app.get('/movies/{id}', tags=['Movies'])
def get_movie(id: int = Path(gt=0)) -> Movie | dict[str, str]:
    for movie in movies:
        if movie.id == id:
            return movie.model_dump()
    else:
        return {'message': 'Movie not found'}

# define endpoint that retrurn movie by category and year querry /movies?category=action


@app.get('/movies/', tags=['Movies'])
def get_movie_by_category(category: str = Query(min_length=5, max_length=20)) -> Movie | dict[str, str]:
    for movie in movies:
        if movie.category == category:
            return movie.model_dump()
    else:
        return {'message': 'Movie not found'}


# define endpiont to intert new movie by id /movies/{id}
@app.post('/movies/', tags=['Movies'])
def create_movie(movie: Movie) -> list[Movie]:

    movies.append(movie)
    return [movie.model_dump() for movie in movies]


# define endpoint to update by body data movie by id /movies/{id}
@app.put('/movies/{id}', tags=['Movies'])
def update_movie(
        id: int,
        movie: Movie_update) -> list[Movie]:

    for item in movies:
        if item['id'] == id:
            item['title'] = movie.title
            item['director'] = movie.director
            item['category'] = movie.category
            item['year'] = movie.year
            return [movie.model_dump() for movie in movies]
    else:
        return {'message': 'Movie not found'}

# define endpoint to delete movie by id /movies/{id}


@app.delete('/movies/{id}', tags=['Movies'])
def delete_movie(id: int) -> list[Movie]:
    for movie in movies:
        if movie['id'] == id:
            movies.remove(movie)
            return [movie.model_dump() for movie in movies]
    else:
        return {'message': 'Movie not found'}
