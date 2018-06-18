"""Implementation of OceanDB plugin based in MongoDB"""
from oceandb_plugin_system.plugin import AbstractPlugin
from plugins.mongo.instance import get_database_instance


class Plugin(AbstractPlugin):
    """Mongo ledger plugin for `Ocean DB's Python reference
    implementation <https://github.com/oceanprotocol/oceandb_plugin_system>`_.
    Plugs in a MongoDB instance as the persistence layer for Ocean Db
    related actions.
    """

    def __init__(self, config):
        """Initialize a :class:`~.Plugin` instance and connect to MongoDB.
        Args:
            *nodes (str): One or more URLs of MongoDB nodes to
                connect to as the persistence layer
        """
        self.driver = get_database_instance(config)

    @property
    def type(self):
        """str: the type of this plugin (``'MongoDB'``)"""
        return 'MongoDB'

    def write(self, obj):
        return self.driver.instance.insert_one(obj)

    def read(self, id):
        return self.driver.instance.find_one({"id": id})

    def update(self, id, obj):
        prev = self.read(id)
        return self.driver.instance.replace_one(prev, obj)

    def delete(self, id):
        return self.driver.instance.delete_one({"id": id})

    def list(self, search_from=None, search_to=None, offset=None, limit=None):
        return self.driver.instance.find()

