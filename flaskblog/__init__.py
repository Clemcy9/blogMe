# from enum import unique
from flask import Flask
# from sqlalchemy.orm import backref
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'c5b581ae872c7b70c4fc6b018ea74134'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:mechatronic@localhost/web1'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from flaskblog import route