from intcode import process_instructions


def get_scaffold_grid(data):
    gen = process_instructions(data, [])
    return [output for output in gen]


def count_alignment_params_sum(data, tiles):
    grid = get_scaffold_grid(data)
    alignment_params_sum = 0
    shifts = ((0, 1), (0, -1), (1, 0), (-1, 0))
    for row in range(1, len(grid) - 2):
        for col in range(1, len(grid[0]) - 1):
            if grid[row][col] == 35 and all([grid[row + shift[0]][col + shift[1]] == 35 for shift in shifts]):
                alignment_params_sum += row * col
    return alignment_params_sum


if __name__ == "__main__":
    with open('day17/input.txt') as inp:
        ns = list(map(int, inp.read().strip().split(',')))

    # print(get_scaffold_grid(ns, {35: '#', 46: '.', 10: '\n'}))
    print(count_alignment_params_sum(ns, {}))