from intcode import process_instructions


def get_scaffold_grid(data):
    gen = process_instructions(data, [])
    grid = []
    grid_row = []

    while True:
        while (output := next(gen)) != 10:
            grid_row.append(output)
        if not len(grid_row) and output == 10:
            break
        grid.append(grid_row)
        grid_row = []

    return grid


def count_alignment_params_sum(data, tiles):
    grid = get_scaffold_grid(data)
    alignment_params_sum = 0
    shifts = ((0, 1), (0, -1), (1, 0), (-1, 0))
    for row in range(1, len(grid) - 2):
        for col in range(1, len(grid[0]) - 1):
            if grid[row][col] == tiles['scaffold'] and all(
                    [grid[row + shift[0]][col + shift[1]] == tiles['scaffold'] for shift in shifts]):
                alignment_params_sum += row * col
    return alignment_params_sum


if __name__ == "__main__":
    with open('day17/input.txt') as inp:
        ns = list(map(int, inp.read().strip().split(',')))

    print(count_alignment_params_sum(ns, {'scaffold': 35, 'open_space': 46}))  # 4112
