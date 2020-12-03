from math import prod


def count_trees(grid, shift):
    width = len(grid[0])
    coord = [0, 0]
    count = 0
    while coord[1] < len(grid) - 1:
        if grid[coord[1]][coord[0]] == '#':
            count += 1
        coord = [(coord[0] + shift[0]) % width, coord[1] + shift[1]]
    return count


def check_slopes(grid):
    slopes = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
    return prod([count_trees(grid, item) for item in slopes])


if __name__ == "__main__":
    with open('day03/input.txt') as inp:
        trees_map = tuple(tuple(line.strip()) for line in inp)

    print(check_slopes(trees_map))  # 1260601650
