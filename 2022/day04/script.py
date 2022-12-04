from typing import Iterable


def _create_section_range(pair: str) -> Iterable:
    start, end = pair.split("-")
    return range(int(start), int(end) + 1)


def _has_overlap(first: Iterable, second: Iterable) -> bool:
    return min(first) >= min(second) and max(first) <= max(second)


def total_number_of_overlapping_ranges(pairs: str) -> int:
    total = 0
    for pair in pairs.splitlines():
        first, second = pair.split(",")
        first_section = _create_section_range(first)
        second_section = _create_section_range(second)
        if _has_overlap(first_section, second_section) or _has_overlap(
            second_section, first_section
        ):
            total += 1
    return total
