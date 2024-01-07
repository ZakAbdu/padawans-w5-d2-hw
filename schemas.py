from marshmallow import Schema, fields

class MovieSchema(Schema):
    id = fields.Str(dump_only=True)
    director = fields.Str(required=True)
    title = fields.Str(required=True)
    year = fields.Str(required=True)

class BookSchema(Schema):
    id = fields.Str(dump_only=True)
    author = fields.Str(required=True)
    publisher = fields.Str(required=True)
    title = fields.Str(required=True)
    year = fields.Str(required=True)