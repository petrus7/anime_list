from random import randint

from repository.anime_repository_interface import AnimeRepositoryInterface


class ImproperQueryParameters(Exception):
    pass


class AnimeRepositoryMongoDB(AnimeRepositoryInterface):

    def __init__(self, db):
        super(AnimeRepositoryMongoDB, self).__init__(db)
        self.animes = self._db.db().animes

    def get_animes_sorted(self, sort_attribute, reverse=False, page=None, on_page_count=None):
        sort_order = -1 if reverse else 1
        return self.get_animes(page=page, on_page_count=on_page_count).sort(sort_attribute, sort_order)

    def get_animes_filtered(self, attribute, value, page=None, on_page_count=None):
        return self.__page(self.animes.find({attribute: {"$eq": value}}), page, on_page_count)

    def get_animes_filtered_sorted(self, attribute, value, sort_attribute, reverse=False, page=None,
                                   on_page_count=None):
        sort_order = -1 if reverse else 1
        c = self.animes.find({attribute: {"$eq": value}}).sort(sort_attribute, sort_order)
        return self.__page(c, page, on_page_count)

    def get_random_from_genre(self, genre):
        self.animes.create_index([('genre', 'text')])
        filtered_cursor = self.animes.find({'$text': {'$search': genre}})
        count = filtered_cursor.count()
        chosen = randint(0, count - 1)
        return filtered_cursor[chosen]

    def get_best_rated(self, genre=None):
        try:
            return self.animes.find().sort('rank', 1)[0]
        except StopIteration as e:
            print(f'No entities found {e}')
            return {}

    def get_anime_by_id(self, anime_id):
        return self.animes.find_one({'anime_id': anime_id})

    def get_anime_by_id_list(self, anime_id_list):
        return self.animes.find({'anime_id': {'$in': anime_id_list}})

    def get_animes(self, page=None, on_page_count=None):

        return self.__page(self.animes.find(), page, on_page_count)

    def __page(self, cursor, page, on_page_count):
        if page is None and on_page_count is None:
            return cursor
        elif page is None and on_page_count is not None:
            return cursor.limit(on_page_count)
        elif page is not None and on_page_count is None:
            raise ImproperQueryParameters('Add on_page_count param to allow skipping')
        elif page < 0 or on_page_count <= 0:
            raise ImproperQueryParameters('page count must be >= 0   on_page_count must be > 0')
        else:
            return cursor.skip(page * on_page_count).limit(on_page_count)
