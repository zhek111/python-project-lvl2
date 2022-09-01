DEFAULF = []

def plain(diff, depth=DEFAULF):
    text = ''
    for i in diff:
        if i['operation'] == 'addition':
            if type(i['new']) != list:
                text += f"Property '{'.'.join(depth + [i['key']])}' was " \
                        f"added with value: '{i['new']}'\n"
            if type(i['new']) == list:
                text += f"Property '{'.'.join(depth + [i['key']])}' was " \
                        f"added with value: [complex value]\n"
        if i['operation'] == 'delete':
            text += f"Property '{'.'.join(depth + [i['key']])}' was removed\n"
        if i['operation'] == 'nothing' and type(i['value']) == list:
            children = i['value']
            new_value = plain(children, depth=depth + [i['key']])
            text += f"{new_value}\n"
        if i['operation'] == 'update':
            if type(i['new']) != list:
                new_value = f"'{i['new']}'"
            if type(i['new']) == list:
                new_value = '[complex value]'
            if type(i['old']) != list:
                old_value = f"'{i['old']}'"
            if type(i['old']) == list:
                old_value = '[complex value]'
            text += f"Property '{'.'.join(depth + [i['key']])}' was update" \
                    f"d. From {old_value} to {new_value}\n"
    text = text.replace("'True'", "true").replace("'False'", "false") \
        .replace("'None'", "null").replace("  ", " '' ").replace("'0'", "0")
    return text[:-1]
