from games.adapters.repository import AbstractRepository
from games.authentication.services import UnknownUserException
from games.domainmodel.model import User

def get_users(repo: AbstractRepository):
    return repo.get_users()

def get_user(username:str, repo: AbstractRepository) -> User:
    user = repo.get_user(username)
    if user is None:
        raise UnknownUserException
    return user

