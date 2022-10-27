from flask_restx import Resource, Namespace
from container import genre_service
from dao.model.genre import GenreSchema

genre_ns = Namespace('genres')
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)

@genre_ns.route('/') # получить все жанры
class GenresView(Resource):
    def get(self):
        genre = genre_service.get_all()
        return genre_schema.dump(genre), 200

@genre_ns.route('/<int:mid>') # получить жанр по id
class GenresView(Resource):
    def get(self, mid):
        movie = genre_service.get_one(mid)
        return genre_schema.dump(movie), 200


