from gendiff.diff import get_diff
from gendiff.data import get_data
from gendiff.formaters.stylish import stylish
from gendiff.formaters.plain import plain
from gendiff.formaters.json import json


def generate_diff(path_file1, path_file2, formater='stylish'):
    file1 = get_data(path_file1)
    file2 = get_data(path_file2)
    diff = get_diff(file1, file2)
    if formater == 'stylish':
        return stylish(diff)
    if formater == 'plain':
        return plain(diff)
    if formater == 'json':
        return json(diff)
