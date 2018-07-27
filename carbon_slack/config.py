from ruamel.yaml import YAML
import getpass
import subprocess
import os
import sys

CONFIG_PATH = '/etc/carbon-slack.yml'

TOKEN = 'token'
CHANNEL = 'channel'
CARBON_SERVER='carbon-server'
CARBON_PORT='carbon-port'

class Config(object):
    def __init__(self, data):
        self.token = data[TOKEN]
        self.channel = data[CHANNEL]
        self.carbon_server = data[CARBON_SERVER]
        self.carbon_port = data[CARBON_PORT]

def serialized_sample():
    return YAML().dump({
        TOKEN: 'xoxp-1234567890-yadda-yadda',
        CHANNEL: 'metrics',
        CARBON_SERVER: '127.0.0.1',
        CARBON_PORT: 2023
    }, sys.stdout)

def load(config_file=None):
    config_path = config_file or CONFIG_PATH
    data = {}

    with open(config_path) as f:
        data = YAML.load(f)

    return Config(data)


