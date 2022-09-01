INDENT = 4
DEFAUL = 0
def stylish(diff, depth=DEFAUL):
    text = '{\n'
    for i in diff:
        if i['operation'] == 'nothing':
            if type(i['value']) != list:
                text += f'{" " * depth}    {i["key"]}: {i["value"]}\n'
            if type(i['value']) == list:
                children = i['value']
                new_value = stylish(children, depth + INDENT)
                text += f'{" " * depth}    {i["key"]}: {new_value}\n'
        if i['operation'] == 'addition':
            if type(i['new']) != list:
                text += f'{" " * depth}  + {i["key"]}: {i["new"]}\n'
            if type(i['new']) == list:
                children = i['new']
                new_value = stylish(children, depth + INDENT)
                text += f'{" " * depth}  + {i["key"]}: {new_value}\n'
        if i['operation'] == 'delete':
            if type(i['old']) != list:
                text += f'{" " * depth}  - {i["key"]}: {i["old"]}\n'
            if type(i['old']) == list:
                children = i['old']
                new_value = stylish(children, depth + INDENT)
                text += f'{" " * depth}  - {i["key"]}: {new_value}\n'
        if i['operation'] == 'update':
            if type(i['old']) != list:
                text += f'{" " * depth}  - {i["key"]}: {i["old"]}\n'
            if type(i['old']) == list:
                children = i['old']
                new_value = stylish(children, depth + INDENT)
                text += f'{" " * depth}  - {i["key"]}: {new_value}\n'
            if type(i['new']) != list:
                text += f'{" " * depth}  + {i["key"]}: {i["new"]}\n'
            if type(i['new']) == list:
                children = i['new']
                new_value = stylish(children, depth + INDENT)
                text += f'{" " * depth}  + {i["key"]}: {new_value}\n'
    text += f'{" " * (depth)}{"}"}'
    text = text.replace('True', 'true').replace('False',
                                                'false').replace('None',
                                                                 'null')
    return text
