import yaml
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

def load(config_file=None):
    config_path = config_file or CONFIG_PATH
    data = {}

    with open(config_path) as f:
        data = yaml.safe_load(f)

    return Config(data)


