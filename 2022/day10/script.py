def get_x_values(lines):
    x = 1
    results = []
    for i, instruction in enumerate(lines):
        if instruction == "noop":
            results.append((i, x))
        elif instruction.startswith("addx"):
            instruction, amount = instruction.split()
            amount = int(amount)
            results.append((i, x))
            i += 1
            x += amount
            results.append((i, x))
        else:
            raise AssertionError(instruction + "?")
    return results


def solution_part1(data: str) -> int:
    lines = data.strip().splitlines()
    results = get_x_values(lines)
    return sum(
        index * results[index-1][1]
        for index in range(20, 221, 40)
    )


def solution_part2(data: str) -> int:
    lines = data.strip().splitlines()
    rows = []
    output_line = []
    sprite = range(0, 3)
    results = get_x_values(lines)

    for i, (_, x) in enumerate(results, start=1):
        if len(output_line) in sprite:
            output_line.append("#")
        else:
            output_line.append(".")

        sprite = range(x-1, x+2)

        if i % 40 == 0:
            rows.append(output_line)
            output_line = []

    return "\n".join(
        "".join(row) for row in rows
    )
