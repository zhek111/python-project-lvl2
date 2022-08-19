import json
import yaml


def reverse(string):
    return string[::-1]


def generate_diff(path_file1, path_file2):
    if path_file1.endswith('.yaml') or path_file1.endswith('.yml'):
        file1 = yaml.safe_load(open(path_file1))
    if path_file1.endswith('.json'):
        file1 = json.load(open(path_file1))
    if path_file2.endswith('.yaml') or path_file2.endswith('.yml'):
        file2 = json.load(open(path_file2))
    if path_file2.endswith('.json'):
        file2 = json.load(open(path_file2))
    return change_to_txt(file1, file2)


def change_to_txt(file1, file2):
    sorted_keys = sorted(list(set(file1.keys()) | set(file2.keys())))
    result = '{\n'
    for i in sorted_keys:
        if i in file1 and i in file2 and file1[i] == file2[i]:
            result += f'   {i}: {file1[i]}\n'
        if i in file1 and i in file2 and file1[i] != file2[i]:
            result += f' - {i}: {file1[i]}\n + {i}: {file2[i]}\n'
        if i in file1 and i not in file2:
            result += f' - {i}: {file1[i]}\n'
        if i not in file1 and i in file2:
            result += f' + {i}: {file2[i]}\n'
    result += '}'
    result = result.replace('True', 'true').replace('False', 'false')
    return result

# print(generate_diff('tests/fixtures/empty_file.json',
# 'tests/fixtures/empty_file.json'))
