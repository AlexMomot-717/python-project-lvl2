import pytest
from gendiff.core import generate_diff
from tests.fixtures.expected_diffs import (
    EXPECTED_DIFF,
    EXPECTED_DIFF_JSON,
    EXPECTED_DIFF_PLAIN,
)
from tests.paths import resolve_path


@pytest.fixture
def diff_nested() -> str:
    with open("tests/fixtures/expected_diff_nested.txt", "r") as diff_file:
        diff = diff_file.read()
    return diff


def test_generate_diff_json() -> None:
    # given
    file1 = str(resolve_path("fixtures/file1.json"))
    file2 = str(resolve_path("fixtures/file2.json"))

    # when
    diff = generate_diff(file1, file2)

    # then
    expected_diff = EXPECTED_DIFF
    assert diff == expected_diff


def test_generate_diff_yaml() -> None:
    # given
    file1 = str(resolve_path("fixtures/file1.yaml"))
    file2 = str(resolve_path("fixtures/file2.yaml"))

    # when
    diff = generate_diff(file1, file2)

    # then
    expected_diff = EXPECTED_DIFF
    assert diff == expected_diff


def test_generate_diff_mixed() -> None:
    # given
    file1 = str(resolve_path("fixtures/file1.yaml"))
    file2 = str(resolve_path("fixtures/file2.json"))

    # when
    diff_yaml_json = generate_diff(file1, file2)

    # then
    expected_diff = EXPECTED_DIFF
    assert diff_yaml_json == expected_diff


def test_generate_diff_nested(diff_nested) -> None:
    # given
    file1 = str(resolve_path("fixtures/file1_nested.json"))
    file2 = str(resolve_path("fixtures/file2_nested.json"))

    # when
    diff = generate_diff(file1, file2)

    # then
    expected_diff = diff_nested
    assert diff == expected_diff


def test_generate_diff_plain() -> None:
    # given
    file1 = str(resolve_path("fixtures/file1_nested.json"))
    file2 = str(resolve_path("fixtures/file2_nested.json"))
    format_name = "plain"

    # when
    diff = generate_diff(file1, file2, format_name=format_name)

    # then
    expected_diff = EXPECTED_DIFF_PLAIN
    assert diff == expected_diff


def test_generate_diff_json_format() -> None:
    # given
    file1 = str(resolve_path("fixtures/file1_nested.json"))
    file2 = str(resolve_path("fixtures/file2_nested.json"))
    format_name = "json"

    # when
    diff = generate_diff(file1, file2, format_name=format_name)

    # then
    expected_diff = EXPECTED_DIFF_JSON
    assert diff == expected_diff
