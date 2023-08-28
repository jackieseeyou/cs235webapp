from bisect import insort_left
from typing import List
import os
from games.adapters.repository import AbstractRepository
from games.domainmodel.model import Game, Genre, Publisher
from games.adapters.datareader.csvdatareader import GameFileCSVReader
class MemoryRepository(AbstractRepository):
    def __init__(self):
        self.__games = list()
        self.__genres = list()
        self.__publishers = list()

    def add_game(self, game: Game):
        if isinstance(game, Game):
            insort_left(self.__games, game)

    def add_genre(self, genre: Genre):
        if isinstance(genre, Genre) and genre not in self.__genres:
            self.__genres.append(genre)

    def add_publisher(self, publisher):
        if isinstance(publisher, Publisher) and publisher not in self.__publishers:
            self.__publishers.append(publisher)

    def get_games(self) -> List[Game]:
        return self.__games

    def get_number_of_games(self):
        return len(self.__games)
    
    def get_all_genres(self):
        return self.__genres
    
    def get_number_of_genres(self):
        return len(self.__genres)
    
    def get_publishers(self):
        return self.__publishers
    
    def get_number_of_publishers(self):
        return len(self.__publishers)

def populate(repo: AbstractRepository):
    dir_name = os.path.dirname(os.path.abspath(__file__))
    games_file_name = os.path.join(dir_name, "data/games.csv")
    reader = GameFileCSVReader(games_file_name)

    reader.read_csv_file()
    games = reader.dataset_of_games

    for game in games:
        repo.add_game(game)
        for genre in game.genres:
            repo.add_genre(genre)
        repo.add_publisher(game.publisher)