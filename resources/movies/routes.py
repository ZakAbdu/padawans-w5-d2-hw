from flask import request
from uuid import uuid4
from flask.views import MethodView

from db import movies
from . import bp
from schemas import MovieSchema


@bp.route('/<movie_id>')
class Movie(MethodView):

    @bp.response(200, MovieSchema)
    def get(self, movie_id):
        try:
            return movies[movie_id]
        except KeyError:
            return {'message': "Invalid Movie Id"}, 400
    
    @bp.arguments(MovieSchema)
    def put(self, movie_data, movie_id):
        try:
            movie = movies[movie_id]
            movie_data = request.get_json()
            movie |= movie_data
            return { 'message': f'{movie["title"]} updated' }, 202
        except KeyError:
            return { 'message': 'Invalid Movie' }, 400
    
    def delete(self, movie_id):
        try:
            del movies[movie_id]
            return {"message": "Movie Deleted"}, 202
        except:
            return {"message": "Invalid Movie"}, 400


@bp.route('/')
class MovieList(MethodView):

    @bp.response(200, MovieSchema(many=True))
    def get(self):
        return list(movies.values())
    
    @bp.arguments(MovieSchema)
    def post(self, movie_data):
        movies[uuid4()] = movie_data
        return { 'message': f'Movie: {movie_data["title"]} added to movies list' }, 201


