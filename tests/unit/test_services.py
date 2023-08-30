import pytest
from games.domainmodel.model import Game, Genre, Publisher
from games.adapters.memory_repository import MemoryRepository
from games.adapters.repository import AbstractRepository
from games.browse import browseServices as browseServices
from games.description import descriptionServices
from games.searchBar import searchBarServices as searchBarServices

@pytest.fixture
def test_game():
    test_game = Game(2020, "Test Game")
    test_game.add_genre(Genre("Test Genre"))
    test_game.add_genre(Genre("Test Genre 2"))
    test_game.publisher = Publisher("Test Publisher")
    return test_game


@pytest.fixture
def test_repo(test_game):
    repo = MemoryRepository()
    repo.add_game(test_game)
    return repo

# tests for getting games
def test_get_games(test_repo):
    assert test_repo.get_games()[0].title == browseServices.get_games(test_repo)[0]["title"]

# tests for getting number of games
def test_get_number_of_games(test_repo):
    assert len(browseServices.get_games(test_repo)) == 1

# tests for getting genres
def test_get_all_genres(test_repo):
    assert len(browseServices.get_genres(test_repo)) == 2

# tests for getting publishers
def test_get_publishers(test_repo):
    assert len(browseServices.get_publishers(test_repo)) == 1


# tests for getting games by genre
def test_get_games_by_genre(test_repo, test_game):
    selected_genres = ["Test Genre"]
    games = browseServices.get_games_by_genre(selected_genres, test_repo)
    assert games[0]['title'] == test_game.title


# tests for getting games by publisher
def test_get_games_by_publisher(test_repo, test_game):
    assert test_game.title == browseServices.get_games_by_publisher("Test Publisher", test_repo)[0]["title"]

# tests for getting games by genre and publisher
def test_get_games_by_genre_and_publisher(test_repo, test_game):
    selected_genres = ["Test Genre"]
    assert test_game.title == browseServices.get_games_by_genre_and_publisher(selected_genres, "Test Publisher", test_repo)[0]["title"]

# tests for getting items
def test_get_items(test_repo, test_game):
    assert test_game.title == browseServices.get_items(test_repo, 0, 1)[0]["title"]

# test for invalid genre
def test_get_games_by_invalid_genre(test_repo):
    selected_genres = ["Invalid Genre"]
    assert len(browseServices.get_games_by_genre(selected_genres, test_repo)) == 0

# test for invalid publisher
def test_get_games_by_invalid_publisher(test_repo):
    assert len(browseServices.get_games_by_publisher("Invalid Publisher", test_repo)) == 0


# test for invalid genre and publisher
def test_get_games_by_invalid_genre_and_publisher(test_repo):
    selected_genres = ["Invalid Genre"]
    assert len(browseServices.get_games_by_genre_and_publisher(selected_genres, "Invalid Publisher", test_repo)) == 0

# test for invalid offset
def test_get_items_invalid_offset(test_repo):
    assert len(browseServices.get_items(test_repo, 100, 1)) == 0

# test for invalid per_page
def test_get_items_invalid_per_page(test_repo):
    assert len(browseServices.get_items(test_repo, 0, 100)) == 1

# test for negative offset
def test_get_items_negative_offset(test_repo):
    assert len(browseServices.get_items(test_repo, -1, 1)) == 0

# test for negative per_page
def test_get_items_negative_per_page(test_repo):
    assert len(browseServices.get_items(test_repo, 0, -1)) == 0


# test for zero per_page and offset
def test_get_items_zero_per_page_and_offset(test_repo):
    assert len(browseServices.get_items(test_repo, 0, 0)) == 0

'''

Tests for descriptionServices.py

'''

# tests for getting game
def test_get_game(test_repo, test_game):
    assert descriptionServices.get_game(test_repo, 2020).title == test_game.title

# tests for getting game with invalid id
def test_get_game_invalid_id(test_repo):
    assert descriptionServices.get_game(test_repo, 1000) is None

'''
Testing for searchServices.py

'''

# tests for getting games
def test_get_games(test_repo, test_game):
    assert searchBarServices.get_games(test_repo)[0]["title"] == test_game.title

# tests for searching games
def test_search_games(test_repo, test_game):
    assert searchBarServices.search_games("test", test_repo)[0]["title"] == test_game.title

# tests for searching games with invalid query
def test_search_games_invalid_query(test_repo):
    assert len(searchBarServices.search_games("invalid", test_repo)) == 0

# tests for searching games with empty query
def test_search_games_empty_query(test_repo):
    assert len(searchBarServices.search_games("", test_repo)) == len(test_repo.get_games())

# tests for searching games with whitespace query
def test_search_games_whitespace_query(test_repo):
    assert len(searchBarServices.search_games(" ", test_repo)) == len(test_repo.get_games())