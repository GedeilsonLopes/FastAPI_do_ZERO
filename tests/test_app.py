from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_deve_retornar_ok_ola_mundo():
    client = TestClient(app)
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo'}


def test_html_deve_retornar_ok_ola_mundo():
    client = TestClient(app)
    response = client.get('/OlaHtml')
    assert response.status_code == HTTPStatus.OK
    assert response.text == '''
    <HTML>
        <head>
            <title> Nosso olá mundo </title>
        </head>
        <body>
            <H1>Olá Mundo!</H1>
        </body>
    </HTML>
'''
