from flask import request
from flask_restful import Resource
from api import settings


class GenreListResource(Resource):
    def get(self):
        genres = ["reggae", "rock"]
        return genres
