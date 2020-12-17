from itertools import product
from collections import defaultdict
from copy import deepcopy


def find_active_cubes(grid):
    lens = [(-1, 2), (0, len(grid)), (0, len(grid[0]))]
    dim3 = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: '.')), ((0, grid),))
    shifts = list(product(range(-1, 2), repeat=3))
    shifts.remove((0, 0, 0))

    for _ in range(6):
        previous = deepcopy(dim3)
        lens = [(item[0] - 1, item[1] + 1) for item in lens]
        for z in range(*lens[0]):
            for y in range(*lens[1]):
                for x in range(*lens[2]):
                    actives = sum(1 if previous[z + shift[0]][y + shift[1]][x + shift[2]] == '#'
                                  else 0 for shift in shifts)
                    if previous[z][y][x] == '#' and actives not in (2, 3):
                        dim3[z][y][x] = '.'
                    if previous[z][y][x] == '.' and actives == 3:
                        dim3[z][y][x] = '#'

    return sum(1 if dim3[z][y][x] == '#' else 0 for x in range(*lens[2]) for y in range(*lens[1])
               for z in range(*lens[0]))


if __name__ == "__main__":
    with open('day17/input.txt') as inp:
        cubes = defaultdict(lambda: defaultdict(lambda: '.'), (
            (i, defaultdict(lambda: '.', ((j, item) for j, item in enumerate(list(line.strip())))))
            for i, line in enumerate(inp)))

    print(find_active_cubes(cubes))  # 257
