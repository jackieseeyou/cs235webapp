import csv
from pathlib import Path
from datetime import date, datetime

from werkzeug.security import generate_password_hash

from games.adapters.repository import AbstractRepository
from games.domainmodel.model import Game, Genre, Publisher, ModelException

def read_csv_file(filename: str):
    with open(filename, encoding='utf-8-sig') as infile:
        reader = csv.reader(infile)

        # Read first line of the the CSV file.
        headers = next(reader)

        # Read remaining rows from the CSV file.
        for row in reader:
            # Strip any leading/trailing white space from data read.
            row = [item.strip() for item in row]
            yield row

def load_games_genres_and_publishers(data_path: Path, repo: AbstractRepository, database_mode: bool):
    genres = dict()
    
    games_filename = str(data_path / "games.csv")
    for data_row in read_csv_file(games_filename):
        game = Game(game_id = int(data_row['AppID']), game_title = data_row['Name'])
        game.release_date = data_row["Release date"]
        game.price = float(data_row["Price"])
        game.description = data_row["About the game"]
        game.image_url = data_row["Header image"]
        game.website_url = data_row["Website"]
        game.video_url = data_row["Movies"]
        game.screenshot = data_row["Screenshots"]

        publisher = Publisher(data_row["Publishers"])
        repo.add_publisher(publisher)
        game.publisher = publisher

        genre_names = data_row["Genres"].split(",")
        for genre_name in genre_names:
            genre = Genre(genre_name.strip())
            game.add_genre(genre)
            repo.add_genre(genre)
        
        repo.add_game(game)

 