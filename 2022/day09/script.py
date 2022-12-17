from typing import Iterable

START_X, START_Y = 4, 0
ADJACENT_CELL_COORDS = [
    (i, j) for i in (-1, 0, 1) for j in (-1, 0, 1) if not (i == j == 0)
]


def head_overlaps_tail(h_pos: list[int], t_pos: list[int]) -> bool:
    return h_pos[0] == t_pos[0] and h_pos[1] == t_pos[1]


def head_touches_tail(h_pos: Iterable[int], t_pos: Iterable[int]) -> bool:
    r, c = h_pos
    for x, y in ADJACENT_CELL_COORDS:
        new = (r + x, c + y)
        if new == tuple(t_pos):
            return True
    return False


def _move_sign(x: int, y: int) -> int:
    if x > y:
        return 1
    elif x < y:
        return -1
    else:
        return 0


def _solution(data: str, length: int) -> int:
    positions = [[START_X, START_Y] for _ in range(length)]
    t_visits = {tuple(positions[-1])}

    for line in data.strip().splitlines():
        print(line)
        move, steps = line.split()

        direction = 1 if move in ("R", "D") else -1
        x_or_y = 0 if move in ("U", "D") else 1

        for _ in range(int(steps)):
            positions[0][x_or_y] += direction

            for i in range(1, len(positions)):
                head, tail = positions[i - 1], positions[i]

                if not head_touches_tail(head, tail) and not head_overlaps_tail(
                    head, tail
                ):
                    positions[i][0] += _move_sign(head[0], tail[0])
                    positions[i][1] += _move_sign(head[1], tail[1])

            t_visits.add(tuple(positions[-1]))

    return len(t_visits)


def solution_part1(data: str) -> int:
    return _solution(data, length=2)


def solution_part2(data: str) -> int:
    return _solution(data, length=10)
