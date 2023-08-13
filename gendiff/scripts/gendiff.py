#!/usr/bin/env python3
import argparse
import json


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


def generate_diff(first_file: str, second_file: str) -> str:
    with (
        open(first_file, "r") as file1,
        open(second_file, "r") as file2,
    ):
        f1 = json.load(file1)
        f2 = json.load(file2)

    keys1_set = set(f1.keys())
    keys2_set = set(f2.keys())
    sorted_list = sorted(list(keys1_set | keys2_set))
    common_keys = keys1_set & keys2_set
    missing_keys = keys1_set - common_keys

    output_str = "{\n"
    for b in sorted_list:
        if b in common_keys and f2[b] == f1[b]:
            output_str += f"      {b}: {f2[b]})\n"
        elif b in common_keys and f2[b] != f1[b]:
            output_str += f"    + {b}: {f2[b]})\n"
            output_str += f"    - {b}: {f1[b]})\n"
        elif b in missing_keys:
            output_str += f"    - {b}: {f1[b]})\n"
        else:
            output_str += f"    + {b}: {f2[b]})\n"
    output_str += "}"
    return output_str.lower()


def main() -> None:
    args = get_args_parser()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__ == "main":
    main()
