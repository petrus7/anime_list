



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
from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource

from api.api_exceptions import InvalidArgument
from rest.fetch_data_rest import FetchRestData

otaku_app = Blueprint('otaku_api', __name__)

oatku_api = Api(otaku_app)

class GetExtremeUsers(Resource):

    def get(self):
        anime_id = request.args.get('anime_id', None)
        if anime_id is None or anime_id == '':
            raise InvalidArgument('anime_id missing')
        anime_users = FetchRestData('http://192.168.1.107:8082/get_users_extremum_users', anime_id=anime_id).get()
        users = [ u.get('username') for u in anime_users ]
        users_d = FetchRestData('http://192.168.1.107:8081/get_user', username=users).get()
        return users_d





@otaku_app.errorhandler(InvalidArgument)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

oatku_api.add_resource(GetExtremeUsers, '/get_extreme_user')





