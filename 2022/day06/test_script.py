from pathlib import Path

import pytest

from script import solution_part1

BASE_DIR = Path(__file__).parent


@pytest.fixture
def file_sample():
    return (BASE_DIR / "input.txt").read_text()


@pytest.mark.parametrize(
    "inp, expected",
    [
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
        ("nppdvjthqldpwncqszvftbrmjlhg", 6),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11),
    ],
)
def test_part1_exercise_samples(inp, expected):
    assert solution_part1(inp) == expected


def test_part1_file_sample(file_sample):
    assert solution_part1(file_sample) == 1235


@pytest.mark.parametrize(
    "inp, expected",
    [
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 23),
        ("nppdvjthqldpwncqszvftbrmjlhg", 23),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 26),
    ],
)
def test_part2_exercise_samples(inp, expected):
    assert solution_part1(inp, marker_length=14) == expected


def test_part2_file_sample(file_sample):
    assert solution_part1(file_sample, marker_length=14) == 3051
