def find_manhattan_distance(instructions):
    direction = 'E'
    dir_chain = 'NWSE'
    shifts = {
        'N': (-1, 0),
        'S': (1, 0),
        'E': (0, 1),
        'W': (0, -1)
    }
    directions = {
        'L': lambda x: dir_chain[int((dir_chain.index(direction) + x / 90) % 4)],
        'R': lambda x: dir_chain[int((dir_chain.index(direction) - x / 90) % 4)]
    }
    coord = (0, 0)

    for d, v in instructions:
        if d == 'F':
            d = direction
        if d in shifts:
            coord = coord[0] + shifts[d][0] * v, coord[1] + shifts[d][1] * v
        if d in directions:
            direction = directions[d](v)

    return abs(coord[0]) + abs(coord[1])


if __name__ == "__main__":
    with open('day12/input.txt') as inp:
        navigation_instructions = [(line[0], int(line[1:])) for line in inp]

    print(find_manhattan_distance(navigation_instructions))  # 1687
