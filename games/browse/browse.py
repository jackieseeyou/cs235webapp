from flask import Flask, jsonify, render_template, Blueprint, request
from flask_paginate import Pagination, get_page_parameter
import games.adapters.repository as repo
from games.browse import services
browse_blueprint = Blueprint(
    'games_bp', __name__)

@browse_blueprint.route('/browse', methods=['GET'])
def browse_games():
    num_games = services.get_number_of_games(repo.repo_instance)
    all_games = services.get_games(repo.repo_instance)
    all_genres = services.get_genres(repo.repo_instance)


    page = (int(request.args.get('page', 1)))
    per_page = 10
    offset = (page - 1) * per_page
    games = services.get_items(repo.repo_instance, offset, per_page)
    pagination = Pagination(page=page, per_page=per_page, total=num_games)

    return render_template(
        'browse/browse.html', games=games, pagination=pagination, genre=all_genres
    )

@browse_blueprint.route('/search/<query>', methods=['GET'])
def search_games(query):
    search_results = services.search_games(query, repo.repo_instance)
    return jsonify(search_results)