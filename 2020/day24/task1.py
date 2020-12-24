import re


def count_black_tiles(tiles):
    shifts = {'e': (0, 2), 'w': (0, -2), 'se': (1, 1), 'sw': (1, -1), 'ne': (-1, 1), 'nw': (-1, -1)}
    seen = {}
    for tile in tiles:
        tile_coord = (0, 0)
        for direction in tile:
            tile_coord = tile_coord[0] + shifts[direction][0], tile_coord[1] + shifts[direction][1]
        seen[tile_coord] = not seen.get(tile_coord, False)
    return sum(seen.values())


if __name__ == "__main__":
    reg = re.compile(r'w|e|se|sw|ne|nw')
    with open('day24/input.txt') as inp:
        tiles_list = [re.findall(reg, tile.strip()) for tile in inp]

    print(count_black_tiles(tiles_list))  # 266
