from gendiff import generate_diff
import pytest


@pytest.mark.parametrize(
    "test_input1,test_input2, formater,  expected",
    [
        pytest.param(
            'tests/fixtures/file1.json',
            'tests/fixtures/file2.json',
            'stylish',
            'tests/fixtures/correct_result.txt',
            id="flat_json_file"
        ),
        pytest.param(
            'tests/fixtures/file1.yaml',
            'tests/fixtures/file2.yaml',
            'stylish',
            'tests/fixtures/correct_result.txt',
            id="flat_yaml_file"
        ),
        pytest.param(
            'tests/fixtures/file1.yaml',
            'tests/fixtures/file2.json',
            'stylish',
            'tests/fixtures/correct_result.txt',
            id="flat_mix_file"
        ),
        pytest.param(
            'tests/fixtures/empty_file.json',
            'tests/fixtures/empty_file.json',
            'stylish',
            'tests/fixtures/correct_result_empty.txt',
            id="empty_file"
        ),
        pytest.param(
            'tests/fixtures/file1_tree.json',
            'tests/fixtures/file2_tree.json',
            'stylish',
            'tests/fixtures/correct_result_tree.txt',
            id="tree_json_file"
        ),
        pytest.param(
            'tests/fixtures/file1_tree.yaml',
            'tests/fixtures/file2_tree.yaml',
            'stylish',
            'tests/fixtures/correct_result_tree.txt',
            id="tree_yaml_file"
        ),
        pytest.param(
            'tests/fixtures/file1_tree.yaml',
            'tests/fixtures/file2_tree.yaml',
            'plain',
            'tests/fixtures/correct_result_tree_plain.txt',
            id="tree_plain"
        ),
        pytest.param(
            'tests/fixtures/file1_tree.json',
            'tests/fixtures/file2_tree.json',
            'json',
            'tests/fixtures/correct_result_tree_json.txt',
            id="tree_json"
        ),
    ],
)
def test_generare_diff(test_input1, test_input2, formater, expected):
    with open(expected, 'r') as file:
        result_data = file.read()
    assert generate_diff(test_input1, test_input2, formater) == result_data
