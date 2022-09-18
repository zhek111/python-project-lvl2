from gendiff.diff import get_diff
from gendiff.get_parsed_data import get_parsed_data
from gendiff.formaters.select_formatter import select_formatter


def generate_diff(path_file1, path_file2, formater='stylish'):
    file1 = get_parsed_data(path_file1)
    file2 = get_parsed_data(path_file2)
    diff = get_diff(file1, file2)
    return select_formatter(formater)(diff)
