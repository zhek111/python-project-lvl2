def get_diff(file1, file2):
    diff = []
    sorted_keys = sorted(list(set(file1.keys()) | set(file2.keys())))
    for i in sorted_keys:
        if not (isinstance(file1.get(i), dict) and isinstance(file2.get(i),
                                                              dict)):
            if i in file1 and i in file2 and file1[i] != file2[i]:
                diff.append({'key': i, 'operation': 'update', 'old': file1[i],
                             'new': file2[i]})
            if i in file1 and i not in file2:
                diff.append({'key': i, 'operation': 'delete', 'old': file1[i]})
            if i not in file1 and i in file2:
                diff.append(
                    {'key': i, 'operation': 'addition', 'new': file2[i]})
            if i in file1 and i in file2 and file1[i] == file2[i]:
                diff.append(
                    {'key': i, 'operation': 'nothing', 'value': file2[i]})
        if isinstance(file1.get(i), dict) and isinstance(file2.get(i), dict):
            children1 = file1.get(i)
            children2 = file2.get(i)
            new_value = get_diff(children1, children2)
            diff.append({'key': i, 'operation': 'nothing', 'value': new_value})
        if isinstance(file1.get(i), dict) and not isinstance(file2.get(i),
                                                             dict):
            children1 = file1.get(i)
            children2 = file1.get(i)
            new_value = get_diff(children1, children2)
            for d in diff:
                if d.get('key') == i:
                    if d.get('old'):
                        d['old'] = new_value
        if not isinstance(file1.get(i), dict) and isinstance(file2.get(i),
                                                             dict):
            children1 = file2.get(i)
            children2 = file2.get(i)
            new_value = get_diff(children1, children2)
            for d in diff:
                if d.get('key') == i:
                    d['new'] = new_value
    return diff
