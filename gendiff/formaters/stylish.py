DEFAULT_INDENT = 4
DEFAULT_DEPTH = 0


def stylish(diff, depth=DEFAULT_DEPTH):
    text = '{\n'
    for i in diff:
        if i['operation'] == 'none':
            if type(i['value']) != list:
                text += f'{" " * depth}    {i["key"]}: {i["value"]}\n'
            if type(i['value']) == list:
                children = i['value']
                new_value = stylish(children, depth + DEFAULT_INDENT)
                text += f'{" " * depth}    {i["key"]}: {new_value}\n'
        if i['operation'] == 'add':
            if type(i['new']) != list:
                text += f'{" " * depth}  + {i["key"]}: {i["new"]}\n'
            if type(i['new']) == list:
                children = i['new']
                new_value = stylish(children, depth + DEFAULT_INDENT)
                text += f'{" " * depth}  + {i["key"]}: {new_value}\n'
        if i['operation'] == 'delete' or i['operation'] == 'update':
            if type(i['old']) != list:
                text += f'{" " * depth}  - {i["key"]}: {i["old"]}\n'
            if type(i['old']) == list:
                children = i['old']
                new_value = stylish(children, depth + DEFAULT_INDENT)
                text += f'{" " * depth}  - {i["key"]}: {new_value}\n'
        if i['operation'] == 'update':
            if type(i['new']) != list:
                text += f'{" " * depth}  + {i["key"]}: {i["new"]}\n'
            if type(i['new']) == list:
                children = i['new']
                new_value = stylish(children, depth + DEFAULT_INDENT)
                text += f'{" " * depth}  + {i["key"]}: {new_value}\n'
    text += f'{" " * (depth)}{"}"}'
    text = text.replace('True', 'true').replace('False',
                                                'false').replace('None',
                                                                 'null')
    return text
