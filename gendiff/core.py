from typing import Dict, Any

from gendiff.file_operations import parse_file
from gendiff.diff import get_diff_view


def generate_diff(first_file: str, second_file: str) -> Dict[str, Any]:
    f1 = parse_file(first_file)
    f2 = parse_file(second_file)
    output_str = get_diff_view(f1, f2)
    return output_str
