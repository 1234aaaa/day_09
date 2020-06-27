import yaml
import os


class Utils:
    @classmethod
    def get_yaml_data(cls, name):
        with open("./data"+os.sep+name, "r")as f:
            return yaml.safe_load(f)
