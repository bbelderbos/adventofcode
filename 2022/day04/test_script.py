from pathlib import Path

from script import calculate_number_of_overlaps, has_any_overlap

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
    assert calculate_number_of_overlaps(EXERCISE_SAMPLE) == 2


def test_part1_with_input_file():
    pairs = (BASE_DIR / "input.txt").read_text()
    assert calculate_number_of_overlaps(pairs) == 511


def test_part2_with_sample():
    assert calculate_number_of_overlaps(EXERCISE_SAMPLE, overlap=has_any_overlap) == 4


def test_part2_with_input_file():
    pairs = (BASE_DIR / "input.txt").read_text()
    assert calculate_number_of_overlaps(pairs, overlap=has_any_overlap) == 821
