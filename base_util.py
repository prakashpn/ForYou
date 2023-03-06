import os
from configparser import ConfigParser

basepath = os.path.dirname(__file__)

project_url = "http://localhost:8080"
config_dir = os.path.join(basepath, "conf")

config = ConfigParser()
config.read(os.path.join(config_dir, 'app.ini'))
