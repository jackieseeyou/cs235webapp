"""Initialize Flask app."""

from games.adapters.datareader import csvdatareader as csvreader 
from flask import Flask, render_template

# TODO: Access to the games should be implemented via the repository pattern and using blueprints, so this can not
#  stay here!


def get_games():
    csv_reader = csvreader.GameFileCSVReader("games/adapters/data/games.csv")
    csv_reader.read_csv_file()
    
    print(csv_reader.get_unique_games_count())
    return csv_reader.dataset_of_games


def create_app():
    """Construct the core application."""

    # Create the Flask app object.
    app = Flask(__name__)

    @app.route('/')
    def home():
        # Use Jinja to customize a predefined html page rendering the layout for showing a single game.
        return render_template("layout.html")
    
    @app.route('/gamePage')
    @app.route('/gamesPage/<int:page>')
    def games_page(page=1):
        per_page = 10
        start = (page - 1) * per_page
        end = start + per_page
        games = get_games()[start:end]
        total_pages = -(-len(get_games()) // per_page)
        return render_template("gamePage.html", games=games, page=page, total_pages=total_pages)
    
    @app.route('/gamesPage/<int:game_id>')
    def game_description(game_id):
        game = next((game for game in get_games() if game.game_id == game_id), None)
        if game:
            print(game)
            return render_template("gameDescription.html", game= game)
        return "Game not found", 404
    
    return app




create_app()