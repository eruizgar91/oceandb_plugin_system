#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `oceandb_plugin_system` package."""

from pytest import mark, raises



def test_oceandb_expects_plugin():
    from oceandb_plugin_system.plugin import AbstractPlugin
    with raises(TypeError):
        AbstractPlugin()


def test_oceandb_expcects_subclassed_plugin():
    from oceandb_plugin_system.plugin import AbstractPlugin

    class NonSubclassPlugin():
        pass

    plugin = NonSubclassPlugin()
    with raises(TypeError):
        AbstractPlugin(plugin)

def test_oceandb_using_mongo_plugin():
    from oceandb_plugin_system.oceandb import OceanDb
    from oceandb_plugin_system.utils import parse_config

    conf = parse_config('../config/oceandb_plugin_system.ini')
    oceandb = OceanDb(conf)
    assert oceandb.plugin.type == "MongoDB"


