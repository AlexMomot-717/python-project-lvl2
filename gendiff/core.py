from gendiff.file_operations import parse_file
from gendiff.formatting import get_diff_str, get_diff_str_nested


def generate_diff(
    first_file: str, second_file: str, output_format: str = "stylish"
) -> str:
    f1 = parse_file(first_file)
    f2 = parse_file(second_file)
    if output_format == "stylish":
        return get_diff_str_nested(f1, f2)
    else:
        return get_diff_str(f1, f2)
