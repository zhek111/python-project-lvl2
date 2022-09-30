from typing import Any


def to_str(value: Any) -> str:
    if isinstance(value, dict):
        return "[complex value]"
    elif value is True:
        return "true"
    elif value is False:
        return "false"
    elif value is None:
        return "null"
    elif not isinstance(value, int):
        return f"'{value}'"


def build_plain_iter(diff: dict, path: list = None) -> str:
    if path is None:
        path = list()
    line = list()
    for dictionary in diff:
        property = '.'.join(path + [dictionary['key']])
        if dictionary['operation'] == 'add':
            line.append(f"Property '{property}' "
                        f"was added with value: "
                        f"{to_str(dictionary['new'])}")
        if dictionary['operation'] == 'removed':
            line.append(f"Property '{property}' was removed")
        if dictionary['operation'] == 'nested':
            new_value = build_plain_iter(dictionary['value'],
                                         path + [dictionary['key']])
            line.append(f"{new_value}")
        if dictionary['operation'] == 'changed':
            line.append(f"Property '{property}' was updated. "
                        f"From {to_str(dictionary['old'])} to "
                        f"{to_str(dictionary['new'])}")
    return '\n'.join(line)


def render_plain(diff: dict) -> str:
    return build_plain_iter(diff)
