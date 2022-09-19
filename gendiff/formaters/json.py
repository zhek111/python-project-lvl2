import json as json_global


def json(diff: list[dict]) -> str:
    return json_global.dumps(diff)
