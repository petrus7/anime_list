from model.anime import Anime


class AnimeAmbiqiousException(Exception):
    pass


class AnimeStorage:

    def __init__(self, anime: dict = None, animes: list = None):
        if anime and animes:
            raise AnimeAmbiqiousException("Both single value and array provided")
        elif anime:
            self.current_anime = Anime(anime)
        else:
            self.current_animes = [Anime(a) for a in animes]

