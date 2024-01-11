from flask import request
from uuid import uuid4
from flask.views import MethodView
from flask_smorest import abort

from db import books
from . import bp
from schemas import BookSchema
from models.BookModel import BookModel


@bp.route('/<book_id>')
class Book(MethodView):

    @bp.response(200, BookSchema)
    def get(self, book_id):
        book = BookModel.query.get(book_id)
        if book:
            return book
        else:
            abort(400, message='Book not found')
 

    @bp.arguments(BookSchema)
    def put(self, book_data, book_id):
        book = BookModel.query.get(book_id)
        if book:
            book.title = book_data['title']
            book.author = book_data['author']
            book.publisher = book_data['publisher']
            book.year = book_data['year']
            book.commit()
            return {'message': f"{book.title} updated"}, 202
        return {'Message': 'Invalid Book Id'}, 400
        
     
   

    def delete(self, book_id):
        book = BookModel.query.get(book_id)
        if book:
            book.delete()
            return {'Message': f"Book: {book.title} deleted"}, 202
        return {'Message': 'Invalid book'}, 400
      

@bp.route('/')
class BookList(MethodView):

    @bp.response(200, BookSchema(many=True))
    def get(self):
        return BookModel.query.all()
    
    @bp.arguments(BookSchema)
    def post(self, book_data):
        try:
            book = BookModel()
            book.title = book_data['title']
            book.author = book_data['author']
            book.publisher = book_data['publisher']
            book.year = book_data['year']
            book.commit()
            return {'Message': f"{book_data['title']} added to library"}, 201
        except:
            return {'Message': 'Invalid'}, 401
        

        
            

