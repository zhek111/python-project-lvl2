from os.path import splitext


def prepare_data(path_file: str) -> tuple[str, str]:
    with open(path_file) as f:
        data = f.read()
        if splitext(path_file)[1] == '.yaml' or splitext(
                path_file)[1] == '.yml':
            return data, 'yml'
        if splitext(path_file)[1] == '.json':
            return data, 'json'
