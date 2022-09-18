import json
import yaml
from gendiff.get_data import get_data_from_file


def get_parsed_data(path_file):
    if path_file.endswith('.yaml') or path_file.endswith('.yml'):
        parsed_data = yaml.safe_load(get_data_from_file(path_file))
    if path_file.endswith('.json'):
        parsed_data = json.load(get_data_from_file(path_file))
    return parsed_data
