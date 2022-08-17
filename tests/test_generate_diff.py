from gendiff import generate_diff
import pytest


def test_generare_diff_for_empty_file():
    with open('tests/fixtures/Result12.txt', 'r') as file:
        a = file.read()
    assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json') == a


    #     '''{
    #  - follow: false
    #    host: hexlet.io
    #  - proxy: 123.234.53.22
    #  - timeout: 50
    #  + timeout: 20
    #  + verbose: true
    # }'''

    #
    #
    # def test_stack():
    #     stack = []
    #     stack.append('one')
    #     stack.append('two')
    #
    #     assert stack.pop() == 'two'
    #     assert stack.pop() == 'one'
    #
    #
    # def test_emptiness():
    #     stack = []
    #     assert not stack
    #     stack.append('one')
    #     assert bool(stack)
    #     stack.pop()
    #     assert not stack
    #
    #
    # def test_pop_with_empty_stack():
    #     stack = []
    #     with pytest.raises(IndexError):
    #         stack.pop()
