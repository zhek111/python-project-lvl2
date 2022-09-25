DEFAULT_INDENT = 4
DEFAULT_DEPTH = 0


def get_value(dict_values, depth):
    text = '{\n'
    for key, value in dict_values.items():
        if not isinstance(value, dict):
            text += f"{' ' * (depth)}    {key}: {value}\n"
        if isinstance(value, dict):
            new_value = get_value(value, depth + 4)
            text += f"{' ' * (depth)}    {key}: {new_value}\n"
    text += f'{" " * (depth)}}}'
    return text


def line_forming(i, value, depth, sign):
    if type(i[value]) == dict:
        i[value] = get_value(i[value], depth + 4)
    return f'{" " * depth}{sign}{i["key"]}: {i[value]}\n'


def stylish(diff, depth=DEFAULT_DEPTH):
    text = '{\n'
    for i in diff:
        if i['operation'] == 'same':
            text += line_forming(i, 'value', depth, sign='    ')
        if i['operation'] == 'add':
            text += line_forming(i, 'new', depth, sign='  + ')
        if i['operation'] == 'removed' or i['operation'] == 'changed':
            text += line_forming(i, 'old', depth, sign='  - ')
        if i['operation'] == 'changed':
            text += line_forming(i, 'new', depth, sign='  + ')
        if i['operation'] == 'nested':
            new_value = stylish(i['value'], depth + 4)
            text += f'{" " * depth}    {i["key"]}: {new_value}\n'

    text += f'{" " * depth}}}'
    text = text.replace('True', 'true').replace(
        'False', 'false').replace('None', 'null')
    return text