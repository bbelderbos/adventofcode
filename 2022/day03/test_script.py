from pathlib import Path

from script import get_total_sum_of_priorities

BASE_DIR = Path(__file__).parent


def test_example_rugsacks():
    all_rugsacks = """
    vJrwpWtwJgWrhcsFMMfFFhFp
    jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
    PmmdzqPrVvPwwTWBwg
    wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
    ttgJtRGJQctTZtZT
    CrZsJsPPZsGzwwsLwLmpwMDw
    """.strip()
    total = get_total_sum_of_priorities(all_rugsacks)
    assert total == 157


def test_part1_solution():
    all_rugsacks = (BASE_DIR / "input.txt").read_text()
    total = get_total_sum_of_priorities(all_rugsacks)
    assert total == 7903
