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
            if not i.startswith('del.') and not i.startswith(
                    'ch-.') and not i.startswith('ch+.') and not i.startswith(
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
            if not i.startswith('del.') and not i.startswith(
                    'add.') and not i.startswith('ch-.') and not i.startswith(
                    'ch+.'):
                text += f'{" " * depth}    {i}: {new_value}\n'
    text += f'{" " * (depth)}{"}"}'
    text = text.replace('True', 'true').replace('False',
                                                'false').replace('None',
                                                                 'null')
    return text
