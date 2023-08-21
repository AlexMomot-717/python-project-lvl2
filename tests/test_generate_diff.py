from gendiff.scripts.gendiff import generate_diff
from tests.fixtures.expected_diff import EXPECTED_DIFF
from tests.paths import resolve_path


def test_generate_diff() -> None:
    # given
    file1 = str(resolve_path("fixtures/file1.json"))
    file2 = str(resolve_path("fixtures/file2.json"))

    # when
    diff = generate_diff(file1, file2)

    # then
    expected_diff = EXPECTED_DIFF
    assert diff == expected_diff
