from flask import Blueprint, jsonify
from flask_restful import Api, Resource
from flask import request

from controller.anime_fetcher import DBException, AnimeFetcherFactory

animes_api = Blueprint('animes_api', __name__)

api = Api(animes_api)

class InvalidArgument(Exception):

    def __init__(self, message, status_code=400, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        rv['code'] = self.status_code
        return rv


class GetAnimes(Resource):

    def get(self):
        return f'ala ma kota!'


class GetAnimeById(Resource):

    def get(self):
        _id = self.__get_valid_id(dict(request.args))
        a = AnimeFetcherFactory.build_rest_mongo_controller().get_anime_by_id(_id)
        return f'ala ma kota! o id {a}'

    def __get_valid_id(self, request_dict):
        if not request_dict.get('id', None):
            raise InvalidArgument('No id provided')
        elif not request_dict.get('id').isdigit():
            raise InvalidArgument('Id must be digit')
        return request_dict.get('id')


@animes_api.errorhandler(DBException)
@animes_api.errorhandler(InvalidArgument)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

api.add_resource(GetAnimes, '/get_animes')
api.add_resource(GetAnimeById, '/get_anime_by_id')


