from typing import Any, Dict

from gendiff.diff import get_diff_view

plain_templates = {
    "added": "Property '{prefix}{key}' was added with value: {value}\n",
    "missing": "Property '{prefix}{key}' was removed\n",
    "changed": "Property '{prefix}{key}' was updated. From {value} to {ch_value}\n",
}


def convert_value_plain_format(val: Any) -> Any:
    if type(val) is int and val == 0:
        return "0"
    exceptions_to_convert: Dict[bool | None, str] = {
        False: "false",
        True: "true",
        None: "null",
    }
    if isinstance(val, dict):
        val = "[complex value]"
    else:
        val = exceptions_to_convert.get(val, f"'{val}'")
    return val


def get_diff_str_plain(
    dict1: Dict[str, Any], dict2: Dict[str, Any], prefix: str = ""
) -> str:
    diff_view = get_diff_view(dict1, dict2)
    diff_str = ""

    for key, val in diff_view.items():
        key_type = val["type"]
        value = convert_value_plain_format(val["value"])
        ch_value = convert_value_plain_format(val["changed_value"])
        key_path = prefix + key + "."

        if "added" in key_type:
            diff_str += plain_templates["added"].format(
                prefix=prefix, key=key, value=value
            )
        elif "missing" in key_type:
            diff_str += plain_templates["missing"].format(
                prefix=prefix, key=key, value=value
            )
        elif "changed" in key_type:
            diff_str += plain_templates["changed"].format(
                prefix=prefix, key=key, value=value, ch_value=ch_value
            )
        elif key_type == "nested":
            diff_str += get_diff_str_plain(dict1[key], dict2[key], prefix=key_path)

    return diff_str


def decorate_plain_diff(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> str:
    return get_diff_str_plain(dict1, dict2).rstrip("\n")
