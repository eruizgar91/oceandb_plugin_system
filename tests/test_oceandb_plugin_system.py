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


