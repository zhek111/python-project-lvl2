def get_diff(parced_data1: dict, parced_data2: dict) -> list[dict]:
    diff = list()
    sorted_keys = sorted(
        list(set(parced_data1.keys()) | set(parced_data2.keys()))
    )
    for i in sorted_keys:
        if i not in parced_data1:
            diff.append({'key': i, 'operation': 'add', 'new': parced_data2[i]})
        elif i not in parced_data2:
            diff.append(
                {'key': i, 'operation': 'removed', 'old': parced_data1[i]})
        elif isinstance(parced_data1[i], dict) and isinstance(
                parced_data2[i], dict):
            child = get_diff(parced_data1[i], parced_data2[i])
            diff.append({'key': i, 'operation': 'nested', 'value': child})
        elif parced_data1[i] == parced_data2[i]:
            diff.append({'key': i, 'operation': 'same',
                         'value': parced_data1[i]})
        elif parced_data1[i] != parced_data2[i]:
            diff.append({'key': i, 'operation': 'changed',
                         'old': parced_data1[i],
                         'new': parced_data2[i]})
    return diff
