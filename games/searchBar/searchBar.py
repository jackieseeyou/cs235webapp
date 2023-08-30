from flask import blueprints, jsonify 
import games.adapters.repository as repo
from games.searchBar import services as services
from games.browse.browse import browse_blueprint

search_blueprint = blueprints.Blueprint(
    'search_bp', __name__)


@search_blueprint.route('/search/<query>', methods=['GET'])
def search_games(query):
    search_results = services.search_games(query, repo.repo_instance)
    return jsonify(search_results)
