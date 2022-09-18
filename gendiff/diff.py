def add_pair_in_diff(diff, i, operation, **kwargs):
    diff.append({'key': i, 'operation': operation, **kwargs})


def determine_value(file1, file2, i):
    if isinstance(file1.get(i), dict) and isinstance(file2.get(i), dict):
        file1[i] = get_diff(file1[i], file2[i])


def add_data_in_diff(diff, i, file1, file2):
    if i in file1 and i not in file2:
        determine_value(file1, file1, i)
        add_pair_in_diff(diff, i, 'delete', old=file1[i])
    if i not in file1 and i in file2:
        determine_value(file2, file2, i)
        add_pair_in_diff(diff, i, 'add', new=file2[i])
    if i in file1 and i in file2 and file1[i] != file2[i]:
        determine_value(file1, file1, i)
        determine_value(file2, file2, i)
        add_pair_in_diff(diff, i, 'update', old=file1[i], new=file2[i])
    if i in file1 and i in file2 and file1[i] == file2[i]:
        determine_value(file1, file2, i)
        add_pair_in_diff(diff, i, 'none', value=file1[i])
    return diff


def get_diff(file1, file2):
    diff = []
    sorted_keys = sorted(list(set(file1.keys()) | set(file2.keys())))
    for i in sorted_keys:
        if isinstance(file1.get(i), dict) and isinstance(file2.get(i), dict):
            add_pair_in_diff(diff, i, 'none',
                             value=get_diff(file1.get(i), file2.get(i)))
        else:
            add_data_in_diff(diff, i, file1, file2)
    return diff
# Хочу убрать проверки в get_diff чтобы получилось:
# def get_diff(file1, file2):
#     diff = []
#     sorted_keys = sorted(list(set(file1.keys()) | set(file2.keys())))
#     for i in sorted_keys:
#         add_data_in_diff(diff, i, file1, file2)
#     return diff
# Т.е как то проверку isinstance убрать, добавить ее в конец add_data_in_diff.
# Возможно ли это? Я пробую, не получается упростить условие, чтобы это работ.
# если это нельзя сделать, можно add_data сократить будет)
