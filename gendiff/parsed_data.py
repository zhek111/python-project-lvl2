import json
import yaml


def parse(data: str, format: str) -> dict:
    if format == 'yml':
        return yaml.safe_load(data)
    if format == 'json':
        return json.loads(data)
    raise ValueError(f"Unrecognized format: {format}")
