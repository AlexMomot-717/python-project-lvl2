from typing import Any, Dict, Set

from gendiff.file_operations import parse_file
from tests.paths import resolve_path


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
        "new": keys2_set - common
    }


def get_diff_view(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    keys_groups = get_keys_groups(dict1, dict2)
    diff_view: dict[str, Any] = {}
    for key in sorted(list(keys_groups["union"])):
        if key in keys_groups["common"]:
            if dict2[key] == dict1[key]:
                key_type = "no_change"
                value = dict1[key]
                changed_value = value
            else:
                if isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
                    key_type = "changed_nested"
                    value = dict1[key]
                    changed_value = get_diff_view(value, dict2[key])
                else:
                    key_type = "changed"
                    value = dict1[key]
                    changed_value = dict2[key]
        elif key in keys_groups["missing"]:
            if isinstance(dict1[key], dict):
                key_type = "missing_nested"
            else:
                key_type = "missing"
            value = dict1[key]
            changed_value = ""
        else:
            if isinstance(dict2[key], dict):
                key_type = "added_nested"
            else:
                key_type = "added"
            value = ""
            changed_value = dict2[key]

        diff_view[key] = {
            "type": key_type,
            "value": value,
            "changed_value": changed_value
        }
    return diff_view
