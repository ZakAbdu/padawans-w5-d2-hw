from marshmallow import Schema, fields

class MovieSchema(Schema):
    id = fields.Str(dump_only=True)
    director = fields.Str(required=True)
    title = fields.Str(required=True)
    year = fields.Str(required=True)
    # user_id = fields.Str(required = True)

class BookSchema(Schema):
    id = fields.Str(dump_only=True)
    author = fields.Str(required=True)
    publisher = fields.Str(required=True)
    title = fields.Str(required=True)
    year = fields.Str(required=True)
    # user_id = fields.Str(required = True)

class UserSchema(Schema):
    id = fields.Str(dump_only = True)
    email = fields.Str(required = True)
    username = fields.Str(required = True)
    password = fields.Str(required = True, load_only = True )
    first_name = fields.Str()
    last_name = fields.Str()

class UserLogin(Schema):
  username = fields.Str(required = True)
  password = fields.Str(required = True, load_only = True )



class MovieSchemaNested(MovieSchema):
    user = fields.Nested(UserSchema, dump_only=True)

class BookSchemaNested(BookSchema):
    user = fields.Nested(UserSchema, dump_only=True)

class UserSchemaNested(UserSchema):
    movies = fields.List(fields.Nested(MovieSchema), dump_only=True)
    books = fields.List(fields.Nested(BookSchema), dump_only=True)