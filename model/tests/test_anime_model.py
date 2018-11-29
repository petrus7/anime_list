import unittest
from datetime import datetime

proper_data = {
    'anime_id': 11013,
    'title': "Inu x Boku SS",
    'title_english': "Inu X Boku Secret Service",
    'title_synonyms': "Youko x Boku SS",
    'image_url': "https://myanimelist.cdn-dena.com/images/anime/12/35893.jpg",
    'type': "TV",
    'source': "Manga",
    'episodes': 12,
    'status': "Finished Airing",
    'airing': "False",
    'aired_string': "Jan 13, 2012 to Mar 30, 2012",
    'aired': '{"from": "2012-01-13", "to": "2012-03-30"}',
    'duration': "24 min. per ep.",
    'rating': "PG-13 - Teens 13 or older",
    'score': 7.63,
    'scored_by': 139250,
    'rank': 1274,
    'popularity': 231,
    'members': 283882,
    'favorites': 2809,
    'background': "Inu x Boku SS was licensed by Sentai Filmworks for North America, whil...",
    'premiered': "Winter 2012",
    'broadcast': "Fridays at Unknown",
    'related': "{'Adaptation': [{'mal_id': 17207, 'type': 'manga', 'url': 'https://mya...",
    'producer': "Aniplex, Square Enix, Mainichi Broadcasting System, Movic, Inu x Boku ...",
    'licensor': "Sentai Filmworks",
    'studio': "David Production",
    'genre': "Comedy, Supernatural, Romance, Shounen"
}

empty_value = {}

wrong_jsons = [
    {'{"from": "2012-01-13", "to": "2012-03-30"}'},
    {"{'from': '2012-01-13', 'to': '2012-03-30'}"},
    {'{"from": "2012_01_13", "to": "2012_03_30"}'},
]


class TestAnimeModel(unittest.TestCase):

    def test_convert_date_str(self):
        for j_data in wrong_jsons:
            a = Anime(j_data)
            self.assertEqual(a.on_air_period[0], datetime(1970, 1, 1))
            self.assertEqual(a.on_air_period[1], datetime(1970, 1, 1))
        pass



if __name__ == '__main__':
    unittest.main()