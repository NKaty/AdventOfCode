import re
import math


def manhattan_distance(a, b):
    return sum(abs(ac - bc) for ac, bc in zip(a, b))


def find_coord(bots):
    xs = [item[0][0] for item in bots]
    ys = [item[0][1] for item in bots]
    zs = [item[0][2] for item in bots]
    mins = min(xs), min(ys), min(zs)
    maxs = max(xs), max(ys), max(zs)

    start = 1
    while start < max(maxs) - min(mins):
        start *= 2

    result = 0, 0
    for i in range(4):
        min_x, min_y, min_z = mins
        max_x, max_y, max_z = maxs
        dist = start

        while True:
            best_count = 0
            best_bot = None
            best_md = math.inf
            for x in range(min_x, max_x + 1, dist):
                for y in range(min_y, max_y + 1, dist):
                    for z in range(min_z, max_z + 1, dist):
                        count = 0
                        for c, r in bots:
                            md = manhattan_distance((x, y, z), c)
                            if dist == 1:
                                if md <= r:
                                    count += 1
                            else:
                                if md // dist - i <= r // dist:
                                    count += 1

                        if count > best_count:
                            best_count = count
                            best_bot = x, y, z
                            best_md = manhattan_distance(best_bot, (0, 0, 0))
                        if count == best_count:
                            new_md = manhattan_distance((x, y, z), (0, 0, 0))
                            if new_md < best_md:
                                best_md = new_md
                                best_bot = x, y, z
            if dist == 1:
                if result[0] < best_count or (result[0] == best_count and result[1] > best_md):
                    result = best_count, best_md
                break
            min_x, min_y, min_z = best_bot[0] - dist, best_bot[1] - dist, best_bot[2] - dist
            max_x, max_y, max_z = best_bot[0] + dist, best_bot[1] + dist, best_bot[2] + dist
            dist //= 2

    return result[1]


if __name__ == "__main__":
    reg = re.compile(r'-?\d+')
    with open('day23/input.txt') as inp:
        data = [list(map(int, re.findall(reg, line.strip()))) for line in inp]
    data = [(item[:3], item[3]) for item in data]

    print(find_coord(data))  # 100985898
