from flask import Blueprint, render_template, abort, session, redirect, url_for
from games.utilities import get_user
import games.adapters.repository as repo

user_blueprint = Blueprint('user_bp', __name__)


@user_blueprint.route('/user', methods=['GET'])
def user():
    username = session.get('username', None)
    user = get_user(username, repo.repo_instance)
    return render_template("/user/user.html", user=user)