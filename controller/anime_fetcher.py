from pymongo.errors import PyMongoError

from controller.controllers_exceptions import DBException
from model.anime_storage import AnimeStorage
from repository.anime_repository_interface import AnimeRepositoryInterface


class AnimeFetcher:

    def __init__(self, repository: AnimeRepositoryInterface):
        self.repo = repository

    def get_anime_by_id(self, id):
        try:
            return AnimeStorage(anime=self.repo.get_anime_by_id(int(id))).get_json()
        except PyMongoError as e:
            print(e)
            raise DBException(message='Something goes wrong')

    def get_anime_by_id_list(self, id_list):
        try:
            return AnimeStorage(animes=self.repo.get_anime_by_id_list(id_list)).get_json()
        except PyMongoError as e:
            print(e)
            raise DBException(message='Something goes wrong')