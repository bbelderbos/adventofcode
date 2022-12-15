from pathlib import Path

from script import solution_part1, solution_part2

EXERCISE_SAMPLE = """
forward 5
down 5
forward 8
up 3
down 8
forward 2
""".strip()
EXERCISE_FILE_CONTENT = (Path(__file__).parent / "input.txt").read_text()
EXPECTED_SAMPLE_P1 = 150
EXPECTED_FILE_P1 = 1804520
EXPECTED_SAMPLE_P2 = 900
EXPECTED_FILE_P2 = 1971095320


def test_p1_sample():
    assert solution_part1(EXERCISE_SAMPLE) == EXPECTED_SAMPLE_P1


def test_p1_file():
    assert solution_part1(EXERCISE_FILE_CONTENT) == EXPECTED_FILE_P1


def test_p2_sample():
    assert solution_part2(EXERCISE_SAMPLE) == EXPECTED_SAMPLE_P2


def test_p2_file():
    assert solution_part2(EXERCISE_FILE_CONTENT) == EXPECTED_FILE_P2
