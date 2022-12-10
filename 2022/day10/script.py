from typing import Iterable


def get_x_values(lines: list[str]) -> list[tuple[int, int]]:
    x = 1
    results = []
    for i, instruction in enumerate(lines):
        if instruction == "noop":
            results.append((i, x))
        elif instruction.startswith("addx"):
            instruction, amount = instruction.split()
            results.append((i, x))
            i += 1
            x += int(amount)
            results.append((i, x))
        else:
            raise AssertionError(instruction + "?")
    return results


def solution_part1(data: str) -> int:
    lines = data.strip().splitlines()
    results = get_x_values(lines)
    cycles = range(20, 221, 40)
    return sum(i * results[i - 1][1] for i in cycles)


def _set_sprite(x: int) -> Iterable:
    return range(x - 1, x + 2)


def solution_part2(data: str) -> str:
    lines = data.strip().splitlines()
    row: list[str] = []
    rows = []
    x, nl = 1, 40
    sprite = _set_sprite(x)
    results = get_x_values(lines)

    for i, (_, x) in enumerate(results, start=1):
        row.append("#" if len(row) in sprite else ".")
        sprite = _set_sprite(x)
        if i % nl == 0:
            rows.append(row)
            row = []

    return "\n".join("".join(row) for row in rows)
