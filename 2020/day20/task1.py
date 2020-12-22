from math import prod


def get_possible_borders(grid):
    left = [row[0] for row in grid]
    right = [row[-1] for row in grid]
    return [grid[0], ''.join(grid[0][::-1]), grid[-1], ''.join(grid[-1][::-1]),
            ''.join(left), ''.join(left[::-1]), ''.join(right), ''.join(right[::-1])]


def assemble_image(grids):
    borders = [(i, get_possible_borders(grid)) for i, grid in grids.items()]
    count = {k: 0 for k in grids.keys()}

    for i, (k1, grid1) in enumerate(borders):
        for border1 in grid1:
            for k2, grid2 in borders[i + 1:]:
                for border2 in grid2:
                    if border1 == border2:
                        count[k1] += 1
                        count[k2] += 1

    return prod(sorted(count, key=count.get)[:4])


if __name__ == "__main__":
    with open('day20/input.txt') as inp:
        tiles = [tile.split('\n') for tile in inp.read().strip().split('\n\n')]

    tiles = {int(tile[0][-5:-1]): [row.strip() for row in tile[1:]] for tile in tiles}

    print(assemble_image(tiles))  # 54755174472007
