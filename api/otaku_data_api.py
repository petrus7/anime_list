



"""USE CASES:

- get users which gives the highest note for anime:
    - input: anime_id
    - output: user data

- get all users which finished anime
    -input: anime_id
    -output user collections


- get all animes of user
    - input: username
    - output animes collection

- get best/worst user anime
    - input user, order switch
    - output: anime data

- give anime and time spend on the longest user anime
    -input user name
    - output: anime data and time spend

- give most viewed:
    -input: none
    output: anime data of anime watched by most people



"""
import asyncio
import threading

from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from api import user_list_breaker
from api.api_exceptions import InvalidArgument
from controller.controllers_factory import AnimeFetcherFactory
from rest.async_fetch_data_rest import AsyncFetchRestData
from rest.fetch_data_rest import FetchRestData
from validators.alphanumeric_validator import IsAlphanumericValidator
import api
from concurrent.futures import FIRST_COMPLETED

otaku_app = Blueprint('otaku_api', __name__)

oatku_api = Api(otaku_app)


class GetExtremeUsers(Resource):

    def get(self):
        api.request_number += 1
        return api.request_number


class GetUserAnimes(Resource):


    @user_list_breaker
    def get(self):
        username = request.args.get('username', None)
        print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
        print(threading.active_count())
        print(threading.current_thread())
        print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
        if username is None or username == '':
            raise InvalidArgument('Not username provided')
        elif not IsAlphanumericValidator(username).validate():
            raise InvalidArgument('User name must be alphanumeric')
        # fetcher = AnimeFetcherFactory.build_rest_mongo_controller()
        asyncio.run(self.t())

        return f'alamakota!'#fetcher.get_anime_by_id_list(anime_ids)

    async def t(self):
        a = AsyncFetchRestData('http://ani_user_lists_service:5000/get_user_anime_ids', username='IronFox')
        futures = [a.a_get() for l in [1, 2, 3]]
        d, e = await asyncio.wait(futures, return_when=FIRST_COMPLETED)
        for q in d:
            print(q.result())


@otaku_app.errorhandler(InvalidArgument)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

oatku_api.add_resource(GetExtremeUsers, '/get_extreme_user')
oatku_api.add_resource(GetUserAnimes, '/get_user_animes')





