from typing import Dict, Any

import pytest

from gendiff.diff import get_keys_groups, get_diff_view
from gendiff.file_operations import parse_file
from tests.fixtures.expected_tests_results import EXPECTED_KEYS_GROUPS, EXPECTED_DIFF_VIEW
from tests.paths import resolve_path


@pytest.fixture
def dict1() -> Dict[str, Any]:
    file1 = str(resolve_path("fixtures/file1_nested.yaml"))
    dict1 = parse_file(file1)
    return dict1


@pytest.fixture
def dict2() -> Dict[str, Any]:
    file2 = str(resolve_path("fixtures/file2_nested.yaml"))
    dict2 = parse_file(file2)
    return dict2


# test checks first level keys, cause it works inside recursive function get_diff_view
def test_get_keys_groups(dict1, dict2) -> None:
    # given
    expected_keys_groups = EXPECTED_KEYS_GROUPS

    # when
    keys_groups = get_keys_groups(dict1, dict2)

    # then
    assert keys_groups == expected_keys_groups


def test_get_diff_view(dict1, dict2) -> None:
    # given
    expected_diff_view = EXPECTED_DIFF_VIEW

    # when
    diff_view = get_diff_view(dict1, dict2)

    # then
    assert diff_view == expected_diff_view
