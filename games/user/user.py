from flask import Blueprint, render_template, abort, session, redirect, url_for
import games.adapters.repository as repo
from games.utilities import get_user
from games.authentication.authentication import login_required

user_blueprint = Blueprint('user_bp', __name__)



@user_blueprint.route('/profile', methods=['GET'])
@login_required
def user():
    username = session['username']
    username = username.lower().strip()
    user = get_user(username, repo.repo_instance)
    return render_template("/user/user.html", user=user)