import string
import typing

ITEM_PRIORITIES = dict(
    zip(string.ascii_lowercase + string.ascii_uppercase, range(1, 53))
)


class Item(typing.NamedTuple):
    letter: str
    value: int


def get_item(rugsack: str) -> Item:
    half_index = len(rugsack) // 2
    first_compartment = rugsack[:half_index]
    second_compartment = rugsack[half_index:]

    (common_item,) = set(first_compartment) & set(second_compartment)
    item_value = ITEM_PRIORITIES.get(common_item)

    return Item(common_item, item_value)


def get_total_sum_of_priorities(all_rugsacks):
    return sum(get_item(rugsack.strip()).value for rugsack in all_rugsacks.splitlines())
