from model.anime import Anime


class AnimeAmbiqiousException(Exception):
    pass


class AnimeStorage:

    def __init__(self, anime: dict = None, animes: list = None):

        if anime and animes:
            raise AnimeAmbiqiousException("Both single value and array provided")
        elif not anime and not animes:
            self.current_anime = Anime({})
        elif anime:
            self.current_anime = Anime(anime)
        else:
            self.current_animes = [Anime(a) for a in animes]

    def get_json(self):
        if self.current_anime:
            return self.current_anime.get_json_str()
        return [anime.get_json_str() for anime in self.current_animes]