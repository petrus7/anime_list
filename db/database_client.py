from pymongo import MongoClient


class DB(object):
    _instance = None
    _db_name = None

    class __DB(MongoClient):
        pass

    def __init__(self, config=None):

        if DB._instance is None:
            if config is not None:
                DB._instance = DB.__DB(config['MONGO_DB_URI'])
            else:
                raise AttributeError()

        if DB._db_name is None:
            if config is not None:
                DB._db_name = config['MONGO_DB_NAME']
            else:
                raise AttributeError()

    def db(self):
        return DB._instance[DB._db_name]

    def client(self):
        return DB._instance
