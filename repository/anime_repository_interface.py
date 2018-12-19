import abc


class AnimeRepositoryInterface(abc.ABC):

    def __init__(self, db):
        self._db = db

    @abc.abstractmethod
    def get_animes(self, page=None, on_page_count=None):
        pass

    @abc.abstractmethod
    def get_animes_sorted(self, sort_attribute, reverse=False, page=None, on_page_count=None):
        pass

    @abc.abstractmethod
    def get_animes_filtered(self, attribute, value, page=None, on_page_count=None):
        pass

    @abc.abstractmethod
    def get_animes_filtered_sorted(self, attribute, value, sort_attribute, reverse=False, page=None, on_page_count=None):
        pass

    @abc.abstractmethod
    def get_random_from_genre(self, genre):
        pass

    @abc.abstractmethod
    def get_best_rated(self, genre=None):
        pass

    @abc.abstractmethod
    def get_anime_by_id(self, anime_id):
        pass

    @abc.abstractmethod
    def get_anime_by_id_list(self, anime_id_list):
        pass
