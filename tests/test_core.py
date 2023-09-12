from gendiff.scripts.gendiff import generate_diff
from tests.fixtures.expected_diff import EXPECTED_DIFF, EXPECTED_DIFF_NESTED
from tests.paths import resolve_path


def test_generate_diff_json() -> None:
    # given
    file1 = str(resolve_path("fixtures/file1.json"))
    file2 = str(resolve_path("fixtures/file2.json"))
    expected_diff = EXPECTED_DIFF

    # when
    diff = generate_diff(file1, file2, output_format="stylish")

    # then
    assert diff == expected_diff


def test_generate_diff_yaml() -> None:
    # given
    file1 = str(resolve_path("fixtures/file1.yaml"))
    file2 = str(resolve_path("fixtures/file2.yaml"))
    expected_diff = EXPECTED_DIFF

    # when
    diff = generate_diff(file1, file2, output_format="stylish")

    # then
    assert diff == expected_diff


def test_generate_diff_mixed() -> None:
    # given
    file1 = str(resolve_path("fixtures/file1.yaml"))
    file2 = str(resolve_path("fixtures/file2.json"))
    expected_diff = EXPECTED_DIFF

    # when
    diff_yaml_json = generate_diff(file1, file2, output_format="stylish")

    # then
    assert diff_yaml_json == expected_diff


def test_generate_diff_miss_format() -> None:
    # given
    file1 = str(resolve_path("fixtures/file1.json"))
    file2 = str(resolve_path("fixtures/file2.json"))
    expected_diff = EXPECTED_DIFF

    # when
    diff = generate_diff(file1, file2)

    # then

    assert diff == expected_diff


def test_generate_diff_nested() -> None:
    # given
    file1 = str(resolve_path("fixtures/file1_nested.json"))
    file2 = str(resolve_path("fixtures/file2_nested.json"))
    expected_diff = EXPECTED_DIFF_NESTED

    # when
    diff = generate_diff(file1, file2)

    # then
    assert diff == expected_diff
