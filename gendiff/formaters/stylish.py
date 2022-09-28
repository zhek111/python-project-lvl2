from typing import Any

DEFAULT_INDENT = 4


def get_nested_value(dict_values: dict, depth: int) -> str:
    list_str = ['{']
    for key, value in dict_values.items():
        if isinstance(value, dict):
            new_value = get_nested_value(value, depth + DEFAULT_INDENT)
            list_str.append(f"{' ' * depth}    {key}: {new_value}")
        else:
            list_str.append(f"{' ' * depth}    {key}: {value}")
    list_str.append(f'{" " * depth}}}')
    text_str = '\n'.join(list_str)
    return text_str


def line_forming(dictionary: dict, value: Any, depth: int, sign: str) -> str:
    if isinstance(dictionary[value], dict):
        dictionary[value] = get_nested_value(dictionary[value],
                                             depth + DEFAULT_INDENT)
    if dictionary[value] is True:
        return f'{" " * depth}{sign}{dictionary["key"]}: true'
    if dictionary[value] is False:
        return f'{" " * depth}{sign}{dictionary["key"]}: false'
    if dictionary[value] is None:
        return f'{" " * depth}{sign}{dictionary["key"]}: null'
    return f'{" " * depth}{sign}{dictionary["key"]}: {dictionary[value]}'


def build_stylish_iter(diff, depth=0):
    text = ['{']
    for dictionary in diff:
        if dictionary['operation'] == 'same':
            text.append(line_forming(dictionary, 'value', depth, sign='    '))
        if dictionary['operation'] == 'add':
            text.append(line_forming(dictionary, 'new', depth, sign='  + '))
        if dictionary['operation'] == 'removed' or dictionary[
                'operation'] == 'changed':
            text.append(line_forming(dictionary, 'old', depth, sign='  - '))
        if dictionary['operation'] == 'changed':
            text.append(line_forming(dictionary, 'new', depth, sign='  + '))
        if dictionary['operation'] == 'nested':
            new_value = build_stylish_iter(dictionary['value'],
                                           depth + DEFAULT_INDENT)
            text.append(f'{" " * depth}    {dictionary["key"]}: {new_value}')
    text.append(f'{" " * depth}}}')
    text_str = '\n'.join(text)
    return text_str


def render_stylish(diff):
    return build_stylish_iter(diff, depth=0)
