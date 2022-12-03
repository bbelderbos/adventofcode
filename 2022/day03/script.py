import string
import typing

ITEM_PRIORITIES = dict(
    zip(string.ascii_lowercase + string.ascii_uppercase, range(1, 53))
)


# part 1


def get_item_value(rugsack: str) -> int:
    half_index = len(rugsack) // 2
    first_compartment = rugsack[:half_index]
    second_compartment = rugsack[half_index:]

    (common_item,) = set(first_compartment) & set(second_compartment)
    return ITEM_PRIORITIES[common_item]


def get_total_sum_of_priorities(all_rugsacks: str) -> int:
    return sum(get_item_value(rugsack.strip()) for rugsack in all_rugsacks.splitlines())


# part 2


def get_common_item(batch_rugsacks: list[str]) -> str:
    common = set(batch_rugsacks[0].strip())
    for rs in batch_rugsacks[1:]:
        common &= set(rs)
    return common.pop()


def _chunker(seq: list[str], size: int) -> typing.Iterator[list[str]]:
    """Source: https://stackoverflow.com/a/434328"""
    # fmt: off
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))
    # fmt: on


def get_total_group_common_items(all_rugsacks: str, size: int = 3) -> int:
    rugsacks = all_rugsacks.splitlines()
    total = 0
    for chunk in _chunker(rugsacks, size):
        item = get_common_item(chunk)
        value = ITEM_PRIORITIES[item]
        total += value
    return total
