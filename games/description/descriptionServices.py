from games.adapters.repository import AbstractRepository

def get_game(repo: AbstractRepository, game_id):
    games_list = repo.get_games()
    for game in games_list:
        if game.game_id == game_id:
            return game

def get_favourite_games(repo: AbstractRepository, username):
    if username is None:
        return []
    else:
        user = repo.get_user(username)

        return user.favourite_games