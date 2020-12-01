import copy


def create_empty_grid(height, width):
    return [['.'] * width for _ in range(height)]


def is_grid_empty(grid):
    return sum(sum(1 for item in row if item == '#') for row in grid) == 0


def transform_level(grid, prev_grid, next_grid):
    height = len(grid)
    width = len(grid[0])
    shifts = ((0, 1), (0, -1), (1, 0), (-1, 0))
    new_grid = copy.deepcopy(grid)

    for row in range(height):
        for col in range(width):
            bugs = 0
            if row == height // 2 and col == width // 2:
                continue

            if row == 0 and prev_grid[height // 2 - 1][width // 2] == '#':
                bugs += 1
            if col == 0 and prev_grid[height // 2][width // 2 - 1] == '#':
                bugs += 1
            if row == height - 1 and prev_grid[height // 2 + 1][width // 2] == '#':
                bugs += 1
            if col == width - 1 and prev_grid[height // 2][width // 2 + 1] == '#':
                bugs += 1
            if row == height // 2 - 1 and col == width // 2:
                bugs += sum(1 for i in range(width) if next_grid[0][i] == '#')
            if row == height // 2 and col == width // 2 - 1:
                bugs += sum(1 for i in range(height) if next_grid[i][0] == '#')
            if row == height // 2 + 1 and col == width // 2:
                bugs += sum(1 for i in range(width) if next_grid[height - 1][i] == '#')
            if row == height // 2 and col == width // 2 + 1:
                bugs += sum(1 for i in range(height) if next_grid[i][width - 1] == '#')

            for r_sh, c_sh in shifts:
                if 0 <= row + r_sh < height and 0 <= col + c_sh < width and \
                        not (row + r_sh == height // 2 and col + c_sh == width // 2) \
                        and grid[row + r_sh][col + c_sh] == '#':
                    bugs += 1

            if grid[row][col] == '#' and bugs != 1:
                new_grid[row][col] = '.'
            if grid[row][col] == '.' and bugs in (1, 2):
                new_grid[row][col] = '#'

    return new_grid


def get_grids_of_levels(grid, minutes):
    height = len(grid)
    width = len(grid[0])
    grids = {0: copy.deepcopy(grid), -1: create_empty_grid(height, width), 1: create_empty_grid(height, width)}

    for _ in range(minutes):
        new_grids = {}
        levels = grids.keys()
        min_level = min(levels)
        max_level = max(levels)

        for level in range(max_level + 1):
            if level + 1 not in grids and not is_grid_empty(grids[level]):
                new_grids[level + 1] = create_empty_grid(height, width)
            new_grid = transform_level(grids[level], grids[level - 1],
                                       grids.get(level + 1, create_empty_grid(height, width)))
            new_grids[level] = new_grid

        for level in range(-1, min_level - 1, -1):
            if level - 1 not in grids and not is_grid_empty(grids[level]):
                new_grids[level - 1] = create_empty_grid(height, width)
            new_grid = transform_level(grids[level], grids.get(level - 1, create_empty_grid(height, width)),
                                       grids[level + 1])
            new_grids[level] = new_grid

        grids = copy.deepcopy(new_grids)

    return grids


def count_bugs(grid, minutes):
    grids = get_grids_of_levels(grid, minutes)
    return sum(sum(1 for item in row if item == '#') for grid in grids.values() for row in grid)


if __name__ == "__main__":
    with open('day24/input.txt') as inp:
        eris = [list(line.strip()) for line in inp]

    print(count_bugs(eris, 200))  # 1937
