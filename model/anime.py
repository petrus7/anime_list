import json
from datetime import datetime
from json import JSONDecodeError


class Anime:

    def __init__(self, db_anime_entity: dict):

        self.title = db_anime_entity.get('title_english') if not db_anime_entity.get('title_english') else ''
        self.episodes_count = db_anime_entity.get('episodes') if not db_anime_entity.get('episodes') else 0
        self.status = db_anime_entity.get('status') if not db_anime_entity.get('status') else ''
        self.on_air_period = self.__convert_to_time_tuple(db_anime_entity.get('aired') if not db_anime_entity.get('aired') else '')
        self.score = db_anime_entity.get('score') if not db_anime_entity.get('score') else 0.00
        self.votes_count = db_anime_entity.get('scored_by') if not db_anime_entity.get('scored_by') else 0
        self.ranking = db_anime_entity.get('rank') if not db_anime_entity.get('rank') else 0
        self.description = db_anime_entity.get('background') if not db_anime_entity.get('background') else ''
        self.genre = self.__convert_to_genre_list(db_anime_entity.get('genre') if not db_anime_entity.get('genre') else '')


    def __convert_to_time_tuple(self, timed_string):
        try:
            date_format = "%Y-%m-d"
            d = json.loads(timed_string)
            return datetime.strptime(d.get('from'), date_format), datetime.strftime(d.get('to'), date_format)
        except ValueError as e:
            print(f'cannot convert fetched value to dictionary. check format, {e}')
            return datetime(1970, 1, 1), datetime(1970, 1, 1)
        except TypeError as e:
            print(f'no date values provided {e}')
            return datetime(1970, 1, 1), datetime(1970, 1, 1)

    def __convert_to_genre_list(self, genres_str: str):
        if not genres_str:
            return []
        return genres_str.split(',')







