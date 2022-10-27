from flask_restx import Resource, Namespace
from container import genre_service
from dao.model.director import DirectorSchema

director_ns = Namespace('directors')
director_schema = DirectorSchema()



@director_ns.route('/')  # получить все жанры
class GenresView(Resource):
    def get(self):
        genre = genre_service.get_all()
        return director_schema.dump(genre), 200


@director_ns.route('/<int:mid>')  # получить жанр по id
class GenresView(Resource):
    def get(self, mid):
        movie = genre_service.get_one(mid)
        return director_schema.dump(movie), 200


