#!/usr/bin/env python

from gendiff.diff_with_formatter import generate_diff
from gendiff.scripts.cli import parse_command


def main():
    args = parse_command()
    print(
        generate_diff(args.first_file, args.second_file, formater=args.format))


if __name__ == '__main__':
    main()
