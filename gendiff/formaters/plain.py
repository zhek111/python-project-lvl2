from typing import Any

DEFAULT_DEPTH = list()


def determine_value(dictionary: dict, value: Any) -> None:
    if isinstance(dictionary[value], dict):
        dictionary[value] = "[complex value]"
    elif dictionary[value] is True:
        dictionary[value] = "true"
    elif dictionary[value] is False:
        dictionary[value] = "false"
    elif dictionary[value] is None:
        dictionary[value] = "null"
    elif not isinstance(dictionary[value], int):
        dictionary[value] = f"'{dictionary[value]}'"


def build_plain_iter(diff: list[dict], depth: list = None) -> str:
    if depth is None:
        depth = DEFAULT_DEPTH
    text = list()
    for dictionary in diff:
        property = '.'.join(depth + [dictionary['key']])
        if dictionary['operation'] == 'add':
            determine_value(dictionary, 'new')
            text.append(f"Property '{property}' "
                        f"was added with value: {dictionary['new']}")
        if dictionary['operation'] == 'removed':
            text.append(f"Property '{property}' was removed")
        if dictionary['operation'] == 'nested':
            new_value = build_plain_iter(dictionary['value'],
                                         depth + [dictionary['key']])
            text.append(f"{new_value}")
        if dictionary['operation'] == 'changed':
            determine_value(dictionary, 'new')
            determine_value(dictionary, 'old')
            text.append(f"Property '{property}' was updated. "
                        f"From {dictionary['old']} to {dictionary['new']}")
    text_str = '\n'.join(text)
    return text_str


def render_plain(diff: list[dict]) -> str:
    return build_plain_iter(diff, depth=None)
