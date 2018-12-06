import json
import unittest

from rest.fetch_data_rest import FetchRestData, FetchDataError


class TestRestFetcher(unittest.TestCase):

    def test_succ_no_param_fetch_data(self):
        url = 'https://jsonplaceholder.typicode.com/todos/1'
        r_fetcher = FetchRestData(url)
        self.assertEqual(r_fetcher.get(),
                         json.loads('{"userId": 1, "id": 1,"title": "delectus aut autem", "completed": false}'))

    def test_succ_params_fetch_data(self):
        url = 'https://jsonplaceholder.typicode.com/comments?postId=1'
        r_fetcher = FetchRestData(url)
        self.assertEqual(r_fetcher.get()[0],
                         json.loads(r'''
                         {
                         "postId": 1,
                         "id": 1,
                         "name": "id labore ex et quam laborum",
                         "email": "Eliseo@gardner.biz",
                         "body": "laudantium enim quasi est quidem magnam voluptate ipsam eos\ntempora quo necessitatibus\ndolor quam autem quasi\nreiciendis et nam sapiente accusantium"
                         }
                         '''))

    def test_wrong_url(self):
        url = 'https://jsonplaceholder.typicode.comaaaa/comments?postId=1'
        r_fetcher = FetchRestData(url)
        self.assertRaises(FetchDataError,r_fetcher.get)


