from pathlib import Path

import pytest

from script import solution_part1, solution_part2, snafu_to_decimal, decimal_to_snafu

EXERCISE_SAMPLE = """
1=-0-2
12111
2=0=
21
2=01
111
20012
112
1=-1=
1-12
12
1=
122
""".strip()
EXERCISE_FILE_CONTENT = (Path(__file__).parent / "input.txt").read_text()

EXPECTED_SAMPLE_P1 = "2=-1=0"
EXPECTED_FILE_P1 = 1
EXPECTED_SAMPLE_P2 = 2
EXPECTED_FILE_P2 = 2


@pytest.mark.parametrize("inp, expected", [
    ("2=-01", 976),
    ("1=-0-2", 1747),
    ("20012", 1257),
    ("122", 37),
])
def test_snafu_to_decimal(inp, expected):
    assert snafu_to_decimal(inp)  == expected

def test_decimal_to_snafu():
    assert decimal_to_snafu(4890)  == "2=-1=0"

def test_p1_sample():
    assert solution_part1(EXERCISE_SAMPLE) == EXPECTED_SAMPLE_P1


def test_p1_file():
    assert solution_part1(EXERCISE_FILE_CONTENT) == EXPECTED_FILE_P1


def test_p2_sample():
    assert solution_part2(EXERCISE_SAMPLE) == EXPECTED_SAMPLE_P2


def test_p2_file():
    assert solution_part2(EXERCISE_FILE_CONTENT) == EXPECTED_FILE_P2
