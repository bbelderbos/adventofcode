def coords(grid, find, func=next):
    """Nice way: https://stackoverflow.com/a/53085140"""
    return func(
        (i, j) for i, sub in enumerate(grid) for j, x in enumerate(sub) if x == find
    )


def _would_go_off_the_grid(r, c, x, y, xmin, ymin):
    return any(
        [
            r == 0 and x == -1,
            c == 0 and y == -1,
            r == xmin - 1 and x == 1,
            c == ymin - 1 and y == 1,
        ]
    )


def _get_possible_moves(grid, pos):
    r, c = pos
    xmin, ymin = len(grid), len(grid[0])
    current = "a" if grid[r][c] == "S" else grid[r][c]
    moves = []
    for x, y in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        if _would_go_off_the_grid(r, c, x, y, xmin, ymin):
            continue
        rr = r + x
        cc = c + y
        destination = "z" if grid[rr][cc] == "E" else grid[rr][cc]
        test = ord(current) >= ord(destination) - 1
        if test:
            moves.append((rr, cc))
    return moves


def shortest_path(grid, start_point, end_point):
    """
    Used this shortest path algo
    https://gist.github.com/akpw/9a30020008294f4a7d6229e076335d34
    """
    queue = []
    visited = set()
    queue.append([start_point])
    while queue:
        path = queue.pop(0)
        current_point = path[-1]

        if current_point == end_point:
            return path[1:]  # exclude start point

        moves = _get_possible_moves(grid, current_point)
        for move in moves:
            if move not in visited:
                visited.add(move)
                new_path = list(path)
                new_path.append(move)
                queue.append(new_path)

    return []


def print_grid(grid, path=None):
    for i, sub in enumerate(grid):
        for j, value in enumerate(sub):
            print("*" if path and (i, j) in path else value, end=" ")
        print()


def solution_part1(data: str) -> int:
    grid = [list(row) for row in data.splitlines()]
    start = coords(grid, "S")
    end = coords(grid, "E")
    path = shortest_path(grid, start, end)
    print_grid(grid, path)
    return len(path)


def solution_part2(data: str) -> int:
    grid = [list(row) for row in data.splitlines()]
    end = coords(grid, "E")
    start_points = [coords(grid, "S")] + list(coords(grid, "a", func=iter))
    paths = []
    for start in start_points:
        path = shortest_path(grid, start, end)
        paths.append(path)
    return min([len(p) for p in paths if len(p)])
