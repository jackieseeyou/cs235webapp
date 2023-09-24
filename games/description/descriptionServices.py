from games.adapters.repository import AbstractRepository

def get_game(repo: AbstractRepository, game_id):
    games_list = repo.get_games()
    for game in games_list:
        if game.game_id == game_id:
            return game

def add_review(game_id: int, review_text: str, rating: int, username: str, repo: AbstractRepository):
    # Check that the article exists.
    game = repo.get_game(game_id)
    if game is None:
        raise NonExistentGameException

    user = repo.get_user(username)
    if user is None:
        raise UnknownUserException

    # Create comment.
    review = make_review(review_text, user, game, rating, )

    # Update the repository.
    repo.add_review(review)

def get_reviews_for_game(game_id, repo: AbstractRepository):
    game = repo.get_game(game_id)

    if game is None:
        raise NonExistentGameException

    return reviews_to_dict(game.reviews)
