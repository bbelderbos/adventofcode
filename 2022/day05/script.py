import re

Stacks = list[list[str]]


def populate_stacks(stack_data: str) -> Stacks:
    number_of_stacks = int(stack_data.strip()[-1])

    # cannot do [[]] * num_stacks (= by reference / lists with same id!)
    stacks: Stacks = []
    for _ in range(number_of_stacks):
        stacks.append([])

    for line in stack_data.splitlines()[:-1]:
        crates = re.findall(r"(?:\s{3}|(\[[A-Z]\]))\s?", line)
        # argh the spaces after [V] get truncated
        if len(crates) < number_of_stacks:
            crates.append("")  # 8 -> 9

        for i, crate in enumerate(crates):
            if crate:
                stacks[i].append(crate)

    return stacks


def move_crates(stacks: Stacks, instructions: str) -> Stacks:
    for instruction in instructions.strip().splitlines():
        amount, from_, to_ = re.findall(r"\d+", instruction)
        for _ in range(int(amount)):
            from_index = int(from_) - 1
            to_index = int(to_) - 1
            from_crate = stacks[from_index].pop(0)
            stacks[to_index].insert(0, from_crate)  # TODO: use deque
    return stacks


def get_top_level_crates(input_text: str) -> str:
    stack_data, instructions = input_text.split("\n\n")
    stacks = populate_stacks(stack_data)
    updated_stacks = move_crates(stacks, instructions)
    return "".join(stack[0].strip("[]") for stack in updated_stacks)
