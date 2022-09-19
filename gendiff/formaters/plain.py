DEFAULT_DEPTH = list()


def determine_value(i, value):
    if isinstance(i[value], list):
        i[value] = "[complex value]"


def plain(diff: list[dict], depth=None) -> str:
    if depth is None:
        depth = DEFAULT_DEPTH
    text = str()
    for i in diff:
        property = '.'.join(depth + [i['key']])
        if i['operation'] == 'add':
            determine_value(i, 'new')
            text += f"Property '{property}' " \
                    f"was added with value: '{i['new']}'\n"
        if i['operation'] == 'delete':
            text += f"Property '{property}' was removed\n"
        if i['operation'] == 'none' and type(i['value']) == list:
            new_value = plain(i['value'], depth + [i['key']])
            text += f"{new_value}\n"
        if i['operation'] == 'update':
            determine_value(i, 'new')
            determine_value(i, 'old')
            text += f"Property '{property}' was updated. " \
                    f"From '{i['old']}' to '{i['new']}'\n"
    text = text.replace("'True'", "true").replace("'False'", "false") \
        .replace("'None'", "null").replace("  ", " '' ").replace(
        "'0'", "0").replace("'[complex value]'", "[complex value]")
    return text[:-1]
