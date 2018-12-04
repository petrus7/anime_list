from pymongo.errors import PyMongoError

from base_exception import BaseWebException


class BasePyMongo(BaseWebException, PyMongoError):
    pass


class DBException(BasePyMongo):
    pass
