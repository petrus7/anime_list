import unittest

from api import db
from repository.mongo_anime_repository import AnimeRepositoryMongoDB


class TestMongoRepository(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.repo = AnimeRepositoryMongoDB(db)

    @classmethod
    def tearDownClass(cls):
        cls.repo._db.client().close()

    def test_get_anime_by_id(self):
        a = self.repo.get_anime_by_id(11013)
        self.assertEqual(a.get('anime_id'), 11013)

    def test_get_best_rated(self):
        a = self.repo.get_best_rated()
        self.assertIsNotNone(a)

    def test_animes(self):
        anime_count = 14478
        self.assertEqual(self.repo.get_animes().count(), anime_count)

    def test_paged(self):
        paged = list(self.repo.get_animes(page=1, on_page_count=10))
        self.assertEqual(len(paged), 10)

    def test_get_animes_sorted(self):
        a = self.repo.get_animes_sorted('anime_id')[0]
        self.assertEqual(a.get('anime_id'), 1)

    def test_animes_filtered(self):
        self.assertEqual(self.repo.get_animes_filtered(attribute='genre', value='fake_genre').count(), 0)
        self.assertNotEqual(self.repo.get_animes_filtered(attribute='genre', value='Hentai').count(), 0)
        self.assertGreater(self.repo.get_animes().count(), self.repo.get_animes_filtered(attribute='genre', value='Hentai').count())

    def test_animes_filtered_sorted(self):
        a = self.repo.get_animes_filtered_sorted('genre','Hentai','anime_id')[0]
        self.assertEqual(a.get('anime_id'), 211)

    def test_random_from_genre(self):
        self.assertIsNotNone(self.repo.get_random_from_genre('Hentai'))
