
from fastapi import Path, Query, APIRouter
from fastapi.responses import JSONResponse, RedirectResponse
from src.models.movie import Movie, Movie_update


# list of movies
movies: list[Movie] = []

# create api router
movie_router = APIRouter()

@movie_router.get('/', tags=['Movies'])
def get_movies() -> list[Movie]:
    content = [movie.model_dump() for movie in movies]
    return JSONResponse(content=content)

# define endpoint that return id /movies/{id}
@movie_router.get('/{id}', tags=['Movies'])
def get_movie(id: int = Path(gt=0)) -> Movie | dict[str, str]:
    for movie in movies:
        if movie.id == id:
            return JSONResponse(movie.model_dump())
    else:
        return JSONResponse(content={'message': 'Movie not found'})

# define endpoint that retrurn movie by category and year querry /movies?category=action


@movie_router.get('/movie_by_category/', tags=['Movies'])
def get_movie_by_category(category: str = Query(min_length=5, max_length=20)) -> Movie | dict[str, str]:
    for movie in movies:
        if movie.category == category:
            return movie.model_dump()
    else:
        JSONResponse({'message': 'Movie not found'})


# define endpiont to intert new movie by id /movies/{id}
@movie_router.post('/', tags=['Movies'])
def create_movie(movie: Movie) -> list[Movie]:

    movies.append(movie)
    content = [movie.model_dump() for movie in movies]
    # return JSONResponse(content=content)
    return RedirectResponse(url='/movies', status_code=303)

# define endpoint to update by body data movie by id /movies/{id}
@movie_router.put('/{id}', tags=['Movies'],status_code=200)
def update_movie(
        id: int,
        movie: Movie_update) -> list[Movie]:

    for item in movies:
        if item.id == id:
            item.title = movie.title
            item.director = movie.director
            item.category = movie.category
            item.year = movie.year
            return [movie.model_dump() for movie in movies]
    else:
        return {'message': 'Movie not found'}

# define endpoint to delete movie by id /movies/{id}


@movie_router.delete('/{id}', tags=['Movies'])
def delete_movie(id: int) -> list[Movie]| dict[str, str]:
    for movie in movies:
        if movie.id== id:
            movies.remove(movie)
            return [movie.model_dump() for movie in movies]
    else:
        return {'message': 'Movie not found'}

# define endpoint to delete all movies /movies
@movie_router.delete('/', tags=['Movies'])
def delete_all_movies() -> dict[str, str]:
    movies.clear()
    return {'message': 'All movies deleted'}