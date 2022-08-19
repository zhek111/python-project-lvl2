from gendiff import generate_diff


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
