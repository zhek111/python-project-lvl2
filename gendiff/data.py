from os.path import splitext


def prepare_data(path_file: str) -> tuple[str, str]:
    extension = splitext(path_file)[1]
    extensions = ('.yaml', '.yml', '.json')
    if extension in extensions:
        with open(path_file) as f:
            data = f.read()
            if extension == '.yaml' or extension == '.yml':
                return data, extension
            if extension == '.json':
                return data, extension
    raise ValueError(f"Unrecognized extension: {extension}")
