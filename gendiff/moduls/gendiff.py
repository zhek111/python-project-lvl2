import json

def generate_diff(path_file1, path_file2):
    file1 = json.load(open(path_file1))
    file2 = json.load(open(path_file2))
    sorted_keys = sorted(list(set(file1.keys()) | set(file2.keys())))
    result = f'{{\n'
    for i in sorted_keys:
        if i in file1 and i in file2 and file1[i] == file2[i]:
            result += f'   {i}: {file1[i]}\n'
        if i in file1 and i in file2 and file1[i] != file2[i]:
            result += f' - {i}: {file1[i]}\n + {i}: {file2[i]}\n'
        if i in file1 and i not in file2:
            result += f' - {i}: {file1[i]}\n'
        if i not in file1 and i in file2:
            result += f' + {i}: {file2[i]}\n'
    result += f'}}'
    result = result.replace('True', 'true').replace('False', 'false')
    return result

print(generate_diff('gendiff/files/file1.json', 'gendiff/files/file2.json'))