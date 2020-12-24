import re
from collections import Counter


def get_floor(tiles, shifts):
    blacks = set()
    for tile in tiles:
        tile_coord = (0, 0)
        for direction in tile:
            tile_coord = tile_coord[0] + shifts[direction][0], tile_coord[1] + shifts[direction][1]
        if tile_coord in blacks:
            blacks.remove(tile_coord)
        else:
            blacks.add(tile_coord)
    return blacks


def count_black_tiles(tiles, days):
    shifts = {'e': (0, 2), 'w': (0, -2), 'se': (1, 1), 'sw': (1, -1), 'ne': (-1, 1), 'nw': (-1, -1)}
    blacks = get_floor(tiles, shifts)

    for _ in range(days):
        neighbours = Counter(
            (coord[0] + shift[0], coord[1] + shift[1]) for coord in blacks for shift in
            shifts.values())
        blacks = set(
            nb[0] for nb in neighbours.items() if nb[1] == 2 or (nb[0] in blacks and nb[1] == 1))

    return len(blacks)


if __name__ == "__main__":
    reg = re.compile(r'w|e|se|sw|ne|nw')
    with open('day24/input.txt') as inp:
        tiles_list = [re.findall(reg, tile.strip()) for tile in inp]

    print(count_black_tiles(tiles_list, 100))  # 3627
