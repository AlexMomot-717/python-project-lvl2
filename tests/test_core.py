from gendiff.core import generate_diff
from tests.fixtures.expected_diffs import (
    EXPECTED_DIFF,
    EXPECTED_DIFF_NESTED,
    EXPECTED_DIFF_PLAIN,
)
from tests.paths import resolve_path


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


def test_generate_diff_nested() -> None:
    # given
    file1 = str(resolve_path("fixtures/file1_nested.json"))
    file2 = str(resolve_path("fixtures/file2_nested.json"))

    # when
    diff = generate_diff(file1, file2)

    # then
    expected_diff = EXPECTED_DIFF_NESTED
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
