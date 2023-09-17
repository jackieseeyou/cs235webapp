from flask import Blueprint, render_template, abort

login_blueprint = Blueprint('login_bp', __name__)
signup_blueprint = Blueprint('signup_bp', __name__)

@login_blueprint.route('/login', methods=['GET'])
def login():
    return render_template("/authentication.html", title="Log In", login=True)

@signup_blueprint.route('/signup', methods=['GET'])
def signup():
    return render_template("/authentication.html", title="Sign Up", signup=True)