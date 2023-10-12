import json
from typing import Any, Dict

from gendiff.diff import get_diff_view


def get_diff_json_str(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> str:
    diff_json_data = get_diff_view(dict1, dict2)
    return json.dumps(diff_json_data, indent=4)
