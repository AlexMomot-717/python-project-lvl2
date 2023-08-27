from typing import Any, Dict, Set

from gendiff.file_operations import parse_file


def get_keys_groups(
    dict1: Dict[str, Any], dict2: Dict[str, Any]
) -> Dict[str, Set[str]]:
    keys1_set = set(dict1.keys())
    keys2_set = set(dict2.keys())

    union = keys1_set | keys2_set
    common = keys1_set & keys2_set
    missing = keys1_set - common

    return {
        "union": union,
        "common": common,
        "missing": missing,
    }


def get_diff_str(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> str:
    keys_groups = get_keys_groups(dict1, dict2)
    output_str = "{\n"

    for b in sorted(list(keys_groups["union"])):
        if b in keys_groups["common"] and dict2[b] == dict1[b]:
            output_str += f"      {b}: {dict2[b]}\n"
        elif b in keys_groups["common"] and dict2[b] != dict1[b]:
            output_str += f"    + {b}: {dict2[b]}\n"
            output_str += f"    - {b}: {dict1[b]}\n"
        elif b in keys_groups["missing"]:
            output_str += f"    - {b}: {dict1[b]}\n"
        else:
            output_str += f"    + {b}: {dict2[b]}\n"

    output_str += "}"
    return output_str


def generate_diff(first_file: str, second_file: str) -> Any:
    f1 = parse_file(first_file)
    f2 = parse_file(second_file)
    output_str = get_diff_str(f1, f2)
    return output_str.lower()