from elves import get_max_kcal_elves, get_total_kcal_top_elves


def test_part1():
    assert get_max_kcal_elves() == 72602


def test_part2():
    assert get_total_kcal_top_elves() == 207410
