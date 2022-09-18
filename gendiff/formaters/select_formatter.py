from gendiff.formaters.stylish import stylish
from gendiff.formaters.plain import plain
from gendiff.formaters.json import json


def select_formatter(formater):
    if formater == 'stylish':
        return stylish
    if formater == 'plain':
        return plain
    if formater == 'json':
        return json
