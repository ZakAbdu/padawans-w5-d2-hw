from app import db

class MovieModel(db.Model):

    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key = True)
    director = db.Column(db.String(110), nullable = False)
    title = db.Column(db.String(110), nullable = False)
    year = db.Column(db.String(4), nullable = False)

    
    def __repr__(self):
        return f"<Movie: {self.title} - {self.year}"
    
    def commit(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    