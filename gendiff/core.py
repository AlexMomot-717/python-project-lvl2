from typing import Any

from gendiff.diff import get_diff_view
from gendiff.file_operations import parse_file
from gendiff.formatting import get_diff_str


def generate_diff(
    first_file: str, second_file: str, output_format: str = "stylish"
) -> Any:
    f1 = parse_file(first_file)
    f2 = parse_file(second_file)
    if output_format == "stylish":
        return get_diff_view(f1, f2)
    else:
        return get_diff_str(f1, f2)
