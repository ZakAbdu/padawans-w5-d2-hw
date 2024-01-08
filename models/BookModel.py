from app import db

class BookModel(db.Model):

    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key = True)
    author = db.Column(db.String(100), nullable = False)
    publisher = db.Column(db.String(100), nullable = False)
    title = db.Column(db.String(100), nullable = False)
    year = db.Column(db.String(4), nullable = False)