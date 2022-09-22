from sqlalchemy import Integer, String, Float
from setup_db import db

class Director(db.Model):
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


class Genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String)
    rating = db.Column(db.Float)
    title = db.Column(db.String)
    trailer = db.Column(db.String)
    year = db.Column(db.Integer)
    director_id = db.Column(db.Integer, db.ForeignKey(f"{Director.__tablename__}.id"))
    genre_id = db.Column(db.Integer, db.ForeignKey(f"{Genre.__tablename__}.id"))
    genre = db.relationship("Genre")
    director = db.relationship("Director")

