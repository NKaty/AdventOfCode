def find_manhattan_distance(instructions):
    w_shifts = {
        'N': (-1, 0),
        'S': (1, 0),
        'E': (0, 1),
        'W': (0, -1)
    }
    w_coord = (-1, 10)
    ship_coord = (0, 0)

    def set_w_coord(direction, deg, coord):
        if direction == 'L':
            for _ in range(deg // 90):
                coord = (-coord[1], coord[0])
        else:
            for _ in range(deg // 90):
                coord = (coord[1], -coord[0])
        return coord

    for d, v in instructions:
        if d == 'F':
            ship_coord = ship_coord[0] + w_coord[0] * v, ship_coord[1] + w_coord[1] * v
        if d in w_shifts:
            w_coord = (w_coord[0] + w_shifts[d][0] * v, w_coord[1] + w_shifts[d][1] * v)
        if d in 'LR':
            w_coord = set_w_coord(d, v, w_coord)

    return abs(ship_coord[0]) + abs(ship_coord[1])


if __name__ == "__main__":
    with open('day12/input.txt') as inp:
        navigation_instructions = [(line[0], int(line[1:])) for line in inp]

    print(find_manhattan_distance(navigation_instructions))  # 20873
