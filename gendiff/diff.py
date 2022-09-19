def add_pair_in_diff(diff: list, i: str, operation: str, **kwargs):
    diff.append({'key': i, 'operation': operation, **kwargs})


def determine_value(parced_data1: dict, parced_data2: dict, i: str):
    if isinstance(
            parced_data1.get(i), dict) and isinstance(
            parced_data2.get(i), dict):
        parced_data1[i] = get_diff(parced_data1[i], parced_data2[i])


def add_data_in_diff(
        diff: list,
        i: str,
        parced_data1: dict,
        parced_data2: dict
) -> list[dict]:
    if i not in parced_data2:
        determine_value(parced_data1, parced_data1, i)
        add_pair_in_diff(diff, i, 'delete', old=parced_data1[i])
    if i not in parced_data1:
        determine_value(parced_data2, parced_data2, i)
        add_pair_in_diff(diff, i, 'add', new=parced_data2[i])
    if i in parced_data1 and i in parced_data2 and \
            parced_data1.get(i) != parced_data2.get(i):
        determine_value(parced_data1, parced_data1, i)
        determine_value(parced_data2, parced_data2, i)
        add_pair_in_diff(diff, i, 'update', old=parced_data1[i],
                         new=parced_data2[i])
    if i in parced_data1 and i in parced_data2 and parced_data1[i] == \
            parced_data2[i]:
        determine_value(parced_data1, parced_data2, i)
        add_pair_in_diff(diff, i, 'none', value=parced_data1[i])
    return diff


def get_diff(parced_data1: dict, parced_data2: dict) -> list[dict]:
    diff = []
    sorted_keys = sorted(
        list(set(parced_data1.keys()) | set(parced_data2.keys()))
    )
    for i in sorted_keys:
        if isinstance(parced_data1.get(i), dict) and \
                isinstance(parced_data2.get(i), dict):
            add_pair_in_diff(diff, i, 'none', value=get_diff(
                parced_data1.get(i),
                parced_data2.get(i)))
        else:
            add_data_in_diff(diff, i, parced_data1, parced_data2)
    return diff
# Хочу убрать проверки в get_diff чтобы получилось:
# def get_diff(file1, file2):
#     diff = []
#     sorted_keys = sorted(list(set(file1.keys()) | set(file2.keys())))
#     for i in sorted_keys:
#         add_data_in_diff(diff, i, file1, file2)
#     return diff
# Т.е както проверку isinstance убрать(43-48), но что то чуть изменить в конце
# add_data_in_diff.
# Возможно ли это? Я пробую, не получается.
# если это нельзя сделать, можно add_data сократить будет)
