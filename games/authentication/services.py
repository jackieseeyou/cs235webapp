from games.adapters.repository import AbstractRepository
from games.domainmodel.model import User

def get_users(repo: AbstractRepository):
    return repo.get_users()

def add_user(user_name, password, repo: AbstractRepository):
    repo.add_user(User(user_name, hash(password)))