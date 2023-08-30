import games.adapters.repository as repo

def get_game(game_id):
    games_list = repo.repo_instance.get_games()
    for game in games_list:
        if game.game_id == game_id:
            return game
