from itertools import product
from collections import defaultdict
from copy import deepcopy


def find_active_cubes(grid):
    lens = [(-1, 2), (-1, 2), (0, len(grid)), (0, len(grid[0]))]
    dim4 = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: '.'))))
    dim4[0][0] = grid
    shifts = list(product(range(-1, 2), repeat=4))
    shifts.remove((0, 0, 0, 0))

    for _ in range(6):
        previous = deepcopy(dim4)
        lens = [(item[0] - 1, item[1] + 1) for item in lens]
        for w in range(*lens[0]):
            for z in range(*lens[1]):
                for y in range(*lens[2]):
                    for x in range(*lens[3]):
                        actives = sum(1 if previous[w + shift[0]][z + shift[1]][y + shift[2]][
                                               x + shift[3]] == '#' else 0 for shift in shifts)
                        if previous[w][z][y][x] == '#' and actives not in (2, 3):
                            dim4[w][z][y][x] = '.'
                        if previous[w][z][y][x] == '.' and actives == 3:
                            dim4[w][z][y][x] = '#'

    return sum(1 if dim4[w][z][y][x] == '#' else 0 for x in range(*lens[3]) for y in range(*lens[2])
               for z in range(*lens[1]) for w in range(*lens[0]))


if __name__ == "__main__":
    with open('day17/input.txt') as inp:
        cubes = defaultdict(lambda: defaultdict(lambda: '.'), (
            (i, defaultdict(lambda: '.', ((j, item) for j, item in enumerate(list(line.strip())))))
            for i, line in enumerate(inp)))

    print(find_active_cubes(cubes))  # 2532
