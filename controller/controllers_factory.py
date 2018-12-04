from api import db
from controller.anime_fetcher import AnimeFetcher
from repository.mongo_anime_repository import AnimeRepositoryMongoDB


class AnimeFetcherFactory:

    @staticmethod
    def build_rest_mongo_controller():
        return AnimeFetcher(AnimeRepositoryMongoDB(db))
