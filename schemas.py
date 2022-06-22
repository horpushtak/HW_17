from marshmallow import Schema, fields


class MovieSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()
    genre_id = fields.Int()
    director_id = fields.Int()
    """genre_id = fields.Int()  # Нужно ли что-то предпринимать в связи с тем, что это ForeignKey?
    "genre =  # Тут тоже грустно стало"
    director_id = fields.Int()
    "director ="""


class DirectorSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()


class GenreSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()


movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)
