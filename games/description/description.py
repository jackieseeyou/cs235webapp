from flask import Blueprint, render_template, abort
from games.description import descriptionServices
import games.adapters.repository as repo

description_blueprint = Blueprint('description_bp', __name__)

@description_blueprint.route('/browse/<int:game_id>', methods=['GET'])

def description(game_id):
    game = descriptionServices.get_game(repo.repo_instance, game_id)
    if game is None:
        abort(404, description="No game was found with the given id.")
        
    return render_template("/description/description.html", game = game)