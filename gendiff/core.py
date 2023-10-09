from gendiff.file_operations import parse_file
from gendiff.formats.plain import decorate_plain_diff
from gendiff.formats.stylish import get_diff_str_nested


def generate_diff(
    first_file: str, second_file: str, format_name: str = "stylish"
) -> str:
    f1 = parse_file(first_file)
    f2 = parse_file(second_file)
    if format_name == "plain":
        return decorate_plain_diff(f1, f2)
    return get_diff_str_nested(f1, f2)
