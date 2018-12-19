import time

import aiohttp
import asyncio

class FetchDataError(Exception):
    pass


# class AsyncFetchRestData:
#
#     def __init__(self, url, headers={}, **kwargs):
#         self.url = url
#         self. headers = headers
#         self.headers.update({'content-type': 'application/json'})
#         self.query_string = dict(kwargs)
#
#     async def _a_get(self):
#         async with aiohttp.ClientSession() as session:
#             async with session.get(self.url, params=self.query_string, headers=self.headers) as response:
#                 if response.status == 200:
#                     return await response.json()
#                 else:
#                     raise FetchDataError('Cannot fetch data {}', response.status_code)
#
#     async def a_get(self):
#         try:
#             return await self._a_get()
#         except FetchDataError as e:
#             return FetchDataError('Cannot fetch data {}'.format(e), e)
#
#
#     def post(self):
#         pass

class AsyncFetchRestData:

    def __init__(self, url, headers={}, **kwargs):
        self.url = url
        self. headers = headers
        self.headers.update({'content-type': 'application/json'})
        self.query_string = dict(kwargs)

    async def _a_get(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.url, params=self.query_string, headers=self.headers) as response:
                return await response.json()


    async def a_get(self):
        start = time.time()
        print("TASK START {}".format(start))
        try:
            data = await self._a_get()
        except Exception as e:
            raise Exception('alamakota')
        end = time.time()
        print("TASK END {}".format(end))
        print("TASK DURATION {}".format(end-start))
        return data
