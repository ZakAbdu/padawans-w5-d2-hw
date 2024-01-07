from flask import request
from uuid import uuid4
from flask.views import MethodView

from db import books
from . import bp
from schemas import BookSchema


@bp.route('/<book_id>')
class Book(MethodView):

    @bp.response(200, BookSchema)
    def get(self, book_id):
        try:
            return books[book_id]
        except KeyError:
            return {'message': "Invalid Book Id"}, 400
    
    @bp.arguments(BookSchema)
    def put(self, book_data, book_id):
        try:
            book = books[book_id]
            book_data = request.get_json()
            book |= book_data
            return { 'message': f'{book["title"]} updated' }, 202
        except KeyError:
            return {"message": "Invalid Book"}, 400
    
    def delete(self, book_id):
        try:
            del books[book_id]
            return {"message": "Book Deleted"}, 202
        except:
            return {"message": "Invalid Book"}, 400

@bp.route('/')
class BookList(MethodView):

    @bp.response(200, BookSchema(many=True))
    def get(self):
        return list(books.values())
    
    @bp.arguments(BookSchema)
    def post(self, book_data):
        books[uuid4()] = book_data
        return { 'message': f'Book: {book_data["title"]} added to books list' }, 201
        
            

