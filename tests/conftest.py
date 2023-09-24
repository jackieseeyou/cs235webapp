import pytest

from games import create_app

class AuthenticationManager:
    def __init__(self, client) -> None:
        self.__client = client

    def login(self, username='thorke', password='cLQ^C#oFXloS'):
        return self.__client.post(
            '/login',
            data={'username': username, 'password': password}
        )
    
    def logout(self):
            return self.__client.get('/authentication/logout')
        
    
@pytest.fixture
def client():
    my_app = create_app({
        'TESTING': True,                                # Set to True during testing.
        'WTF_CSRF_ENABLED': False                       # test_client will not send a CSRF token, so disable validation.
    })

    return my_app.test_client()


@pytest.fixture
def auth(client):
    return AuthenticationManager(client)