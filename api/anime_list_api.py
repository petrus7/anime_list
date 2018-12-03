from api import app
from api import db
from flask import Blueprint

from model.anime import Anime
from repository.mongo_anime_repository import AnimeRepositoryMongoDB

animes_api = Blueprint('animes_api', __name__)


@animes_api.route('/get_user')
def test():
    repo = AnimeRepositoryMongoDB(db)
    r = repo.get_best_rated()
    animu = Anime(r)
    return f'ala ma kota {repo.get_animes().count()} dsdsdsdsds {animu.on_air_period}'