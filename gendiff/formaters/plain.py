from typing import Any


def to_str(value: Any) -> [str | int]:
    if isinstance(value, dict):
        return "[complex value]"
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return "null"
    # if isinstance(value, int):
    #     return value
    return f"'{value}'"


def build_plain_iter(diff: dict, path: str = None) -> str:
    if path is None:
        path = str()
    line = list()
    for dictionary in diff:
        property = f"{path}{dictionary['key']}"
        if dictionary['operation'] == 'add':
            line.append(f"Property '{property}' "
                        f"was added with value: "
                        f"{to_str(dictionary['new'])}")
        if dictionary['operation'] == 'removed':
            line.append(f"Property '{property}' was removed")
        if dictionary['operation'] == 'nested':
            new_value = build_plain_iter(dictionary['value'], f"{property}.")
            line.append(f"{new_value}")
        if dictionary['operation'] == 'changed':
            line.append(f"Property '{property}' was updated. "
                        f"From {to_str(dictionary['old'])} to "
                        f"{to_str(dictionary['new'])}")
    return '\n'.join(line)


def render_plain(diff: dict) -> str:
    return build_plain_iter(diff)
