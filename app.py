from flask import Flask, request
from uuid import uuid4

app = Flask(__name__)

movies = {
    '1': {
        'title': 'Batman The Dark Knight',
        'year': '2008',
        'director': 'Christopher Nolan'
    },
    '2': {
        'title': 'The Pursuit of Happyness',
        'year': '2006',
        'director': 'Gabriele Muccino'
    },
    '3': {
        'title': 'Django Unchained',
        'year': '2012',
        'director': 'Quentin Tarantino'
    }
}


books = {
    '1': {
        'title': 'The Catcher in the Rye',
        'author': 'J.D. Salinger',
        'publisher': 'Little, Brown and Company',
        'year': '1951'
    },
    '2': {
        'title': 'The Hunger Games',
        'author': 'Suzanne Collins',
        'publisher': 'Scholastic',
        'year': '2008'
    },
    '3': {
        'title': 'To Kill a Mockingbird',
        'author': 'Harper Lee',
        'publisher': 'Harper-Collins',
        'year': '1960'
    }
}



@app.route('/')
def hello():
    return '<h1>Hellon<h1>'

# Read
@app.get('/movie')
def get_movies():
    return { 'movies': list(movies.values()) }


# Create
@app.post('/movie')
def create_movie():
    movie_data = request.get_json()
    movies[uuid4()] = movie_data
    return { 'message': f'Movie: {movie_data["title"]} added to movies list' }, 201

# Update
@app.put('/movie/<movie_id>')
def update_movie(movie_id):
    try:
        movie = movies[movie_id]
        movie_data = request.get_json()
        movie |= movie_data
        return { 'message': f'{movie["title"]} updated' }, 202
    except KeyError:
        return { 'message': 'Invalid Movie' }, 400

# Delete
@app.delete('/movie/<movie_id>')
def delete_movie(movie_id):
    if movie_id in movies:
        movie = movies[movie_id]
        del movies[movie_id]
        return { 'message': f'{movie["title"]} has been deleted' }, 201
    else:
        return { 'message': 'Movie not found' }, 400


# ------- BOOKS -------

# Read
@app.get('/book')
def get_books():
    return { 'books': list(books.values()) }


# Create
@app.post('/book')
def create_book():
    book_data = request.get_json()
    books[uuid4()] = book_data
    return { 'message': f'Book: {book_data["title"]} added to library' }, 201

# Update
@app.put('/book/<book_id>')
def update_book(book_id):
    try:
        book = books[book_id]
        book_data = request.get_json()
        book |= book_data
        return { 'message': 'Book has been updated' }, 202
    except KeyError:
        return { 'message': 'Invalid book id given' }

# Delete
@app.delete('/book/<book_id>')
def delete_book(book_id):
    if book_id in books:
        book = books[book_id]
        del books[book_id]
        return { 'message': f'{book["title"]} has been deleted' }, 201
    else:
        return { 'message': 'Book not found' }


