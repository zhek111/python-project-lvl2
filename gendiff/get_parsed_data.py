import json
import yaml


def get_parsed_data(data: str, format: str) -> dict:
    if format == 'yml':
        return yaml.safe_load(data)
    if format == 'json':
        return json.loads(data)
    raise ValueError('wrong value')
