from flask import Flask, jsonify, render_template, Blueprint, request
from flask_paginate import Pagination, get_page_parameter
import games.adapters.repository as repo
from games.browse import services
browse_blueprint = Blueprint(
    'games_bp', __name__)

@browse_blueprint.route('/browse', methods=['GET'])
def browse_games():
    all_genres = services.get_genres(repo.repo_instance)
    all_publishers = services.get_publishers(repo.repo_instance)

    page = (int(request.args.get('page', 1)))
    per_page = 5
    offset = (page - 1) * per_page
    selected_genres = request.args.getlist('genres')
    selected_publisher = request.args.get('publisher')
    total_games = 0

    if selected_genres and selected_publisher:
        games = services.get_games_by_genre_and_publisher(selected_genres, selected_publisher, repo.repo_instance)[offset: offset + per_page]
        total_games = len(services.get_games_by_genre_and_publisher(selected_genres, selected_publisher, repo.repo_instance))
    elif selected_genres:
        games = services.get_games_by_genre(selected_genres, repo.repo_instance)[offset: offset + per_page]
        total_games = len(services.get_games_by_genre(selected_genres, repo.repo_instance))
    elif selected_publisher:
        games = services.get_games_by_publisher(selected_publisher, repo.repo_instance)[offset: offset + per_page]
        total_games += len(services.get_games_by_publisher(selected_publisher, repo.repo_instance))
    else:
        games = services.get_items(repo.repo_instance, offset, per_page)
        total_games = services.get_number_of_games(repo.repo_instance)
        
    pagination = Pagination(page=page, per_page=per_page, total=total_games)

    return render_template(
        'browse/browse.html', games=games, pagination=pagination, genres=all_genres, publishers=all_publishers
    )


@browse_blueprint.route('/search/<query>', methods=['GET'])
def search_games(query):
    search_results = services.search_games(query, repo.repo_instance)
    return jsonify(search_results)