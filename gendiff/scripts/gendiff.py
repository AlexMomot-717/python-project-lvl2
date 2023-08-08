#!/usr/bin/env python3
import argparse


def main():
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
    print(parser, args)


if __name__ == "main":
    main()
