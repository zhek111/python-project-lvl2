from gendiff.diff import get_diff
from gendiff.moduls.data import get_data
from gendiff.moduls.formaters.stylish import stylish
from gendiff.moduls.formaters.plain import plain
from gendiff.moduls.formaters.to_json import get_json


def generate_diff(path_file1, path_file2, formater='stylish'):
    file1, file2 = get_data(path_file1, path_file2)
    diff = get_diff(file1, file2)
    if formater == 'stylish':
        return stylish(diff)
    if formater == 'plain':
        return plain(diff)
    if formater == 'json':
        return get_json(diff)
