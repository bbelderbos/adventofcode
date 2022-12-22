import re


def print_grid(grid):
    print()
    for row in grid:
        print(" ".join(row))


def solution_part1(data: str) -> int:
    grid_lines, instructions = data.split("\n\n")
    lines = grid_lines.splitlines()

    max_line = max([len(line) for line in lines])
    grid = [list(line) + list([" "] * (max_line - len(line))) for line in lines]

    instructions = re.findall(r"(\d+|[RL])", instructions)
    facing_shifts = {
        ("R", "^"): ">",
        ("R", ">"): "v",
        ("R", "v"): "<",
        ("R", "<"): "^",
        ("L", "^"): "<",
        ("L", "<"): "v",
        ("L", "v"): ">",
        ("L", ">"): "^",
    }
    facing_values = {">": 0, "v": 1, "<": 2, "^": 3}

    start_y = grid[0].index(".")
    start_x = 0
    pos = (start_x, start_y)
    facing = ">"
    multiplier = 1

    for step in instructions:
        x, y = pos

        if step in ("R", "L"):
            old_dir = facing
            facing = facing_shifts[(step, old_dir)]
            multiplier = 1 if facing in (">", "v") else -1

        elif step.isdigit():
            num_steps = int(step)

            # move horizontally
            if facing in (">", "<"):
                for _ in range(num_steps):
                    grid[x][y] = facing
                    old_y = y
                    y += 1 * multiplier
                    # reached end, go to start
                    if y >= len(grid[0]) or grid[x][y] == " ":
                        row = grid[x]
                        indexes = [i for i, x in enumerate(row) if x != " "]
                        if not indexes:
                            y = old_y
                            pos = (x, y)
                            break
                        y = indexes[0] if multiplier > 0 else indexes[-1]
                    if grid[x][y] == "#":
                        y = old_y
                        pos = (x, y)
                        break
                    pos = (x, y)

            # move vertically
            elif facing in ("v", "^"):
                for _ in range(num_steps):
                    grid[x][y] = facing
                    old_x = x
                    x += 1 * multiplier
                    if x >= len(grid) or grid[x][y] == " ":
                        col = [grid[i][y] for i in range(len(grid))]
                        indexes = [i for i, x in enumerate(col) if x != " "]
                        if not indexes:
                            x = old_x
                            pos = (x, y)
                            break
                        x = indexes[0] if multiplier > 0 else indexes[-1]
                    if grid[x][y] == "#":
                        x = old_x
                        pos = (x, y)
                        break
                    pos = (x, y)

            else:
                raise AssertionError("invalid facing")

        else:
            raise AssertionError("invalid instruction")

    final_x, final_y = pos
    return 1000 * (final_x + 1) + 4 * (final_y + 1) + facing_values[facing]


def solution_part2(data: str) -> int:
    pass
