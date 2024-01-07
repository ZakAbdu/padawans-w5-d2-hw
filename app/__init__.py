from flask import Flask
from flask_smorest import Api
from Config import Config

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)

from resources.movies import bp as movies_bp
api.register_blueprint(movies_bp)

from resources.books import bp as books_bp
api.register_blueprint(books_bp)
