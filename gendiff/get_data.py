def get_data_from_file(path_file: str) -> tuple[str, str]:
    with open(path_file) as f:
        data = f.read()
    if path_file.endswith('.yaml') or path_file.endswith('.yml'):
        return data, 'yml'
    if path_file.endswith('.json'):
        return data, 'json'
