import textwrap
from pathlib import Path

import pytest

from script import get_top_level_crates

BASE_DIR = Path(__file__).parent


@pytest.fixture
def inline_sample():
    return textwrap.dedent(
        """
        [D]
    [N] [C]
    [Z] [M] [P]
    1   2   3

    move 1 from 2 to 1
    move 3 from 1 to 3
    move 2 from 2 to 1
    move 1 from 1 to 2
    """
    ).rstrip()


@pytest.fixture
def file_sample():
    return (BASE_DIR / "input.txt").read_text()


def test_part1_inline_sample(inline_sample):
    assert get_top_level_crates(inline_sample) == "CMZ"


def test_part1_file_sample(file_sample):
    assert get_top_level_crates(file_sample) == "FCVRLMVQP"
