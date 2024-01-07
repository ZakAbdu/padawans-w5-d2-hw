from flask_smorest import Blueprint

bp = Blueprint('movies', __name__, description='Operation for Movies', url_prefix='/movie')

from . import routes