DEFAULT_INDENT = 4
DEFAULT_DEPTH = 0


def line_forming(i: dict, value: str, depth: int, sign: str) -> str:
    if isinstance(i[value], list):
        i[value] = stylish(i[value], depth + DEFAULT_INDENT)
    return f'{" " * depth}{sign}{i["key"]}: {i[value]}\n'


def stylish(diff: list[dict], depth=DEFAULT_DEPTH) -> str:
    text = '{\n'
    for i in diff:
        if i['operation'] == 'none':
            text += line_forming(i, 'value', depth, sign='    ')
        if i['operation'] == 'add':
            text += line_forming(i, 'new', depth, sign='  + ')
        if i['operation'] == 'delete' or i['operation'] == 'update':
            text += line_forming(i, 'old', depth, sign='  - ')
        if i['operation'] == 'update':
            text += line_forming(i, 'new', depth, sign='  + ')
    text += f'{" " * depth}}}'
    text = text.replace('True', 'true').replace(
        'False', 'false').replace('None', 'null')
    return text
# Хотелось бы в 21-ой строчке кода вызвать 17-ую. Кроме, как через создание
# переменной это возможно?
# нужно лл функцию line_formating разделять на две? на проверяющую
# и изменяющую значение строки, и на возвращающую текст?
