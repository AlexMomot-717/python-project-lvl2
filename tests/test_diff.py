from typing import Any, Dict

import pytest
from gendiff.diff import get_diff_view, get_keys_groups
from gendiff.file_operations import parse_file
from tests.fixtures.expected_dicts import (
    EXPECTED_DIFF_VIEW,
    EXPECTED_KEYS_GROUPS,
)
from tests.paths import resolve_path


@pytest.fixture
def dict1() -> Dict[str, Any]:
    file1 = str(resolve_path("fixtures/file1_nested.json"))
    dict1 = parse_file(file1)
    return dict1


@pytest.fixture
def dict2() -> Dict[str, Any]:
    file2 = str(resolve_path("fixtures/file2_nested.json"))
    dict2 = parse_file(file2)
    return dict2


def test_get_keys_groups(dict1, dict2) -> None:
    # when
    keys_groups = get_keys_groups(dict1, dict2)

    # then
    expected_keys_groups = EXPECTED_KEYS_GROUPS
    assert keys_groups == expected_keys_groups


def test_get_diff_view(dict1, dict2) -> None:
    # when
    diff_view = get_diff_view(dict1, dict2)

    # then
    expected_diff_view = EXPECTED_DIFF_VIEW
    assert diff_view == expected_diff_view
