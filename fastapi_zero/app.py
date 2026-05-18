from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def road_root():
    return {'message': 'Olá Mundo!'}
