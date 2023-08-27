from gendiff.scripts.gendiff import generate_diff
from tests.fixtures.expected_diff import EXPECTED_DIFF
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
    expected_diff = EXPECTED_DIFF
    file1 = str(resolve_path("fixtures/file1" + ".yaml"))
    file2 = str(resolve_path("fixtures/file2" + ".json"))

    # when
    diff_yaml_json = generate_diff(file1, file2)

    # then
    assert diff_yaml_json == expected_diff
