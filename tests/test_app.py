from http import HTTPStatus


def test_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')

    assert response.json() == {'message': 'Olá Mundo!'}
    assert response.status_code == HTTPStatus.OK


def test_create_user(client):
    user_data = {
        "username": "John Doe",
        "email": "johndoe@example.com",
        "password": "secret123"
    }

    response = client.post('/users/', json=user_data)

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
                'id': 1,
        'username': 'John Doe',
        'email': 'johndoe@example.com'
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'id': 1,
        'username': 'John Doe',
        'email': 'johndoe@example.com'
            }
        ]
    }
