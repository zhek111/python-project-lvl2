#!/usr/bin/env python
import argparse

from gendiff.moduls.formaters.plain import plain
from gendiff.moduls.formaters.stylish import stylish
from gendiff.moduls.formaters.to_json import get_json
from gendiff.moduls.gendiff import generate_diff


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format',
                        default=stylish, help='set format of output')
    args = parser.parse_args()

    if args.format == 'plain':
        print(
            generate_diff(args.first_file, args.second_file, formater=plain))
    if args.format == 'json':
        print(
            generate_diff(args.first_file, args.second_file,
                          formater=get_json))
    if args.format == stylish or args.format == 'stylish':
        print(
            generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
