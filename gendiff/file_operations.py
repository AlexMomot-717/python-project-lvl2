import json
from typing import Any, Dict

import yaml
from yaml.loader import SafeLoader


def get_file_extension(file_name: str) -> str:
    if file_name.endswith(".json"):
        extension = "json"
    elif file_name.endswith(".yaml") or file_name.endswith(".yml"):
        extension = "yaml"
    else:
        raise Exception("Unsupported file format!")
    return extension


def parse_file(file_name: str) -> Dict[str, Any]:
    extension = get_file_extension(file_name)
    with open(file_name, "r") as f:
        if extension == "json":
            result = dict(json.load(f))
        else:
            result = dict(yaml.load(f, Loader=SafeLoader))
    return result
