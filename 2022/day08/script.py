def _create_grid(data: str) -> list[list[int]]:
    rows = data.splitlines()
    grid = [[int(x) for x in list(row)] for row in rows]
    return grid


def solution_part1(data: str) -> int:
    grid = _create_grid(data)
    grid_len = len(grid)
    total = 0

    for row in range(grid_len):
        for col in range(grid_len):
            outer_index = grid_len - 1
            # outer grid
            if row in (0, outer_index) or col in (0, outer_index):
                total += 1
                continue

            # inner grid cell
            cell = grid[row][col]

            left = [grid[row][i] for i in range(grid_len) if i < col]
            right = [grid[row][i] for i in range(grid_len) if i > col]
            top = [grid[i][col] for i in range(grid_len) if i < row]
            bottom = [grid[i][col] for i in range(grid_len) if i > row]

            vis_left = all(cell > lc for lc in left)
            vis_right = all(cell > rc for rc in right)
            vis_top = all(cell > tc for tc in top)
            vis_bottom = all(cell > bc for bc in bottom)

            if any([vis_left, vis_right, vis_top, vis_bottom]):
                total += 1
    return total


def _num_trees_visible(cell, axis, go_in_reversed_order=False):
    if go_in_reversed_order:
        axis = reversed(axis)

    total = 0

    for c in axis:
        total += 1
        if c >= cell:
            return total

    return total


def solution_part2(data: str) -> int:
    grid = _create_grid(data)
    grid_len = len(grid)
    max_ = 0

    for row in range(grid_len):
        for col in range(grid_len):
            cell = grid[row][col]

            left = [grid[row][i] for i in range(grid_len) if i < col]
            right = [grid[row][i] for i in range(grid_len) if i > col]
            top = [grid[i][col] for i in range(grid_len) if i < row]
            bottom = [grid[i][col] for i in range(grid_len) if i > row]

            vis_top = _num_trees_visible(cell, top, go_in_reversed_order=True)
            vis_left = _num_trees_visible(cell, left, go_in_reversed_order=True)
            vis_bottom = _num_trees_visible(cell, bottom)
            vis_right = _num_trees_visible(cell, right)

            total = vis_top * vis_left * vis_bottom * vis_right

            if total > max_:
                max_ = total

    return max_
