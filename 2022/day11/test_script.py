from pathlib import Path

from script import solution_part1, solution_part2

EXERCISE_SAMPLE = """
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
""".strip()
EXERCISE_FILE_CONTENT = (Path(__file__).parent / "input.txt").read_text()

EXPECTED_SAMPLE_P1 = 10605
EXPECTED_FILE_P1 = 64032
EXPECTED_SAMPLE_P2 = 2713310158
EXPECTED_FILE_P2 = 2


def test_p1_sample():
    assert solution_part1(EXERCISE_SAMPLE) == EXPECTED_SAMPLE_P1


def test_p1_file():
    assert solution_part1(EXERCISE_FILE_CONTENT) == EXPECTED_FILE_P1


def test_p2_sample_smaller():
    assert solution_part2(EXERCISE_SAMPLE, rounds=20) == 10197


def test_p2_sample():
    assert solution_part2(EXERCISE_SAMPLE) == EXPECTED_SAMPLE_P2


# def test_p2_file():
#    assert solution_part2(EXERCISE_FILE_CONTENT) == EXPECTED_FILE_P2
