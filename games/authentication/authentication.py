from flask import Blueprint, render_template, redirect, url_for, abort
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from password_validator import PasswordValidator

login_blueprint = Blueprint('login_bp', __name__)
signup_blueprint = Blueprint('signup_bp', __name__)

@login_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form =  LoginForm()
    return render_template("authentication/authentication.html", title="Log In", form=form)

@signup_blueprint.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()
    return render_template("authentication/authentication.html", title="Sign Up", form=form)

class PasswordValid:
    def __init__(self, message=None):
        if not message:
            message = u'Your password must be at least 8 characters, and contain an upper case letter,\
            a lower case letter and a digit'
        self.message = message

    def __call__(self, form, field):
        schema = PasswordValidator()
        schema \
            .min(8) \
            .has().uppercase() \
            .has().lowercase() \
            .has().digits()
        if not schema.validate(field.data):
            raise ValidationError(self.message)


class RegistrationForm(FlaskForm):
    user_name = StringField('Username', [
        DataRequired(message='Your user name is required'),
        Length(min=3, message='Your user name is too short')])
    password = PasswordField('Password', [
        DataRequired(message='Your password is required'),
        PasswordValid()])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    user_name = StringField('Username', [
        DataRequired(message='Your user name is required'),
    ]
    )
    password = PasswordField('Password', [
        DataRequired(message='Your password is required')
    ])
    submit = SubmitField('Log In')
