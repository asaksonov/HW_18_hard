# from setup_db import db
from dao.model.models import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_all_genre(self):
        return self.session.query(Genre).all()

    def get_genre_by_id(self, uid):
        return self.session.query(Genre).filter(Genre.id == uid).one()