from gendiff.diff import get_diff
from gendiff.moduls.data import get_data
from gendiff.moduls.formaters.stylish import stylish


def generate_diff(path_file1, path_file2, formater=stylish):
    file1, file2 = get_data(path_file1, path_file2)
    diff = get_diff(file1, file2)
    result = formater(diff)
    return result
