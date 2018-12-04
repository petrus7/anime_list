from pymongo.errors import PyMongoError

from base_exception import BaseWebException


class BasePyMongo(PyMongoError, BaseWebException):
    pass


class DBException(BasePyMongo):
    pass
