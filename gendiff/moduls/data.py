import json
import yaml


def get_data(path_file1, path_file2):
    if path_file1.endswith('.yaml') or path_file1.endswith('.yml'):
        file1 = yaml.safe_load(open(path_file1))
    if path_file1.endswith('.json'):
        file1 = json.load(open(path_file1))
    if path_file2.endswith('.yaml') or path_file2.endswith('.yml'):
        file2 = json.load(open(path_file2))
    if path_file2.endswith('.json'):
        file2 = json.load(open(path_file2))
    return file1, file2
