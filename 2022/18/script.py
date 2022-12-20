from typing import NamedTuple


class Point(NamedTuple):
    x: int
    y: int
    z: int


def adjacent_cubes(pt: Point) -> list[Point]:
    x, y, z = pt
    return [
        Point(x + 1, y, z),
        Point(x - 1, y, z),
        Point(x, y + 1, z),
        Point(x, y - 1, z),
        Point(x, y, z + 1),
        Point(x, y, z - 1),
    ]


def parse_cubes(data: str) -> set[Point]:
    cubes = set()
    for line in data.splitlines():
        cubes.add(Point(*[int(x) for x in line.split(",")]))
    return cubes


def solution_part1(data: str) -> int:
    cubes = parse_cubes(data)
    covered = []
    for cube in cubes:
        for adj in adjacent_cubes(cube):
            if adj in cubes:
                covered.append(cube)
    return len(cubes) * 6 - len(covered)


def solution_part2(data: str) -> int:
    pass
