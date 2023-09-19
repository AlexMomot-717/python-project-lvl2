from typing import Any, Dict


def get_keys_groups(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> dict[str, str]:
    keys1_set = set(dict1.keys())
    keys2_set = set(dict2.keys())

    common = keys1_set & keys2_set
    missing = keys1_set - common
    added = keys2_set - common
    keys_groups = {}

    for key in common:
        if isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
            keys_groups[key] = "nested"
        elif isinstance(dict1[key], dict) or isinstance(dict2[key], dict):
            keys_groups[key] = "changed_nested"
        elif dict1[key] == dict2[key]:
            keys_groups[key] = "no_change"
        else:
            keys_groups[key] = "changed"
    for key in missing:
        if isinstance(dict1[key], dict):
            keys_groups[key] = "missing_nested"
        else:
            keys_groups[key] = "missing"
    for key in added:
        if isinstance(dict2[key], dict):
            keys_groups[key] = "added_nested"
        else:
            keys_groups[key] = "added"

    return keys_groups


def get_diff_view(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    keys_groups = get_keys_groups(dict1, dict2)
    diff_view: dict[str, Dict[str, Any]] = {}
    for key, key_type in keys_groups.items():
        value, changed_value = None, None

        if key_type in ("no_change", "missing"):
            value = dict1[key]
        elif key_type == "added":
            value = dict2[key]
        elif key_type == "changed":
            value = dict1[key]
            changed_value = dict2[key]
        elif key_type == "added_nested":
            value = get_diff_view(dict2[key], dict2[key])
        elif key_type == "missing_nested":
            value = get_diff_view(dict1[key], dict1[key])
        elif key_type == "nested":
            value = get_diff_view(dict1[key], dict2[key])
        elif key_type == "changed_nested":
            if isinstance(dict1, dict):
                value = get_diff_view(dict1[key], dict1[key])
                changed_value = dict2[key]
            else:
                value = dict1[key]
                changed_value = get_diff_view(dict2[key], dict2[key])

        diff_view[key] = {
            "type": key_type,
            "value": value,
            "changed_value": changed_value,
        }
    return dict(sorted(diff_view.items()))
