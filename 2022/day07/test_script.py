import textwrap
from pathlib import Path

import pytest

from script import solution_part1, solution_part2

BASE_DIR = Path(__file__).parent


@pytest.fixture
def inline_sample():
    return textwrap.dedent(
        """
        $ cd /
        $ ls
        dir a
        14848514 b.txt
        8504156 c.dat
        dir d
        $ cd a
        $ ls
        dir e
        29116 f
        2557 g
        62596 h.lst
        $ cd e
        $ ls
        584 i
        $ cd ..
        $ cd ..
        $ cd d
        $ ls
        4060174 j
        8033020 d.log
        5626152 d.ext
        7214296 k
        """
    ).rstrip()


@pytest.fixture
def file_sample():
    return (BASE_DIR / "input.txt").read_text()


def test_part1_inline_sample(inline_sample):
    assert solution_part1(inline_sample) == 95437


def test_part1_file_sample(file_sample):
    assert solution_part1(file_sample) == 1297159


def test_part2_inline_sample(inline_sample):
    assert solution_part2(inline_sample) == 24933642


def test_part2_file_sample(file_sample):
    assert solution_part2(file_sample) == 3866390
