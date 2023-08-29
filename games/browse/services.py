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
            'release_date': game.release_date,
            'price': game.price,
            'genres': [genre.genre_name for genre in game.genres],
            'publisher': game.publisher.publisher_name
        }
        game_dicts.append(game_dict)
    return game_dicts

def get_items(repo, offset, per_page):
    games = get_games(repo)
    return games[offset: offset + per_page]

def search_games(query, repo):
    games = get_games(repo)
    filtered_games = [game for game in games if query.lower() in game['title'].lower()]
    return filtered_games

def get_game(game_id, repo):
    game = repo.get_game(game_id)
    if game is None:
        return None
    return game

def get_genres(repo):
    genres = repo.get_all_genres()
    return genres

def get_publishers(repo):
    publishers = repo.get_publishers()
    return publishers

def get_games_by_genre(selected_genres, repo):
    games = get_games(repo)
    filtered_games = [game for game in games if any(genre in selected_genres for genre in game['genres'])]

    return filtered_games
