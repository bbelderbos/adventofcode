from pathlib import Path

from script import total_number_of_overlapping_ranges

BASE_DIR = Path(__file__).parent

EXERCISE_SAMPLE = """
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
""".strip()


def test_part1_with_sample():
    assert total_number_of_overlapping_ranges(EXERCISE_SAMPLE) == 2


def test_part1_with_input_file():
    pairs = (BASE_DIR / "input.txt").read_text()
    assert total_number_of_overlapping_ranges(pairs) == 511
