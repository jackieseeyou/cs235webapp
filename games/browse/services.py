from games.adapters.repository import AbstractRepository
from games.domainmodel.model import Game

def get_number_of_games(repo: AbstractRepository):
    return repo.get_number_of_games()

def get_games(repo: AbstractRepository):
    games = repo.get_games()
    game_dicts = []
    for game in games:
        game_dict = {
            'game_id': game.game_id,
            'image': game.image_url,
            'title': game.title,
            'release_date': game.release_date
        }
        game_dicts.append(game_dict)
    return game_dicts

def search_games(query, repo):
    games = get_games(repo)
    filtered_games = [game for game in games if query.lower() in game['title'].lower()]
    return filtered_games

