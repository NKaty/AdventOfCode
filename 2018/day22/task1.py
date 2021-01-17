def find_risk_level(depth, target):
    depth = int(depth)
    target = tuple(map(int, target.split(',')))
    grid = {}

    for y in range(target[1] + 1):
        for x in range(target[0] + 1):
            if (x, y) in ((0, 0), target):
                geo_index = 0
            elif y == 0:
                geo_index = x * 16807
            elif x == 0:
                geo_index = y * 48271
            else:
                geo_index = grid[(x - 1, y)][0] * grid[(x, y - 1)][0]
            erosion_level = (geo_index + depth) % 20183
            grid[(x, y)] = erosion_level, erosion_level % 3

    return sum(item[1] for item in grid.values())


if __name__ == "__main__":
    with open('day22/input.txt') as inp:
        data = [line.strip().split(': ')[1] for line in inp]

    print(find_risk_level(data[0], data[1]))  # 7402
