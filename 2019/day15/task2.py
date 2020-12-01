from intcode import process_instructions


def get_graph(data, map_dict):
    # north, back: south; south, back: north; west, back: east; east, back: west
    moves = (((-1, 0), 2), ((1, 0), 1), ((0, -1), 4), ((0, 1), 3))
    area_map = {(0, 0): map_dict['droid']}
    gen = process_instructions(data, [])
    # initialize generator
    next(gen)

    def traverse(position, back):
        for direction, move_item in enumerate(moves, 1):
            move, new_back = move_item
            new_position = (position[0] + move[0], position[1] + move[1])
            if new_position not in area_map:
                status_code = gen.send(direction)
                area_map[new_position] = status_code
                if status_code != map_dict['wall']:
                    traverse(new_position, new_back)
        gen.send(back)

    for i in range(len(moves)):
        traverse((0, 0), moves[i][1])

    return area_map


def find_oxygen_position(graph, status_code):
    for position in graph.keys():
        if graph[position] == status_code:
            return position


def count_minutes_to_fill_area(data, map_dict):
    graph = get_graph(data, map_dict)
    oxygen_position = find_oxygen_position(graph, map_dict['oxygen_system'])
    moves = ((-1, 0), (1, 0), (0, -1), (0, 1))
    visited = {oxygen_position}
    queue = [oxygen_position]
    dist = {oxygen_position: 0}

    while len(queue):
        position = queue.pop(0)
        for move in moves:
            new_position = (position[0] + move[0], position[1] + move[1])
            if new_position not in visited and graph[new_position] != map_dict['wall']:
                visited.add(new_position)
                dist[new_position] = dist[position] + 1
                queue.append(new_position)

    return max(dist.values())


if __name__ == "__main__":
    with open('day15/input.txt') as inp:
        ns = list(map(int, inp.read().strip().split(',')))

    print(count_minutes_to_fill_area(ns, {'wall': 0, 'empty': 1, 'oxygen_system': 2, 'droid': 3}))  # 334
