from flask import Blueprint, jsonify, render_template, abort, request, session, url_for
from games.authentication.authentication import login_required
from games.description import descriptionServices
import games.adapters.repository as repo
import games.utilities.services as services
from better_profanity import profanity
from flask_wtf import FlaskForm
from wtforms import TextAreaField, HiddenField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, ValidationError, InputRequired, NumberRange

description_blueprint = Blueprint('description_bp', __name__)

@description_blueprint.route('/browse/<int:game_id>', methods=['GET'])
def description(game_id):
    game = descriptionServices.get_game(repo.repo_instance, game_id)
    if game is None:
        abort(404, description="No game was found with the given id.")
        
    return render_template("/description/description.html", game = game, add_review_url = url_for('description_bp.comment_on_game', game_id=game.game_id, game=game))

@description_blueprint.route('/browse/<int:game_id>', methods=['POST'])
@login_required
def add_to_wishlist_endpoint(game_id):
    username = session['username']
    add_to_wishlist(game_id, username, repo.repo_instance)
    return render_template("/description/description.html", game = descriptionServices.get_game(repo.repo_instance, game_id))


def add_to_wishlist(game_id, username, repo):
    """Adds a game to a user's wishlist."""
    services.add_to_wishlist(username, game_id, repo)
    
def remove_from_wishlist(game_id, username, repo):
    """Removes a game from a user's wishlist."""
    services.remove_from_wishlist(username, game_id, repo)


@description_blueprint.route('/browse/<int:game_id>/add_review', methods=['GET', 'POST'])
@login_required
def comment_on_game(game_id):
    username = session['username']
    form = CommentForm()

    if form.validate_on_submit():
        # Successful POST, i.e. the comment text has passed data validation.
        # Extract the article id, representing the commented article, from the form.

        # Use the service layer to store the new comment.
        descriptionServices.add_review(game_id, form.review.data, form.rating.data, username, repo.repo_instance)
        print("added review")

        # Retrieve the article in dict form.
        #game = descriptionServices.get_game(repo.repo_instance, game_id)

        # Cause the web browser to display the page of all articles that have the same date as the commented article,
        # and display all comments, including the new comment.
        ##don't need? return redirect(url_for('games_bp.games_by_date', date=article['release_date'], view_comments_for=game_id))



    # For a GET or an unsuccessful POST, retrieve the article to comment in dict form, and return a Web page that allows
    # the user to enter a comment. The generated Web page includes a form object.
    game = descriptionServices.get_game(repo.repo_instance, game_id)
    return render_template(
        'description/comment_on_game.html',
        game=game,
        form=form,
        handler_url=url_for('description_bp.comment_on_game', game_id=game.game_id, game=game)
    )

class ProfanityFree:
    def __init__(self, message=None):
        if not message:
            message = u'Field must not contain profanity'
        self.message = message

    def __call__(self, form, field):
        if profanity.contains_profanity(field.data):
            raise ValidationError(self.message)
class CommentForm(FlaskForm):
    rating = IntegerField('Rating (out of 5)', validators=[InputRequired(), NumberRange(min=1, max=5)])
    review = TextAreaField('Comment', [
        DataRequired(),
        Length(min=4, message='Your comment is too short'),
        ProfanityFree(message='Your comment must not contain profanity')])
    game_id = HiddenField("Game id")
    submit = SubmitField('Submit')