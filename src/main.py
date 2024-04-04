from fastapi import FastAPI,Path, Query, Request, Response, Depends
# response HTML
from fastapi.responses import JSONResponse, RedirectResponse
from src.routers.movie_router import movie_router
from src.util.http_error_handler import HTTPErrorHandlerMiddleware
from typing import Annotated
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os
from src.depends.comon_deps import Common_Params

# create an instance of the FastAPI class
app = FastAPI()

# app.add_middleware(HTTPErrorHandlerMiddleware)

static_path = os.path.join(os.path.dirname(__file__), 'static/')
template_path = os.path.join(os.path.dirname(__file__), 'templates/')

# mount the static files directory and templates directory
app.mount('/static', StaticFiles(directory=static_path), name='static')
templates = Jinja2Templates(directory=template_path)


# define root endpoint returns dictionary /
@app.middleware('http')
async def http_error_handler(request: Request, call_next) -> JSONResponse | Response:
    try:
        print('request:', request)
        return await call_next(request)
    except Exception as e:
        content = {'message': str(e)}
        status_code = 500
        return JSONResponse(content=content, status_code=status_code)

@app.get('/', tags=['Home'])
def home(request: Request):
    return templates.TemplateResponse('index.html', {'request': request, 'title': 'Home'})

def common_params(start_date: str, end_date: str):
    return {'start_date': start_date, 'end_date': end_date}

@app.get('/users/')
def get_users(commons: Common_Params = Depends(Common_Params)):
    return f"Users from {commons.start_date} to {commons.end_date }"

@app.get('/custumers/')
def get_users(start_date: str, end_date: str):
    return f'Users from {start_date} to {end_date}'


# include the movie_router in the app
app.include_router(prefix='/movies',router=movie_router)
