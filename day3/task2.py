import math
from shapely.geometry import LineString


def find_min_steps(wires):
    results = []
    wire_vectors1, wire_vectors2 = [get_vectors(wire) for wire in wires]
    for vec1 in wire_vectors1:
        for vec2 in wire_vectors2:
            steps = find_steps_to_intersection(vec1, vec2)
            if steps is not None:
                results.append(steps)
    results = filter(lambda x: x != 0, results)
    return min(results)


def find_steps_to_intersection(vec1, vec2):
    line1 = LineString(vec1[0])
    line2 = LineString(vec2[0])
    cross = line1.intersection(line2)
    if cross.is_empty:
        steps = None
    else:
        new_steps1 = math.fabs(vec1[0][0][0] - cross.x) + math.fabs(vec1[0][0][1] - cross.y)
        new_steps2 = math.fabs(vec2[0][0][0] - cross.x) + math.fabs(vec2[0][0][1] - cross.y)
        steps = int(sum((vec1[1], vec2[1], new_steps1, new_steps2)))
    return steps


def get_vectors(wire):
    wire_vectors = []
    x = y = 0
    steps = 0
    for item in wire:
        direction = item[0]
        new_x = x
        new_y = y
        step = int(item[1:])
        if direction == 'L':
            new_x = x - step
        elif direction == 'R':
            new_x = x + step
        elif direction == 'U':
            new_y = y + step
        elif direction == 'D':
            new_y = y - step
        else:
            raise Exception('Wrong direction')
        wire_vectors.append([[(x, y), (new_x, new_y)], steps])
        steps += math.fabs(step)
        x = new_x
        y = new_y
    return wire_vectors


if __name__ == "__main__":
    with open('day3/input.txt') as inp:
        ws = [line.strip().split(',') for line in inp]

    print(find_min_steps(ws))  # 56410
