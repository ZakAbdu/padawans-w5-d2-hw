from flask import request
from uuid import uuid4
from flask.views import MethodView
from flask_smorest import abort
from flask_jwt_extended import jwt_required, get_jwt_identity

from . import bp
from schemas import BookSchema, BookSchemaNested
from models.UserModel import BookModel


@bp.route('/<book_id>')
class Book(MethodView):

    @bp.response(200, BookSchemaNested)
    def get(self, book_id):
        book = BookModel.query.get(book_id)
        if book:
            return book
        else:
            abort(400, message='Book not found')
 
    @jwt_required()
    @bp.arguments(BookSchema)
    def put(self, book_data, book_id):
        book = BookModel.query.get(book_id)
        if book and book.user_id == get_jwt_identity():
            book.title = book_data['title']
            book.author = book_data['author']
            book.publisher = book_data['publisher']
            book.year = book_data['year']
            book.commit()
            return {'message': f"{book.title} updated"}, 202
        return {'Message': 'Invalid Book Id'}, 400
        
     
    @jwt_required()
    def delete(self, book_id):
        book = BookModel.query.get(book_id)
        if book and book.user_id == get_jwt_identity():
            book.delete()
            return {'Message': f"Book: {book.title} deleted"}, 202
        return {'Message': 'Invalid book'}, 400
      

@bp.route('/')
class BookList(MethodView):

    @bp.response(200, BookSchema(many=True))
    def get(self):
        return BookModel.query.all()
    
    @jwt_required()
    @bp.arguments(BookSchema)
    def post(self, book_data):
        try:
            book = BookModel()
            book.user_id = get_jwt_identity()
            book.title = book_data['title']
            book.author = book_data['author']
            book.publisher = book_data['publisher']
            book.year = book_data['year']
            book.commit()
            return {'Message': f"{book_data['title']} added to library"}, 201
        except:
            return {'Message': 'Invalid'}, 401
        

        
            

