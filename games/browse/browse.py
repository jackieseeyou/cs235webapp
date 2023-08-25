from flask import Flask, jsonify, render_template, Blueprint
import games.adapters.repository as repo
from games.browse import services
browse_blueprint = Blueprint(
    'games_bp', __name__)

PER_PAGE = 10

browse_blueprint.route('/browse', defaults={'page': 1})
@browse_blueprint.route('/browse/page/<int:page>')
def browse_games(page):
    offset = (page - 1) * PER_PAGE
    games = services.get_games(offset, PER_PAGE, repo.repo_instance)
    total_games = services.get_number_of_games(repo.repo_instance)
    
    return render_template(
        'browse/browse.html',
        games=games,
        page=page,
        total_pages=(total_games + PER_PAGE - 1) // PER_PAGE
    )


@browse_blueprint.route('/search/<query>', methods=['GET'])
def search_games(query):
    search_results = services.search_games(query, repo.repo_instance)
    return jsonify(search_results)