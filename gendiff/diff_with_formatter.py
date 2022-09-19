from gendiff.diff import get_diff
from gendiff.get_parsed_data import get_parsed_data
from gendiff.formaters.select_formatter import select_formatter
from gendiff.get_data import get_data_from_file


def generate_diff(path_file1: str, path_file2: str,
                  formater: str = 'stylish') -> str:
    data1, format1 = get_data_from_file(path_file1)
    data2, format2 = get_data_from_file(path_file2)
    parced_data1 = get_parsed_data(data1, format1)
    parced_data2 = get_parsed_data(data2, format2)
    diff = get_diff(parced_data1, parced_data2)
    return select_formatter(formater)(diff)
