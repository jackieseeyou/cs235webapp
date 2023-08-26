from flask import Blueprint, render_template
from games.description import services

description_blueprint = Blueprint('description_bp', __name__)

@description_blueprint.route('/browse/<int:game_id>', methods=['GET'])

def description(game_id):
    game = services.get_game(game_id)
    return render_template("/description/description.html", game = game)