from typing import Any, Dict, Set

from gendiff.diff import get_diff_view


def get_keys_groups_simple(
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
    keys_groups = get_keys_groups_simple(dict1, dict2)
    output_str = "{\n"

    for b in sorted(list(keys_groups["union"])):
        if b in keys_groups["common"] and dict2[b] == dict1[b]:
            output_str += f"      {b}: {dict2[b]}\n"
        elif b in keys_groups["common"] and dict2[b] != dict1[b]:
            output_str += f"    - {b}: {dict1[b]}\n"
            output_str += f"    + {b}: {dict2[b]}\n"
        elif b in keys_groups["missing"]:
            output_str += f"    - {b}: {dict1[b]}\n"
        else:
            output_str += f"    + {b}: {dict2[b]}\n"

    output_str += "}"
    return output_str.lower()


diffs_templates = {
    "missing": "{indent}- {key}:{space}{value}\n",
    "added": "{indent}+ {key}:{space}{value}\n",
    "no_change": "{indent}  {key}:{space}{value}\n",
    "nested": "{indent}  {key}: {{\n{value}{indent}  }}\n",
    "missing_nested": "{indent}- {key}: {{\n{value}{indent}  }}\n",
    "added_nested": "{indent}+ {key}: {{\n{value}{indent}  }}\n",
}


def convert_value(val: Any) -> Any:
    exceptions_to_convert = {False: "false", True: "true", None: "null"}
    return exceptions_to_convert.get(val, val) if not isinstance(val, dict) else val


def plain_diff(key_type: str, indent: int, key: str, value: Any) -> str:
    value = convert_value(value)
    space = "" if value == "" else " "
    plain_diff_str = diffs_templates[key_type].format(
        indent=indent * " ", key=key, space=space, value=value
    )

    return plain_diff_str


def nested_diff(
    key_type: str, indent: int, key: str, value: Any = None, ch_value: Any = None
) -> str:
    plain_before = plain_after = ""
    if key_type == "changed_nested_1":
        plain_after = plain_diff(
            key_type="added",
            key=key,
            indent=indent,
            value=ch_value,
        )
        key_type = "missing_nested"

    if key_type == "changed_nested_2":
        plain_before = plain_diff(
            key_type="missing",
            key=key,
            indent=indent,
            value=ch_value,
        )
        key_type = "added_nested"

    nested_diff_str = diffs_templates[key_type].format(
        indent=indent * " ", key=key, value=value
    )
    nested_diff_str = plain_before + nested_diff_str + plain_after
    return nested_diff_str


def get_diff_str_nested(
    dict1: Dict[str, Any], dict2: Dict[str, Any], indent: int = 2
) -> str:
    diff_view = get_diff_view(dict1, dict2)
    diff_str = "{\n" if indent == 2 else ""

    for key, val in diff_view.items():
        key_type = val["type"]
        value = val["value"]
        ch_value = val["changed_value"]

        if key_type.endswith("nested"):
            if key_type == "nested":
                d1 = dict1[key]
                d2 = dict2[key]
            elif key_type == "missing_nested":
                d1 = d2 = dict1[key]
            elif key_type == "added_nested":
                d1 = d2 = dict2[key]
            else:
                if isinstance(dict1[key], dict):
                    key_type = "changed_nested_1"
                    d1 = d2 = dict1[key]
                    ch_value = dict2[key]
                else:
                    key_type = "changed_nested_2"
                    d1 = d2 = dict2[key]
                    ch_value = dict1[key]

            value = get_diff_str_nested(d1, d2, indent=indent + 4)
            diff_str += nested_diff(
                key_type=key_type,
                indent=indent,
                key=key,
                value=value,
                ch_value=ch_value,
            )
        else:
            if key_type == "changed":
                key_type = "missing"
                diff_str += plain_diff(
                    key_type=key_type,
                    indent=indent,
                    key=key,
                    value=value,
                )
                key_type = "added"
                value = ch_value

            diff_str += plain_diff(
                key_type=key_type,
                indent=indent,
                key=key,
                value=value,
            )

    diff_str += "}" if indent == 2 else ""
    return diff_str
