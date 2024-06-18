from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fast_zero.schemas import Message

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo'}


@app.get('/OlaHtml', status_code=HTTPStatus.OK, response_class=HTMLResponse)
def read_html():
    return '''
    <HTML>
        <head>
            <title> Nosso olá mundo </title>
        </head>
        <body>
            <H1>Olá Mundo!</H1>
        </body>
    </HTML>
'''
