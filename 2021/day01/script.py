def solution_part1(data: str):
    depths = [int(x) for x in data.strip().splitlines()]
    total = 0
    for i, j in zip(depths, depths[1:]):
        if j > i:
            total += 1
    return total


def solution_part2(data: str):
    depths = [int(x) for x in data.strip().splitlines()]
    total = 0
    size = 3
    for i, _ in enumerate(depths):
        old = sum(depths[i : i + size])
        new = sum(depths[i + 1 : i + size + 1])
        if new > old:
            total += 1
        if i + size == len(depths) - 1:
            break
    return total
