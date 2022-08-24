from gendiff import generate_diff
from gendiff.moduls.formaters.plain import plain


def test_generare_diff_json():
    with open('tests/fixtures/correct_result.txt', 'r') as file:
        result_data = file.read()
    assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json') == result_data


def test_generare_diff_yaml():
    with open('tests/fixtures/correct_result.txt', 'r') as file:
        result_data = file.read()
    assert generate_diff('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yaml') == result_data


def test_generare_diff_mix():
    with open('tests/fixtures/correct_result.txt', 'r') as file:
        result_data = file.read()
    assert generate_diff('tests/fixtures/file1.yaml', 'tests/fixtures/file2.json') == result_data


def test_generare_diff_empty():
    assert generate_diff('tests/fixtures/empty_file.json', 'tests/fixtures/empty_file.json') == '{\n}'


def test_generare_diff_tree_json():
    with open('tests/fixtures/correct_result_tree.rtf', 'r') as file:
        result_data = file.read()
    assert generate_diff('tests/fixtures/file1_tree.json', 'tests/fixtures/file2_tree.json') == result_data


def test_generare_diff_tree_yaml():
    with open('tests/fixtures/correct_result_tree.rtf', 'r') as file:
        result_data = file.read()
    assert generate_diff('tests/fixtures/file1_tree.yaml', 'tests/fixtures/file2_tree.yaml') == result_data

def test_generare_diff_tree_plain():
    with open('tests/fixtures/correct_result_tree_plain.rtf', 'r') as file:
        result_data = file.read()
    assert generate_diff('tests/fixtures/file1_tree.yaml', 'tests/fixtures/file2_tree.yaml', formater=plain) == result_data