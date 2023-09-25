from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flasknotebook.config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'


from flasknotebook.users.routes import users
from flasknotebook.notes.routes import notes
from flasknotebook.main.routes import main
from flasknotebook.errors.handlers import errors

app.register_blueprint(users)
app.register_blueprint(notes)
app.register_blueprint(main)
app.register_blueprint(errors)
