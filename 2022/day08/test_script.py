import textwrap
from pathlib import Path

import pytest

from script import solution_part1, solution_part2

BASE_DIR = Path(__file__).parent


@pytest.fixture
def inline_sample():
    return textwrap.dedent(
        """
        30373
        25512
        65332
        33549
        35390
        """
    ).strip()


@pytest.fixture
def file_sample():
    return (BASE_DIR / "input.txt").read_text()


def test_part1_inline_sample(inline_sample):
    assert solution_part1(inline_sample) == 21


def test_part1_file_sample(file_sample):
    assert solution_part1(file_sample) == 1543


def test_part2_inline_sample(inline_sample):
    assert solution_part2(inline_sample) == 8


def test_part2_file_sample(file_sample):
    assert solution_part2(file_sample) == 595080
