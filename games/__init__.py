"""Initialize Flask app."""

from flask import Flask, render_template
import games.adapters.repository as repo
from games.adapters.memory_repository import MemoryRepository, populate
from games.adapters.datareader.csvdatareader import GameFileCSVReader

# TODO: Access to the games should be implemented via the repository pattern and using blueprints, so this can not
#  stay here!


def create_app():
    """Construct the core application."""

    # Create the Flask app object.
    app = Flask(__name__)

    with app.app_context():
        from .browse import browse
        app.register_blueprint(browse.browse_blueprint)

        from .home import home
        app.register_blueprint(home.home_blueprint)

        from .description import description
        app.register_blueprint(description.description_blueprint)

    repo.repo_instance = MemoryRepository()
    populate(repo.repo_instance)

    
    return app