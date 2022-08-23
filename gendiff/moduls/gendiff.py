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
            if i in file1 and i in file2 and file1[i] != file2[i]:
                diff[f'ch-.{i}'] = file1[i]
                diff[f'ch+.{i}'] = file2[i]
            if i in file1 and i not in file2:
                diff[f'del.{i}'] = file1[i]
            if i not in file1 and i in file2:
                diff[f'add.{i}'] = file2[i]
            if i in file1 and i in file2 and file1[i] == file2[i]:
                diff[i] = file1[i]
        if type(file1.get(i)) == type(file2.get(i)) == dict:
            children1 = file1.get(i)
            children2 = file2.get(i)
            new_value = get_diff(children1, children2)
            diff[i] = new_value
    return diff


def stylish(diff, depth=0):
    text = '{\n'
    for i in diff:
        if not type(diff.get(i)) == dict:
            if i.startswith('add.'):
                text += f'{" " * depth}  + {i[4:]}: {diff[i]}\n'
            if i.startswith('del.'):
                text += f'{" " * depth}  - {i[4:]}: {diff[i]}\n'
            if i.startswith('ch-.'):
                text += f'{" " * depth}  - {i[4:]}: {diff[i]}\n'
            if i.startswith('ch+.'):
                text += f'{" " * depth}  + {i[4:]}: {diff[i]}\n'
            if not i.startswith('del.') and not i.startswith('ch-.') and not i.startswith('ch+.') and not i.startswith(
                    'add.'):
                text += f'{" " * depth}    {i}: {diff[i]}\n'

        if type(diff.get(i)) == dict:
            children = diff.get(i)
            new_value = stylish(children, depth + 4)
            if i.startswith('add.'):
                text += f'{" " * depth}  + {i[4:]}: {new_value}\n'
            if i.startswith('del.'):
                text += f'{" " * depth}  - {i[4:]}: {new_value}\n'
            if i.startswith('ch-.'):
                text += f'{" " * depth}  - {i[4:]}: {new_value}\n'
            if i.startswith('ch+.'):
                text += f'{" " * depth}  + {i[4:]}: {new_value}\n'
            if not i.startswith('del.') and not i.startswith('add.') and not i.startswith('ch-.') and not i.startswith(
                    'ch+.'):
                text += f'{" " * depth}    {i}: {new_value}\n'
    text += f'{" " * (depth)}{"}"}'
    text = text.replace('True', 'true').replace('False',
                                                'false').replace('None', 'null')
    return text


def plain(diff, depth={}):
    text = '{\n'
    for i in diff:
        if type(diff.get(i)) == dict and i[:4] == "    ":
            print('aadfsgs')


def generate_diff(path_file1, path_file2, formater=stylish):
    file1, file2 = get_data(path_file1, path_file2)
    diff = get_diff(file1, file2)
    result = formater(diff)
    return result
