import logging
import os


class DevelopmentConfig(object):
    DEBUG = True
    MONGO_DB_URI = os.environ.get('MONGO_DB_URI', None)
    MONGO_DB_NAME = 'animelist'
    LOG_LEVEL = logging.DEBUG
    CORS_SUPPORTS_CREDENTIALS = True
    CORS_ORIGINS = r''
    USER_SERVICE_URL = os.environ.get('USER_SERVICE_URL', '')
    USERLIST_SERVICE_URL = os.environ.get('USERLIST_SERVICE_URL', '')
    APPS_PORT = 5000
