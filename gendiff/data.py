import json
import yaml


def get_data(path_file):
    if path_file.endswith('.yaml') or path_file.endswith('.yml'):
        file = yaml.safe_load(open(path_file))
    if path_file.endswith('.json'):
        file = json.load(open(path_file))
    return file
