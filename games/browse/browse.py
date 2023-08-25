from flask import Flask, jsonify, render_template, Blueprint
import games.adapters.repository as repo
from games.browse import services
browse_blueprint = Blueprint(
    'games_bp', __name__)

@browse_blueprint.route('/browse', methods=['GET'])
def browse_games():
    num_games = services.get_number_of_games(repo.repo_instance)
    all_games = services.get_games(repo.repo_instance)
    return render_template(
        'browse/browse.html',
        title=f"Browse Games | CS235 Game Library",
        heading="Browse Games",
        games=all_games,
        num_games=num_games
    )

@browse_blueprint.route('/search/<query>', methods=['GET'])
def search_games(query):
    search_results = services.search_games(query, repo.repo_instance)
    return jsonify(search_results)