from typing import Any

DEFAULT_INDENT = 4
DEFAULT_DEPTH = 0


def get_value(dict_values: dict, depth: int) -> str:
    text = '{\n'
    for key, value in dict_values.items():
        if not isinstance(value, dict):
            text += f"{' ' * depth}    {key}: {value}\n"
        if isinstance(value, dict):
            new_value = get_value(value, depth + 4)
            text += f"{' ' * depth}    {key}: {new_value}\n"
    text += f'{" " * depth}}}'
    return text


def line_forming(dictionary: dict, value: Any, depth: int, sign: str) -> str:
    if type(dictionary[value]) == dict:
        dictionary[value] = get_value(dictionary[value], depth + 4)
    return f'{" " * depth}{sign}{dictionary["key"]}: {dictionary[value]}\n'


def stylish(diff: list[dict], depth: int = DEFAULT_DEPTH) -> str:
    text = '{\n'
    for dictionary in diff:
        if dictionary['operation'] == 'same':
            text += line_forming(dictionary, 'value', depth, sign='    ')
        if dictionary['operation'] == 'add':
            text += line_forming(dictionary, 'new', depth, sign='  + ')
        if dictionary['operation'] == 'removed' or \
                dictionary['operation'] == 'changed':
            text += line_forming(dictionary, 'old', depth, sign='  - ')
        if dictionary['operation'] == 'changed':
            text += line_forming(dictionary, 'new', depth, sign='  + ')
        if dictionary['operation'] == 'nested':
            new_value = stylish(dictionary['value'], depth + 4)
            text += f'{" " * depth}    {dictionary["key"]}: {new_value}\n'
    text += f'{" " * depth}}}'
    text = text.replace('True', 'true').replace(
        'False', 'false').replace('None', 'null')
    return text
