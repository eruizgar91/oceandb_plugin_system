from plugins.mongo import plugin
import configparser
import argparse
import pprint


def parse_args():
    """Parse command line arguments given to the agent"""
    parser = argparse.ArgumentParser(description="OceanDB Plugin System")
    parser.add_argument('--config', metavar='path', required=True,
                        help='path to the oceandb_plugin_sysyem.ini file')

    args = parser.parse_args()
    return args


CONFIG_OPTION = 'oceandb'


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


def main():
    args = parse_args()
    config = parse_config(args.config)
    app = plugin.Mongo(config)
    print(app.type)
    # print(app.read(1))
    app.write({"id": 2})
    for doc in app.list():
        pprint.pprint(doc)
    print('_________________')
    app.delete(2)
    for doc in app.list():
        pprint.pprint(doc)
    return app


if __name__ == '__main__':
    app = main()
