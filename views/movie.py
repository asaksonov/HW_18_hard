# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки). сюда импортируются сервисы из пакета service

# Пример
import flask
from flask_restx import Resource, Namespace

from dao.model.schema import MovieSchema
from implemented import movie_service

movie_ns = Namespace('directors')
movie_schema = MovieSchema(many=True)

@movie_ns.route('/')
class MovieView(Resource):
     def get(self):
         args = flask.request.args
         if len(args):
             return movie_schema.dump(
                 movie_service.get_movie_by_kwargs(**args)
             ), 200
         return movie_schema.dump(movie_service.get_movies()), 200

     def post(self):
         if movie_service.create_movie(flask.request.json):
             return 'Фильм создан', 200
         else:
             return 'Ошибка создания фильма', 200


@movie_ns.route('/<int:uid>')
class MovieViews(Resource):
     def get(self, uid):
         return movie_schema.dump([movie_service.get_movie_by_id(uid=uid)]), 200

     def delete(self, uid):
         if movie_service.delete_movie(uid):
             return 'Фильм удален', 200
         else:
             return 'Ошибка удаления фильма', 200

     def put(self, uid):
         if movie_service.update_movie(uid=uid, **flask.request.json):
             return 'Фильм обновлен', 200
         else:
             return 'Ошибка обновления фильма', 200