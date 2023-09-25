from flask import render_template, request, Blueprint
from flasknotebook.models import Note

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    return render_template('home.html', title='O stronie')
