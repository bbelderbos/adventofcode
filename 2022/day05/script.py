import re
from pprint import pprint as pp

input_text = "    [D]    \n" "[N] [C]    \n" "[Z] [M] [P]\n" " 1   2   3 \n"
input_text += """
move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""

Stacks = list[list[str]]


def populate_stacks(stack_data: str = input_text) -> Stacks:
    number_of_stacks = int(stack_data.strip()[-1])

    # cannot do [[]] * number_of_stacks (lists with same id!)
    stacks = []
    for _ in range(number_of_stacks):
        stacks.append([])

    for line in stack_data.splitlines()[:-1]:
        crates = re.findall(r"([ ]{3}|\[[A-Z]\])", line)
        for i, crate in enumerate(crates):
            stacks[i].append(crate)
    return stacks


stack_data, instructions = input_text.split("\n\n")
stacks = populate_stacks(stack_data)
from pprint import pprint as pp

pp(stacks)


def move_crates(stacks: Stacks, instructions: str = instructions):
    for instruction in instructions.strip().splitlines():
        # move 1 from 2 to 1
        amount, from_, to_ = re.findall(r"\d", instruction)
        print(amount, from_, to_)
        for _ in range(int(amount)):
            from_index = int(from_) - 1
            to_index = int(to_) - 1
            from_crate = stacks[from_index].pop(0)  # TODO: use deque
            print(from_crate, to_index, "from index", from_index)
            print("result")
            # breakpoint()
            if stacks[to_index] and not stacks[to_index][0].strip():
                stacks[to_index][0] = from_crate
                stacks[from_index].insert(0, "   ")
            else:
                stacks[to_index].insert(0, from_crate)  # TODO: use deque
            print(stacks)
            print()


move_crates(stacks, instructions)
from pprint import pprint as pp

pp(stacks)
