import json
import yaml


def get_data(path_file1, path_file2):
    if path_file1.endswith('.yaml') or path_file1.endswith('.yml'):
        file1 = yaml.safe_load(open(path_file1))
    if path_file1.endswith('.json'):
        file1 = json.load(open(path_file1))
    if path_file2.endswith('.yaml') or path_file2.endswith('.yml'):
        file2 = json.load(open(path_file2))
    if path_file2.endswith('.json'):
        file2 = json.load(open(path_file2))
    return file1, file2


def get_diff(file1, file2):
    diff = {}
    sorted_keys = sorted(list(set(file1.keys()) | set(file2.keys())))
    for i in sorted_keys:
        if not type(file1.get(i)) == type(file2.get(i)) == dict:
            if i in file1 and i in file2 and file1[i] == file2[i]:
                diff[f'   {i}'] = file1[i]
            if i in file1 and i in file2 and file1[i] != file2[i]:
                diff[f' - {i}'] = file1[i]
                diff[f' + {i}'] = file2[i]
            if i in file1 and i not in file2:
                diff[f' - {i}'] = file1[i]
            if i not in file1 and i in file2:
                diff[f' + {i}'] = file2[i]
        if type(file1.get(i)) == type(file2.get(i)) == dict:
            children1 = file1.get(i)
            children2 = file2[i]
            new_value = list(map(get_diff, (children1,), (children2,)))[0]
            diff[f'   {i}'] = new_value
        if type(file2.get(i)) == dict != type(file1.get(i)):
            children2 = file2.get(i)
            children1 = file2.get(i)
            new_value = list(map(get_diff, (children1,), (children2,)))[0]
        if type(file1.get(i)) == dict != type(file2.get(i)):
            children2 = file1.get(i)
            children1 = file1.get(i)
            new_value = list(map(get_diff, (children1,), (children2,)))[0]
            diff[f' - {i}'] = new_value
    return diff


def stylish(diff, depth=0):
    text = '{\n'
    for i in diff:
        if not isinstance(diff.get(i), dict):
            text += f'{" " * depth}{i}: {diff[i]}\n'
        if isinstance(diff.get(i), dict):
            children = diff.get(i)
            new_value = stylish(children, depth + 4)
            text += f'{" " * depth}{i}: {new_value}\n'
    text += f'{" " * (depth)}{"}"}'

    return text


def generate_diff(path_file1, path_file2):
    file1, file2 = get_data(path_file1, path_file2)
    diff = get_diff(file1, file2)
    formater = stylish(diff)
    return formater


# file1 = {
#     'common': {
#         'setting1': 'Value 1',
#         'setting2': 200,
#         'setting3': True,
#         'setting6': {
#             'key': 'value',
#             'doge': {
#                 'wow': ''
#             }
#         }
#     },
#     'group1': {
#         'baz': 'bas',
#         'foo': 'bar',
#         'nest': {
#             'key': 'value'
#         }
#     },
#     'group2': {
#         'abc': 12345,
#         'deep': {
#             'id': 45
#         }
#     }
# }
#
# file2 = {
#     'common': {
#         'follow': False,
#         'setting1': 'Value 1',
#         'setting3': None,
#         'setting4': 'blah blah',
#         'setting5': {
#             'key5': 'value5'
#         },
#         'setting6': {
#             'key': 'value',
#             'ops': 'vops',
#             'doge': {
#                 'wow': 'so much'
#             }
#         }
#     },
#     'group1': {
#         'foo': 'bar',
#         'baz': 'bars',
#         'nest': 'str'
#     },
#     'group3': {
#         'deep': {
#             'id': {
#                 'number': 45
#             }
#         },
#         'fee': 100500
#     }
# }
#
#
# result = '''{
#     common: {
#       + follow: false
#         setting1: Value 1
#       - setting2: 200
#       - setting3: true
#       + setting3: null
#       + setting4: blah blah
#       + setting5: {
#             key5: value5
#         }
#         setting6: {
#             doge: {
#               - wow:
#               + wow: so much
#             }
#             key: value
#           + ops: vops
#         }
#     }
#     group1: {
#       - baz: bas
#       + baz: bars
#         foo: bar
#       - nest: {
#             key: value
#         }
#       + nest: str
#     }
#   - group2: {
#         abc: 12345
#         deep: {
#             id: 45
#         }
#     }
#   + group3: {
#         deep: {
#             id: {
#                 number: 45
#             }
#         }
#         fee: 100500
#     }
# }'''