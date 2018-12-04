from controller.controllers_exceptions import DBException
from model.anime_storage import AnimeStorage
from repository.anime_repository_interface import AnimeRepositoryInterface





class AnimeFetcher:

    def __init__(self, repository: AnimeRepositoryInterface):
        self.repo = repository

    def get_anime_by_id(self, id):
        try:
            with self.repo as r:
                return AnimeStorage(anime=r.get_anime_by_id(int(id))).get_json()
        except DBException as e:
            print(e)
            raise DBException(message='Something goes wrong')

