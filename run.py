from api import app
from api.anime_list_api import animes_api

app.register_blueprint(animes_api)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
