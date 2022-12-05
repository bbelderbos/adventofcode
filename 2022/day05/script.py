import re
from collections import deque

Stacks = list[deque[str]]


def populate_stacks(stack_data: str) -> Stacks:
    number_of_stacks = int(stack_data.strip()[-1])

    # cannot do [[]] * num_stacks (= by reference / lists with same id!)
    stacks: Stacks = []
    for _ in range(number_of_stacks):
        stacks.append(deque())

    for line in stack_data.splitlines()[:-1]:
        crates = re.findall(r"(?:\s{3}|(\[[A-Z]\]))\s?", line)

        # argh the spaces after [V] on the first line of the input file
        # is getting truncated so need to make this ugly hack
        if len(crates) < number_of_stacks:
            for _ in range(number_of_stacks - len(crates)):
                crates.append("")  # 8 -> 9

        for i, crate in enumerate(crates):
            if crate:
                stacks[i].append(crate)

    return stacks


def move_crates(
    stacks: Stacks, instructions: str, *, retain_order: bool = False
) -> Stacks:
    for instruction in instructions.strip().splitlines():
        amount, from_, to_ = re.findall(r"\d+", instruction)
        amount = int(amount)
        from_index = int(from_) - 1
        to_index = int(to_) - 1

        from_crates = [stacks[from_index].popleft() for _ in range(amount)]

        if retain_order:
            from_crates.reverse()

        for from_crate in from_crates:
            stacks[to_index].insert(0, from_crate)  # TODO: use deque

    return stacks


def get_top_level_crates(input_text: str, retain_order: bool = False) -> str:
    stack_data, instructions = input_text.split("\n\n")

    stacks = populate_stacks(stack_data)

    updated_stacks = move_crates(stacks, instructions, retain_order=retain_order)

    return "".join(stack[0].strip("[]") for stack in updated_stacks)
