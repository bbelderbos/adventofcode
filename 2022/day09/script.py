ADJACENT_CELL_COORDS = [
    (i, j) for i in (-1, 0, 1) for j in (-1, 0, 1) if not (i == j == 0)
]


def overlap(h_pos, t_pos):
    return tuple(h_pos) == tuple(t_pos)


def h_touches_t(h_pos, t_pos):
    """
    if h_pos == t_pos:
        print("overlap")
        return True
    """
    # [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    r, c = h_pos
    for x, y in ADJACENT_CELL_COORDS:
        new = (r + x, c + y)
        # print("coords", new, t_pos)
        if new == t_pos:
            return True
    return False


def solution_part1(data: str) -> int:
    h_pos = [4, 0]
    t_pos = [4, 0]
    num_t_visits = {tuple(t_pos)}
    for line in data.strip().splitlines():
        move, steps = line.split()
        steps = int(steps)
        if move in ("R", "D"):
            multiplier = 1
        else:
            multiplier = -1
        if move in ("U", "D"):
            coord = 0
        else:
            coord = 1
        move = steps * multiplier
        print("\nnew round")
        print("move & steps", move, steps)
        print()

        # prev_h_pos = tuple(h_pos)
        for _ in range(steps):
            prev_h_pos = tuple(h_pos)
            h_pos[coord] += multiplier
            print(h_pos, t_pos)
            touches = h_touches_t(h_pos, t_pos)
            print(f"{touches=}")
            if not touches and not overlap(h_pos, t_pos):
                t_pos = prev_h_pos
                num_t_visits.add(tuple(t_pos))
            """
            else:
                x = t_pos[0] + multiplier
                y = t_pos[1] + multiplier
                t_pos = [x, y]
            """
            print(h_pos, t_pos)
            print()

    breakpoint()
    return len(num_t_visits)


def solution_part2(data: str) -> int:
    pass
