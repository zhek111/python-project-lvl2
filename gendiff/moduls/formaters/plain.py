def plain(diff, depth=[]):
    text = ''
    for i in diff:
        if not type(diff.get(i)) == dict:
            if i.startswith('add.'):
                text += f"Property '{'.'.join(depth + [i[4:]])}" \
                        f"' was added with value: '{diff.get(i)}'\n"
            if i.startswith('del.'):
                text += f"Property '{'.'.join(depth + [i[4:]])}" \
                        f"' was removed\n"
            if i.startswith('ch-.') and type(
                    diff.get(i.replace('ch-.', 'ch+.'))) != dict:
                text += f"Property '{'.'.join(depth + [i[4:]])}" \
                        f"' was updated. From '{diff.get(i)}' to '" \
                        f"{diff.get(i.replace('ch-.', 'ch+.'))}'\n"
        if type(diff.get(i)) == dict:
            children = diff.get(i)
            new_value = plain(children, depth=depth + [i])
            if i.startswith('add.'):
                text += f"Property '{'.'.join(depth + [i[4:]])}' was added " \
                        f"with value: [complex value]\n"
            if i.startswith('del.'):
                text += f"Property '{'.'.join(depth + [i[4:]])}' was removed\n"
            if i.startswith('ch-.'):
                text += f"Property '{'.'.join(depth + [i[4:]])}' was " \
                        f"updated. From [complex val" \
                        f"ue] to '{diff.get(i.replace('ch-.', 'ch+.'))}'\n"
            if i.startswith('ch+.'):
                text += f"Property '{'.'.join(depth + [i[4:]])}' was " \
                        f"updated. " \
                        f"From '{diff.get(i.replace('ch+.', 'ch-.'))}' to [" \
                        f"complex value]\n"
            if not i.startswith('del.') and not i.startswith(
                    'add.') and not i.startswith('ch-.') and not i.startswith(
                    'ch+.'):
                text += f"{new_value}"
                text = text.replace("'True'", "true").replace("'False'",
                                                              "false").replace(
                    "'None'", "null").replace("  ", " '' ").replace("'0'",
                                                                    "0")
                text += ' '
    return text
