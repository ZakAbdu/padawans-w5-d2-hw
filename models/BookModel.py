from app import db

class BookModel(db.Model):

    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key = True)
    author = db.Column(db.String(110), nullable = False)
    publisher = db.Column(db.String(110), nullable = False)
    title = db.Column(db.String(110), nullable = False)
    year = db.Column(db.String(4), nullable = False)

    def __repr__(self):
        return f"<Book: {self.title} - {self.author}"
    
    def commit(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

