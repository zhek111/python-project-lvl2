from gendiff import generate_diff
import pytest


@pytest.mark.parametrize(
    "test_input1,test_input2, expected",
    [
        pytest.param(
            'tests/fixtures/file1.json', 'tests/fixtures/file2.json',
            'tests/fixtures/correct_result.txt', id="flat_json_file"
        ),
        pytest.param(
            'tests/fixtures/file1.yaml', 'tests/fixtures/file2.yaml',
            'tests/fixtures/correct_result.txt', id="flat_yaml_file"
        ),
        pytest.param(
            'tests/fixtures/file1.yaml', 'tests/fixtures/file2.json',
            'tests/fixtures/correct_result.txt', id="flat_mix_file"
        ),
        pytest.param(
            'tests/fixtures/empty_file.json', 'tests/fixtures/empty_file.json',
            'tests/fixtures/correct_result_empty.txt', id="empty_file"
        ),
        pytest.param(
            'tests/fixtures/file1_tree.json', 'tests/fixtures/file2_tree.json',
            'tests/fixtures/correct_result_tree.txt', id="tree_json_file"
        ),
        pytest.param(
            'tests/fixtures/file1_tree.yaml', 'tests/fixtures/file2_tree.yaml',
            'tests/fixtures/correct_result_tree.txt', id="tree_yaml_file"
        ),
    ],
)
def test_generare_diff(test_input1, test_input2, expected):
    with open(expected, 'r') as file:
        result_data = file.read()
    assert generate_diff(test_input1, test_input2) == result_data


def test_generare_diff_json1():
    with open('tests/fixtures/correct_result.txt', 'r') as file:
        result_data = file.read()
    assert generate_diff('tests/fixtures/file1.json',
                         'tests/fixtures/file2.json') == result_data


def test_generare_diff_yaml():
    with open('tests/fixtures/correct_result.txt', 'r') as file:
        result_data = file.read()
    assert generate_diff('tests/fixtures/file1.yaml',
                         'tests/fixtures/file2.yaml') == result_data


def test_generare_diff_mix():
    with open('tests/fixtures/correct_result.txt', 'r') as file:
        result_data = file.read()
    assert generate_diff('tests/fixtures/file1.yaml',
                         'tests/fixtures/file2.json') == result_data


def test_generare_diff_empty():
    with open('tests/fixtures/correct_result_empty.txt', 'r') as file:
        result_data = file.read()
    assert generate_diff('tests/fixtures/empty_file.json',
                         'tests/fixtures/empty_file.json') == result_data


def test_generare_diff_tree_json():
    with open('tests/fixtures/correct_result_tree.txt', 'r') as file:
        result_data = file.read()
    assert generate_diff('tests/fixtures/file1_tree.json',
                         'tests/fixtures/file2_tree.json') == result_data


def test_generare_diff_tree_yaml():
    with open('tests/fixtures/correct_result_tree.txt', 'r') as file:
        result_data = file.read()
    assert generate_diff('tests/fixtures/file1_tree.yaml',
                         'tests/fixtures/file2_tree.yaml') == result_data


def test_generare_diff_tree_plain():
    with open('tests/fixtures/correct_result_tree_plain.txt', 'r') as file:
        result_data = file.read()
    assert generate_diff('tests/fixtures/file1_tree.yaml',
                         'tests/fixtures/file2_tree.yaml',
                         formater='plain') == result_data


def test_generare_diff_tree_get_json():
    with open('tests/fixtures/correct_result_tree_json.txt', 'r') as file:
        result_data = file.read()
    assert generate_diff('tests/fixtures/file1_tree.json',
                         'tests/fixtures/file2_tree.json',
                         formater='json') == result_data
