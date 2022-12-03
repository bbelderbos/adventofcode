from pathlib import Path

from script import get_total_group_common_items, get_total_sum_of_priorities

BASE_DIR = Path(__file__).parent


def test_example_rugsacks_part1():
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


def test_example_rugsacks_part2():
    all_rugsacks = """
    vJrwpWtwJgWrhcsFMMfFFhFp
    jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
    PmmdzqPrVvPwwTWBwg
    wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
    ttgJtRGJQctTZtZT
    CrZsJsPPZsGzwwsLwLmpwMDw
    """.strip()
    assert get_total_group_common_items(all_rugsacks) == 70


def test_part1_solution():
    all_rugsacks = (BASE_DIR / "input.txt").read_text()
    total = get_total_sum_of_priorities(all_rugsacks)
    assert total == 7903


def test_part2_solution():
    all_rugsacks = (BASE_DIR / "input.txt").read_text()
    total = get_total_group_common_items(all_rugsacks)
    assert total == 2548
