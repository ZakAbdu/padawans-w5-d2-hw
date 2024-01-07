from flask_smorest import Blueprint

bp = Blueprint('books', __name__, description='Operation for Books', url_prefix='/book')

from . import routes