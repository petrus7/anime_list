import requests
from requests import HTTPError, RequestException


class FetchDataError(Exception):
    pass


class FetchRestData:

    def __init__(self, url, headers={}, **kwargs):
        self.url = url
        self. headers = headers
        self.headers.update({'content-type': 'application/json'})
        self.query_string = dict(kwargs)

    def get(self):
        try:
            r = requests.get(self.url, params=self.query_string, headers=self.headers)
            if r.status_code == 200:
                return r.json()
            else:
                raise FetchDataError('Cannot fetch data {}',r.status_code)
        except HTTPError as e:
            print(f'Http fault {e}')
            raise FetchDataError(f'Cannot fetch data, {e}')
        except requests.ConnectionError as e:
            print(f'Cannot connect {e}')
            raise FetchDataError(f'Cannot fetch data, {e}')
        except RequestException as e:
            print(f'Error ! {e}')
            raise FetchDataError(f'Cannot fetch data, {e}')

    def post(self):
        pass
