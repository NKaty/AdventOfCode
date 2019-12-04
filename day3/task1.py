import math
from shapely.geometry import LineString


def find_min_distance(wires):
    results = []
    wire_vectors1, wire_vectors2 = [get_vectors(wire) for wire in wires]
    for vec1 in wire_vectors1:
        for vec2 in wire_vectors2:
            cross_point = find_intersection(vec1, vec2)
            if cross_point is not None:
                results.append(int(sum(map(lambda x: math.fabs(x), cross_point))))
    results = filter(lambda x: x != 0, results)
    return min(results)


def find_intersection(vec1, vec2):
    line1 = LineString(vec1)
    line2 = LineString(vec2)
    cross = line1.intersection(line2)
    cross = None if cross.is_empty else (cross.x, cross.y)
    return cross


def get_vectors(wire):
    wire_vectors = []
    x = y = 0
    for item in wire:
        direction = item[0]
        new_x = x
        new_y = y
        if direction == 'L':
            new_x = x - int(item[1:])
        elif direction == 'R':
            new_x = x + int(item[1:])
        elif direction == 'U':
            new_y = y + int(item[1:])
        elif direction == 'D':
            new_y = y - int(item[1:])
        else:
            raise Exception('Wrong direction')
        wire_vectors.append([(x, y), (new_x, new_y)])
        x = new_x
        y = new_y
    return wire_vectors


ws = []
with open('day3/input.txt') as inp:
    for line in inp:
        ws.append(line.strip().split(','))

print(find_min_distance(ws))  # 557
