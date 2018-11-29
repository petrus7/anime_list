import logging
from logging.handlers import RotatingFileHandler

from flask import Flask


class AnimeListServiceFlask(Flask):
    pass


def create_app(config_class):
    app = AnimeListServiceFlask(__name__, static_url_path='')

    # Configuration
    app.config.from_object(f'config.{config_class}')

    file_handler = RotatingFileHandler(filename='app.log', maxBytes=1024*1024)
    file_handler.setLevel(app.config['LOG_LEVEL'])

    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(app.config['LOG_LEVEL'])

    # CORS(app)
    return app