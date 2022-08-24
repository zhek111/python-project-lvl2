def get_diff(file1, file2):
    diff = {}
    sorted_keys = sorted(list(set(file1.keys()) | set(file2.keys())))
    for i in sorted_keys:
        if not type(file1.get(i)) == type(file2.get(i)) == dict:
            if i in file1 and i in file2 and file1[i] != file2[i]:
                diff[f'ch-.{i}'] = file1[i]
                diff[f'ch+.{i}'] = file2[i]
            if i in file1 and i not in file2:
                diff[f'del.{i}'] = file1[i]
            if i not in file1 and i in file2:
                diff[f'add.{i}'] = file2[i]
            if i in file1 and i in file2 and file1[i] == file2[i]:
                diff[i] = file1[i]
        if type(file1.get(i)) == type(file2.get(i)) == dict:
            children1 = file1.get(i)
            children2 = file2.get(i)
            new_value = get_diff(children1, children2)
            diff[i] = new_value
    return diff
