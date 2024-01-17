from datetime import datetime

from app import db

from werkzeug.security import generate_password_hash, check_password_hash

followers = db.Table( 'followers',
  db.Column('follower_id', db.Integer, db.ForeignKey('users.id')),
  db.Column('followed_id', db.Integer, db.ForeignKey('users.id'))  
)

class UserModel(db.Model):

  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key = True)
  username = db.Column(db.String(50), nullable = False, unique = True)
  email = db.Column(db.String(75), nullable = False, unique = True)
  password_hash = db.Column(db.String(250), nullable = False )
  first_name = db.Column(db.String(30))
  last_name = db.Column(db.String(30))
  followed = db.relationship('UserModel',
                            secondary = 'followers',
                            primaryjoin = followers.c.follower_id == id,
                            secondaryjoin = followers.c.followed_id == id,
                            backref = db.backref('followers', lazy = 'dynamic')
                            )
  movies = db.relationship('MovieModel', back_populates = 'user', lazy = 'dynamic', cascade = 'all, delete')
  books = db.relationship('BookModel', back_populates = 'user', lazy = 'dynamic', cascade = 'all, delete')
  
  def __repr__(self):
    return f'<User: {self.username}>'

  def commit(self):
    db.session.add(self)
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def from_dict(self, user_dict):
    for k, v in user_dict.items():
      if k != 'password':
        setattr(self, k, v)
      else:
        setattr(self, 'password_hash', generate_password_hash(v))
        # self.password_hash = v

  def check_password(self, password):
    return check_password_hash(self.password_hash, password)

  def is_following(self, user):
    return user in self.followed
  
  def follow(self, user):
    if self.is_following(user):
      return
    self.followed.append(user)

  def unfollow(self,user):
    if not self.is_following(user):
      return
    self.followed.remove(user)


class MovieModel(db.Model):

    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key = True)
    director = db.Column(db.String(110), nullable = False)
    title = db.Column(db.String(110), nullable = False)
    year = db.Column(db.String(4), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    user = db.relationship('UserModel', back_populates = 'movies')

    
    def __repr__(self):
        return f"<Movie: {self.title} - {self.year}"
    
    def commit(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

class BookModel(db.Model):

    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key = True)
    author = db.Column(db.String(110), nullable = False)
    publisher = db.Column(db.String(110), nullable = False)
    title = db.Column(db.String(110), nullable = False)
    year = db.Column(db.String(4), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    user = db.relationship('UserModel', back_populates = 'books')

    def __repr__(self):
        return f"<Book: {self.title} - {self.author}"
    
    def commit(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()