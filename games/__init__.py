"""Initialize Flask app."""

from flask import Flask
import games.adapters.repository as repo
from games.adapters.memory_repository import MemoryRepository, populate
from dotenv import load_dotenv
import os


def create_app(test_config=None):
    """Construct the core application."""

    load_dotenv()
    # Create the Flask app object.
    app = Flask(__name__)

    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
    app.config['WTF_CSRF_SECRET_KEY'] = os.environ.get('WTF_CSRF_SECRET_KEY')



    with app.app_context():
        from .browse import browse
        app.register_blueprint(browse.browse_blueprint)

        from .home import home
        app.register_blueprint(home.home_blueprint)

        from .description import description
        app.register_blueprint(description.description_blueprint)

        from .searchBar import searchBar
        app.register_blueprint(searchBar.search_blueprint)

        from .user import user
        app.register_blueprint(user.user_blueprint)

        from .authentication import authentication
        app.register_blueprint(authentication.login_blueprint)
        app.register_blueprint(authentication.signup_blueprint)
        app.register_blueprint(authentication.logout_blueprint)
    repo.repo_instance = MemoryRepository()
    populate(repo.repo_instance)

    
    return app