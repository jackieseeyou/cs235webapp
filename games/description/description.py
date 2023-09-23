from flask import Blueprint, jsonify, redirect, render_template, abort, request, session
from games.authentication.authentication import login_required
from games.description import descriptionServices
import games.adapters.repository as repo
import games.utilities as utilities

description_blueprint = Blueprint('description_bp', __name__)

@description_blueprint.route('/browse/<int:game_id>', methods=['GET'])
def description(game_id):
    game = descriptionServices.get_game(repo.repo_instance, game_id)
    if game is None:
        abort(404, description="No game was found with the given id.")
        
    return render_template("/description/description.html", game = game,
                           favourite_games = descriptionServices.get_favourite_games(repo.repo_instance, session['username'])
    )  

@description_blueprint.route('/browse/<int:game_id>', methods=['POST'])
@login_required
def add_to_wishlist_endpoint(game_id):
    username = session['username']
    utilities.add_to_wishlist(username, game_id, repo.repo_instance)
    return render_template("/description/description.html", 
                           game = descriptionServices.get_game(repo.repo_instance, game_id),
                           user = utilities.get_user(username, repo.repo_instance) 
                           )


@description_blueprint.route('/browse/<int:game_id>', methods=['POST'])
@login_required
def remove_from_wishlist_endpoint(game_id):
    username = session['username']
    utilities.remove_from_wishlist(username, game_id, repo.repo_instance)
    return render_template("/description/description.html", 
                           game = descriptionServices.get_game(repo.repo_instance, game_id),
                           user = utilities.get_user(username, repo.repo_instance) 
                           )

