from flask import Blueprint, render_template, abort

user_blueprint = Blueprint('user_bp', __name__)

@user_blueprint.route('/user', methods=['GET'])
def user():
    return render_template("/user/user.html")