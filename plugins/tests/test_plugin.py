from pytest import mark, raises
from plugins.mongo.plugin import Mongo


def test_plugin_type_is_mongodb():
    print(Mongo.type)
    assert Mongo.type == 'MongoDB'
