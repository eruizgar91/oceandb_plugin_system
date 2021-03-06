from pymongo import MongoClient

_DB_INSTANCE = None


def get_database_instance(config_file=None):
    global _DB_INSTANCE
    if _DB_INSTANCE is None:
        _DB_INSTANCE = MongoInstance(config_file)

    return _DB_INSTANCE


class MongoInstance(object):

    def __init__(self, config):
        host = config['db.hostname']
        port = int(config['db.port'])
        username = config['db.username']
        password = config['db.password']
        db_name = config['db.name']
        collection = config['db.collection']

        print('username/password: %s, %s' % (username, password))
        self._client = MongoClient(host=host, port=port)
        self._db = self._client[db_name]
        # self._db.authenticate(name=username, password=password)

        self._collection = self._db[collection]

    @property
    def instance(self):
        return self._collection

