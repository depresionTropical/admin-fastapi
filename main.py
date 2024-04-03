from fastapi import FastAPI


app = FastAPI()

@app.get('/', tags=['Home'])
def home():
    return {'message': 'Welcome to the API'}

@app.get('/movies', tags=['Home'])
def home():
    return {'message': 'Welcome to the Home page'}

