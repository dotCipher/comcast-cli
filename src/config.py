import os
import yaml

DIR_SOURCE = os.path.dirname(os.path.abspath(__file__))
DIR_PROJECT_ROOT = os.path.normpath(os.path.join(DIR_SOURCE, '..'))


CONFIG_FILE_NAME = "comcast.yml"
DEFAULT_SYNC_CONFIG_FILE_PATH = os.path.normpath(os.path.join(DIR_PROJECT_ROOT, CONFIG_FILE_NAME))


def read_config(path=None):
    if path is None:
        return None
    with open(path) as config_yml:
        return yaml.load(config_yml)


class ComcastConfiguration:
    KEY_SYNC = "comcast"

    KEY_SOURCE = "username"
    KEY_DEST = "password"

    def __init__(self, config_file=None):
        if config_file is not None:
            if os.path.exists(config_file):
                self.config = read_config(config_file)
            else:
                raise Exception('Configuration file does not exist: %s' % config_file)

    def __str__(self):
        return yaml.dump(self.config, default_flow_style=False)
