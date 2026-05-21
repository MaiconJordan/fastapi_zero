from fastapi import FastAPI
from http import HTTPStatus
from fastapi_zero.schemas import Message


app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def road_root():
    return {'message': 'Olá Mundo!'}
