from __future__ import annotations


def solution_part1(data: str) -> int:
    c = [0, 0]
    actions = dict(zip("forward down up".split(), ((0, 1), (1, 1), (1, -1))))
    for line in data.strip().splitlines():
        move, num = line.split()
        pos, multiplier = actions[move]
        c[pos] += int(num) * multiplier
    return c[0] * c[1]


def solution_part2(data: str) -> int:
    c = [0, 0, 0]  # hor dep aim
    for line in data.strip().splitlines():
        d, Xi = line.split()
        X = int(Xi)
        if d == "forward":
            c[0] += X
            c[1] += c[2] * X
        elif d == "down":
            c[2] += X
        elif d == "up":
            c[2] -= X
        else:
            raise AssertionError("unknown cmd", d)

    return c[0] * c[1]
