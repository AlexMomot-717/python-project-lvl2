from typing import Any, Dict, Set

from gendiff.file_operations import parse_file


def get_keys_groups(
    dict1: Dict[str, Any], dict2: Dict[str, Any]
) -> Dict[str, Set[str]]:
    keys1_set = set(dict1.keys())
    keys2_set = set(dict2.keys())

    union = keys1_set | keys2_set
    common = keys1_set & keys2_set

    return {
        "union": union,
        "common": common,
        "missing": keys1_set - common,
        "new": keys2_set - common,
    }


def get_diff_view(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    keys_groups = get_keys_groups(dict1, dict2)
    diff_view: dict[str, Any] = {}
    for key in sorted(list(keys_groups["union"])):
        if key in keys_groups["common"]:
            if dict2[key] == dict1[key]:
                diff_view[key] = "equal"
            else:
                if isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
                    diff_view[key] = get_diff_view(dict1[key], dict2[key])
                else:
                    diff_view[key] = "common_diff"
        elif key in keys_groups["missing"]:
            diff_view[key] = "missing"
        else:
            diff_view[key] = "new"
    return diff_view


def convert_value(val: Any) -> Any:
    if not isinstance(val, bool | None):
        return val
    exceptions_to_convert = {False: "false", True: "true", None: "null"}
    return exceptions_to_convert[val]


def extruct_items(dict_obj: Dict[str, Any], depth: int) -> str:
    items_str = ""
    for key, val in dict_obj.items():
        if isinstance(val, dict):
            val = extruct_items(val, depth=depth + 1)
        items_str += f"{' ' * 4 * depth}{key}: {val}\n"
    return items_str


def formatted_items_str(depth: int, key: str, val: Any, special_char: str) -> str:
    output_str = ""
    val = convert_value(val)
    if isinstance(val, dict):
        val = extruct_items(val, depth=depth + 1)
        output_str += f"{' ' * 3 * depth}{special_char}{key}: {{\n"
        output_str += f"{val}"
        output_str += f"{' ' * 3 * depth}  }}\n"
    else:
        if depth != 1:
            output_str += f"{' ' * 3 * depth}{special_char}{key}: {val}\n"
        else:
            output_str += f"{' ' * 2 * depth}{special_char}{key}: {val}\n"
    return output_str


def get_diff_str(
    diff_view: Dict[str, Any],
    dict1: Dict[str, Any],
    dict2: Dict[str, Any],
    depth: int = 1,
) -> str:
    output_str = "{\n"
    for key in diff_view.keys():
        if diff_view[key] == "equal":
            special_char = "  "
            val = dict2[key]
        elif diff_view[key] == "common_diff":
            output_str += formatted_items_str(
                depth=depth, key=key, val=dict1[key], special_char="- "
            )
            special_char = "+ "
            val = dict2[key]
        elif diff_view[key] == "missing":
            special_char = "- "
            val = dict1[key]
        elif diff_view[key] == "new":
            special_char = "+ "
            val = dict2[key]
        else:
            val = get_diff_str(diff_view[key], dict1[key], dict2[key], depth=depth + 1)
            special_char = "  "

        output_str += formatted_items_str(
            depth=depth, key=key, val=val, special_char=special_char
        )

    return output_str + ("}" if depth == 1 else "  " * (depth + 1) + "}")


def generate_diff(
    first_file: str, second_file: str, output_format: str = "stylish"
) -> str:
    f1 = parse_file(first_file)
    f2 = parse_file(second_file)
    diff_view = get_diff_view(f1, f2)
    if output_format == "stylish":
        diff_output = get_diff_str(diff_view, f1, f2)
    else:
        diff_output = ""
    return diff_output
