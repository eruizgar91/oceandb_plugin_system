import configparser
import argparse
import importlib.util
from oceandb_plugin_system.constants import CONFIG_OPTION
from oceandb_plugin_system.exceptions import ConfigError


def parse_args():
    """Parse command line arguments given to the agent"""
    parser = argparse.ArgumentParser(description="OceanDB Plugin System")
    parser.add_argument('--config', metavar='path', required=False,
                        help='path to the oceandb_plugin_sysyem.ini file')
    try:
        args = parser.parse_args()
        return args
    except:
        pass


def parse_config(file_path='../config/oceandb_plugin_system.ini'):
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


def start_plugin():
    """This function initialize the Ocean plugin"""
    try:
        args = parse_args()
        if args is not None:
            if args.config is not None:
                config = parse_config(args.config)
            else:
                config = parse_config()
        else:
            config = parse_config()
    except:
        raise ConfigError("You should provide a valid config.")
    plugin_instance = load_plugin(config)
    return plugin_instance(config)


def load_plugin(config):
    module = config['module']
    module_path = "../plugins/%s/plugin.py" % module
    spec = importlib.util.spec_from_file_location("plugin.py", module_path)
    foo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(foo)
    return foo.Plugin


def print_help():
    """Print the default help in stdout"""
    pass
