START_X, START_Y = 4, 0
ADJACENT_CELL_COORDS = [
    (i, j) for i in (-1, 0, 1) for j in (-1, 0, 1) if not (i == j == 0)
]


def overlaps(h_pos: list[int], t_pos: list[int]) -> bool:
    return h_pos == t_pos


def h_touches_t(h_pos: list[int], t_pos: list[int]) -> bool:
    r, c = h_pos
    for x, y in ADJACENT_CELL_COORDS:
        new = [r + x, c + y]
        if new == t_pos:
            return True
    return False


def solution_part1(data: str) -> int:
    h_pos = [START_X, START_Y]
    t_pos = [START_X, START_Y]
    t_visits = {tuple(t_pos)}

    for line in data.strip().splitlines():
        move, steps = line.split()

        direction = 1 if move in ("R", "D") else -1
        coord = 0 if move in ("U", "D") else 1

        for _ in range(int(steps)):
            prev_h_pos = list(h_pos)
            h_pos[coord] += direction

            if not h_touches_t(h_pos, t_pos) and not overlaps(h_pos, t_pos):
                t_pos = prev_h_pos
                t_visits.add(tuple(t_pos))

    return len(t_visits)


def solution_part2(data: str) -> int:
    pass
