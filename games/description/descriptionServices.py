from games.adapters.repository import AbstractRepository

def get_game(repo: AbstractRepository, game_id):
    games_list = repo.get_games()
    for game in games_list:
        if game.game_id == game_id:
            return game
