from flask import Blueprint, render_template, abort, session, redirect, url_for

user_blueprint = Blueprint('user_bp', __name__)


@user_blueprint.route('/user', methods=['GET'])
def user():
    return render_template("/user/user.html")