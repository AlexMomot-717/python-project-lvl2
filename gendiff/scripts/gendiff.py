#!/usr/bin/env python3
import argparse

from gendiff.core import generate_diff


def get_args_parser() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="gendiff",
        description="Compares two configuration files and shows a difference.",
    )
    parser.add_argument("first_file", type=str)
    parser.add_argument("second_file", type=str)
    parser.add_argument(
        "-f",
        "--format",
        type=str,
        help="set format of output",
    )
    args = parser.parse_args()
    return args


def main() -> None:
    args = get_args_parser()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__ == "main":
    main()
