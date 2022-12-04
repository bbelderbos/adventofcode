from typing import Callable, Iterable


def _create_section_range(pair: str) -> Iterable:
    start, end = pair.split("-")
    return range(int(start), int(end) + 1)


def has_all_overlaps(first: Iterable, second: Iterable) -> bool:
    return all(i in second for i in first)


def has_any_overlap(first: Iterable, second: Iterable) -> bool:
    return any(i in second for i in first)


def calculate_number_of_overlaps(
    pairs: str, overlap: Callable = has_all_overlaps
) -> int:
    total = 0
    for pair in pairs.splitlines():
        first, second = pair.split(",")
        first_section = _create_section_range(first)
        second_section = _create_section_range(second)
        if overlap(first_section, second_section) or overlap(
            second_section, first_section
        ):
            total += 1
    return total
