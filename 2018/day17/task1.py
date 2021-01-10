import re
import sys


def get_clay_set(veins):
    clay = set()
    for c, vein in veins:
        for i in range(vein[1], vein[2] + 1):
            if c == 'x':
                clay.add((vein[0], i))
            else:
                clay.add((i, vein[0]))
    return clay


def count_water_tiles(veins):
    clay = get_clay_set(veins)
    still = set()
    water = set()
    min_y = min(clay, key=lambda item: item[1])[1]
    max_y = max(clay, key=lambda item: item[1])[1]

    def is_sand(x, y):
        return not ((x, y) in clay or (x, y) in water)

    def is_surface(x, y):
        return (x, y) in clay or (x, y) in still

    def make_still_part(x, y, shift):
        cur_x = x
        while (cur_x, y) not in clay:
            still.add((cur_x, y))
            cur_x += shift

    def has_wall(x, y, shift):
        cur_x = x
        while True:
            if (cur_x, y) in clay:
                return True
            if is_sand(cur_x, y):
                return False
            cur_x += shift

    def has_walls(x, y):
        return has_wall(x, y, 1) and has_wall(x, y, -1)

    def make_still(x, y):
        if (x, y) not in still and has_walls(x, y):
            make_still_part(x, y, 1)
            make_still_part(x, y, -1)

    def fill(x, y):
        if y >= max_y:
            return

        if is_sand(x, y + 1):
            water.add((x, y + 1))
            fill(x, y + 1)

        if is_surface(x, y + 1):
            if is_sand(x + 1, y):
                water.add((x + 1, y))
                fill(x + 1, y)
            if is_sand(x - 1, y):
                water.add((x - 1, y))
                fill(x - 1, y)

        make_still(x, y)

    fill(500, 0)
    return sum(1 for x, y in water if y >= min_y)


if __name__ == "__main__":
    reg = re.compile(r'\d+')
    with open('day17/input.txt') as inp:
        veins_of_clay = [(line[0], tuple(map(int, re.findall(reg, line)))) for line in inp]

    sys.setrecursionlimit(3000)
    print(count_water_tiles(veins_of_clay))  # 30737
