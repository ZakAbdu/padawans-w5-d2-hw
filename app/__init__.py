from flask import Flask
from flask_smorest import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from Config import Config

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models.BookModel import BookModel
from models.MovieModel import MovieModel

from resources.movies import bp as movies_bp
api.register_blueprint(movies_bp)

from resources.books import bp as books_bp
api.register_blueprint(books_bp)
