def solution_part1(data: str):
    rows = data.splitlines()
    grid = [[int(x) for x in list(row)] for row in rows]
    len_ = len(grid)
    total = 0
    for row in range(len_):
        for col in range(len_):
            outer_index = len_ - 1
            # outer grid
            if row in (0, outer_index) or col in (0, outer_index):
                total += 1
                continue

            # inner grid cell
            cell = grid[row][col]
            left = [grid[row][i] for i in range(len_) if i < col]
            right = [grid[row][i] for i in range(len_) if i > col]
            top = [grid[i][col] for i in range(len_) if i < row]
            bottom = [grid[i][col] for i in range(len_) if i > row]

            vis_left = all(cell > lc for lc in left)
            vis_right = all(cell > rc for rc in right)
            vis_top = all(cell > tc for tc in top)
            vis_bottom = all(cell > bc for bc in bottom)

            if any([vis_left, vis_right, vis_top, vis_bottom]):
                total += 1
    return total


def solution_part2(data: str):
    pass
