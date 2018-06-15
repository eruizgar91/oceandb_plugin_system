from pytest import mark, raises
from plugins.mongo.plugin import Plugin
from plugins.mongo.app import *


conf = parse_config('./oceandb_plugin_system.ini')
mongo = Plugin(conf)


def test_plugin_type_is_mongodb():
    assert mongo.type == 'MongoDB'


def test_plugin_write_and_read():
    mongo.write({"id": 1, "value": "test"})
    print(mongo.read(1))
    assert mongo.read(1) == {"id": 1, "value": "test"}
