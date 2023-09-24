from games.adapters.repository import AbstractRepository
from games.authentication.services import UnknownUserException
from games.utilities import make_review

def get_game(repo: AbstractRepository, game_id):
    games_list = repo.get_games()
    for game in games_list:
        if game.game_id == game_id:
            return game

def add_review(game_id: int, review_text: str, rating: int, username: str, repo: AbstractRepository):
    # Check that the article exists.
    game = repo.get_game(game_id)

    user = repo.get_user(username)
    if user is None:
        raise UnknownUserException

    # Create comment.
    review = make_review(review_text, user, game, rating, )

    # Update the repository.
    repo.add_review(review)


def get_reviews_for_game(game_id, repo: AbstractRepository):
    game = repo.get_game(game_id)

    return reviews_to_dict(game.reviews)

def add_review(game_id: int, review_text: str, rating: int, username: str, repo: AbstractRepository):
    # Check that the article exists.
    game = repo.get_game(game_id)

    user = repo.get_user(username)
    if user is None:
        raise UnknownUserException

    # Create comment.
    review = make_review(review_text, user, game, rating, )

    # Update the repository.
    repo.add_review(review)

def get_reviews_for_game(game_id, repo: AbstractRepository):
    game = repo.get_game(game_id)

    return reviews_to_dict(game.reviews)

def get_favourite_games(repo: AbstractRepository, username):
    if username is None:
        return []
    else:
        user = repo.get_user(username)

        return user.favourite_games
    

def reviews_to_dict(reviews):
    return {
        'review_text': reviews.review_text,
        'rating': reviews.rating,
        'timestamp': reviews.timestamp,
        'username': reviews.user.username
    }