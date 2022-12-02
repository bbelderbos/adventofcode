import pathlib

import pytest

from script import ElfCalories

EXERCISE_INLINE_EXAMPLE = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""
BASE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def test_data_path1():
    return BASE_DIR / "elf-calories.txt"


@pytest.fixture
def test_data_path2(tmp_path):
    path = pathlib.Path(tmp_path) / "data.txt"
    path.write_text(EXERCISE_INLINE_EXAMPLE)
    return path


@pytest.fixture
def elf_kcal1(test_data_path1):
    return ElfCalories(test_data_path1)


@pytest.fixture
def elf_kcal2(test_data_path2):
    return ElfCalories(test_data_path2)


@pytest.mark.parametrize(
    "fixture_name, expected",
    [
        ("elf_kcal1", 72602),
        ("elf_kcal2", 24000),
    ],
)
def test_part1(request, fixture_name, expected):
    elf_instance = request.getfixturevalue(fixture_name)
    assert elf_instance.get_max_kcal_elves() == expected


@pytest.mark.parametrize(
    "fixture_name, expected",
    [
        ("elf_kcal1", 207410),
        ("elf_kcal2", 45000),
    ],
)
def test_part2(request, fixture_name, expected):
    elf_instance = request.getfixturevalue(fixture_name)
    assert elf_instance.get_total_kcal_top_elves() == expected
