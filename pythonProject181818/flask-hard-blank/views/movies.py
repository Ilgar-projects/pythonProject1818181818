from flask_restx import Resource, Namespace

from container import movie_service
from dao.model.movie import MovieSchema

movie_ns = Namespace('movies')
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/') # получить все фильмы
class MoviesView(Resource):
    def get(self):
        movies = movie_service.get_all()
        return movies_schema.dump(movies), 200

    def post(self, mov):
        movie = movie_service.create(mov)
        return movie_schema.dumps(movie), 200

@movie_ns.route('/<int:mid>') # получить фильм по id
class MoviesView(Resource):
    def get(self, mid):
        movie = movie_service.get_one(mid)
        return movie_schema.dump(movie), 200

    def put(self, data):
        movie = movie_service.update(data)
        return movie_schema.dump(movie), 200

    def delete(self,did):
        movie = movie_service.delete(did)
        return movie_schema.dump(movie), 200

@movie_ns.route('/director/<int:did>') # получить все фильмы режиссёра
class MoviesView(Resource):
    def get(self, did):
        movie = movie_service.get_by_director(did)
        return movie_schema.dump(movie), 200

@movie_ns.route('/genre/<int:gid>') # получить все фильмы жанра
class MoviesView(Resource):
    def get(self, gid):
        movie = movie_service.get_by_genre(gid)
        return movie_schema.dump(movie), 200

@movie_ns.route('/year/<int:yid>') # получить все фильмы за год
class MoviesView(Resource):
    def get(self, yid):
        movie = movie_service.get_by_year(yid)
        return movie_schema.dump(movie), 200
