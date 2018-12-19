import json
from datetime import datetime

from flask import jsonify


class Anime:

    def __init__(self, db_anime_entity: dict):

        self.title = db_anime_entity.get('title_english') if db_anime_entity.get('title_english') else ''
        self.episodes_count = db_anime_entity.get('episodes') if db_anime_entity.get('episodes') else 0
        self.status = db_anime_entity.get('status') if db_anime_entity.get('status') else ''
        self.score = db_anime_entity.get('score') if db_anime_entity.get('score') else 0.00
        self.votes_count = db_anime_entity.get('scored_by') if db_anime_entity.get('scored_by') else 0
        self.ranking = db_anime_entity.get('rank') if db_anime_entity.get('rank') else 0
        self.description = db_anime_entity.get('background') if db_anime_entity.get('background') else ''
        self.genre = self.__convert_to_genre_list(db_anime_entity.get('genre') if db_anime_entity.get('genre') else '')

    def __convert_to_time_tuple(self, timed_string):
        try:
            date_format = "%Y-%m-%d"
            timed_string = timed_string.replace('\'', '"')
            d = json.loads(timed_string)
            return datetime.strptime(d.get('from'), date_format), datetime.strptime(d.get('to'), date_format)
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

    def get_json_str(self):
        return json.dumps(self.__dict__)

    def to_dict(self):
        return self.__dict__


