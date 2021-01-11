from collections import Counter, defaultdict
from itertools import product
from copy import deepcopy


def find_resource_value(grid, minutes):
    shifts = list(product(range(-1, 2), repeat=2))
    shifts.remove((0, 0))
    h = len(grid)
    w = len(grid[0])

    for _ in range(minutes):
        neighbours = Counter(
            ((i, j), grid[i + s[0]][j + s[1]]) for i in range(h) for j in range(w) for s in shifts
            if 0 <= i + s[0] < h and 0 <= j + s[1] < w)

        nbs = defaultdict(dict)
        for k, v in neighbours.items():
            nbs[k[0]][k[1]] = v

        prev = deepcopy(grid)
        for c, n in nbs.items():
            if prev[c[0]][c[1]] == '.' and n.get('|', 0) > 2:
                grid[c[0]][c[1]] = '|'
            elif prev[c[0]][c[1]] == '|' and n.get('#', 0) > 2:
                grid[c[0]][c[1]] = '#'
            elif prev[c[0]][c[1]] == '#' and (n.get('#', 0) == 0 or n.get('|', 0) == 0):
                grid[c[0]][c[1]] = '.'

    count = Counter(grid[i][j] for i in range(h) for j in range(w))
    return count['|'] * count['#']


if __name__ == "__main__":
    with open('day18/input.txt') as inp:
        area = [list(line.strip()) for line in inp]

    print(find_resource_value(area, 10))  # 604884
