# здесь бизнес логика, в виде классов или методов. сюда импортируются DAO классы из пакета dao и модели из dao.model
# некоторые методы могут оказаться просто прослойкой между dao и views,
# но чаще всего будет какая-то логика обработки данных сейчас или в будущем.

# Пример
from typing import List

from dao.genre import GenreDAO


class GenreService:

     def __init__(self, genre_dao: GenreDAO):
         self.genre_dao = genre_dao

     def get_genres(self):
         return self.genre_dao.get_all_genre()

     def get_genre_by_id(self, uid):
         return self.genre_dao.get_genre_by_id(uid)