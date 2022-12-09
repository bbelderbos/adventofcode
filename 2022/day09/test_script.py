from pathlib import Path

from script import solution_part1, solution_part2

EXERCISE_SAMPLE = """
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
""".strip()
EXERCISE_FILE_CONTENT = (Path(__file__).parent / "input.txt").read_text()

EXPECTED_SAMPLE_P1 = 13
EXPECTED_FILE_P1 = 6494
EXPECTED_SAMPLE_P2 = 2
EXPECTED_FILE_P2 = 2


def test_p1_sample():
    assert solution_part1(EXERCISE_SAMPLE) == EXPECTED_SAMPLE_P1


def test_p1_file():
    assert solution_part1(EXERCISE_FILE_CONTENT) == EXPECTED_FILE_P1


def test_p2_sample():
    assert solution_part2(EXERCISE_SAMPLE) == EXPECTED_SAMPLE_P2


def test_p2_file():
    assert solution_part2(EXERCISE_FILE_CONTENT) == EXPECTED_FILE_P2
