from api import db
from model.anime_storage import AnimeStorage
from repository.anime_repository_interface import AnimeRepositoryInterface
from pymongo.errors import PyMongoError

from repository.mongo_anime_repository import AnimeRepositoryMongoDB


class DBException(PyMongoError):

    def __init__(self, message, status_code=503, payload=None):
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


class AnimeFetcher:

    def __init__(self, repository: AnimeRepositoryInterface):
        self.repo = repository


    def get_anime_by_id(self, id):
        try:
            return AnimeStorage(anime=self.repo.get_anime_by_id(int(id))).get_json()
        except DBException as e:
            print(e)
            raise DBException(message='Something goes wrong')


class AnimeFetcherFactory:

    @staticmethod
    def build_rest_mongo_controller():
        return AnimeFetcher(AnimeRepositoryMongoDB(db))