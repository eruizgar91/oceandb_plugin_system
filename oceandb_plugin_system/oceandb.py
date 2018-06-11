"""Console script for oceandb_plugin_system."""
import configparser
import argparse
import attr
import pkgutil
import importlib

from oceandb_plugin_system.constants import CONFIG_OPTION
from oceandb_plugin_system.plugin import AbstractPlugin

"""Main module."""


def parse_args():
    """Parse command line arguments given to the agent"""
    parser = argparse.ArgumentParser(description="OceanDB Plugin System")
    parser.add_argument('--config', metavar='path', required=True,
                        help='path to the oceandb_plugin_sysyem.ini file')

    args = parser.parse_args()
    return args


def parse_config(file_path):
    """Loads the configuration file given as parameter"""
    config_parser = configparser.ConfigParser()
    config_parser.read(file_path)
    plugin_config = {}
    options = config_parser.options(CONFIG_OPTION)
    for option in options:
        try:
            plugin_config[option] = config_parser.get(CONFIG_OPTION, option)
            if plugin_config[option] == -1:
                print("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            plugin_config[option] = None
    return plugin_config


def start_plugin(config):
    """This function initialize the Ocean plugin"""

    # module = __import__(config.get('module'))
    # module = importlib.abc.Loader.load_module(config.get('module'),'../plugins/plugin.py')
    # instance = module.__init__('plugin')
    print(config)
    for (_, name, _) in pkgutil.iter_modules('plugins'):
        print(name)

    my_module = importlib.import_module('plugin', 'plugins')
    return my_module.__init__


def print_help():
    """Print the default help in stdout"""
    pass


@attr.s(frozen=True, repr=False)
class OceanDb:
    """High-level, plugin-bound Ocean DB functions.
    Instantiated with an subclass implementing the ledger plugin
    interface (:class:`~.AbstractPlugin`) that will automatically be
    bound to all top-level functions:
        - :attr:`type` (as a read-only property)
        - :func:`write`
        - :func:`read`
        - :func:`update`
        - :func:`delete`
        - :func:`list`
    Attributes:
        plugin (Plugin): Bound persistence layer plugin.
    """
    plugin = attr.ib(validator=attr.validators.instance_of(AbstractPlugin))

    def __repr__(self):
        return 'OceanDB bound to plugin: {}'.format(self.plugin)

if __name__ == "__main__":
    args = parse_args()
    config = parse_config(args.config)
    plugin = start_plugin(config)


