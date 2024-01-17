from flask import request
from uuid import uuid4
from flask.views import MethodView
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_smorest import abort

from . import bp
from schemas import MovieSchema, MovieSchemaNested
from models.UserModel import MovieModel


@bp.route('/<movie_id>')
class Movie(MethodView):

    @bp.response(200, MovieSchemaNested)
    def get(self, movie_id):
        movie = MovieModel.query.get(movie_id)
        if movie:
            return movie
        else:
            abort(400, message='Movie not found')
       
    @jwt_required()
    @bp.arguments(MovieSchema)
    def put(self, movie_data, movie_id):
        print('in route')
        movie = MovieModel.query.get(movie_id)
        if movie and movie.user_id == get_jwt_identity():
            movie.title = movie_data['title']
            movie.director = movie_data['director']
            movie.year = movie_data['year']
            movie.commit()
            return {'message': f"{movie.title} updated"}, 202
        return {'Message': 'Invalid Movie Id'}, 400
      
    @jwt_required()
    def delete(self, movie_id):
        movie = MovieModel.query.get(movie_id)
        if movie and movie.user_id == get_jwt_identity():
            movie.delete()
            return {"Message": 'Movie Deleted From Library'}, 202
        return {"Message": 'Invalid Movie'}, 400
      

@bp.route('/')
class MovieList(MethodView):

    @bp.response(200, MovieSchema(many=True))
    def get(self):
        return MovieModel.query.all()
    
    @jwt_required()
    @bp.arguments(MovieSchema)
    def post(self, movie_data):
        try:
            movie = MovieModel()
            movie.user_id = get_jwt_identity()
            movie.title = movie_data['title']
            movie.director = movie_data['director']
            movie.year = movie_data['year']
            movie.commit()
            return {'Message': "Movie added to library"}, 201
        except:
            return {'Message': 'Invalid'}, 401
       