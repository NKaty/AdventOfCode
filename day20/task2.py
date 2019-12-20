def parse_maze(maze, height, width):
    portals = {}
    for r in range(1, height):
        for c in range(1, width):
            if maze[r][c].isalpha():
                if maze[r - 1][c].isalpha() and 1 < c < width - 2:
                    tile = (r + 1, c) if r + 1 < height and maze[r + 1][c] == '.' else (r - 2, c)
                    portal = maze[r - 1][c] + maze[r][c]
                    portals[portal] = portals.get(portal, []) + [tile]
                elif maze[r][c - 1].isalpha() and 1 < r < height - 2:
                    tile = (r, c + 1) if c + 1 < width and maze[r][c + 1] == '.' else (r, c - 2)
                    portal = maze[r][c - 1] + maze[r][c]
                    portals[portal] = portals.get(portal, []) + [tile]

    return portals


def get_portal_mapping(portals, height, width):
    portals_map = {}
    for portal, tiles in portals.items():
        if len(tiles) == 2:
            portals_map[tiles[0]] = (tiles[1], -1) \
                if tiles[0][0] in (2, height - 3) or tiles[0][1] in (2, width - 3) else (tiles[1], 1)
            portals_map[tiles[1]] = (tiles[0], -1) \
                if tiles[1][0] in (2, height - 3) or tiles[1][1] in (2, width - 3) else (tiles[0], 1)
    return portals_map


def find_shortest_distance(maze, portals_map, start, end):
    moves = ((-1, 0), (1, 0), (0, -1), (0, 1))
    visited = {(start, 0)}
    queue = [(start, 0)]
    dist = {(start, 0): 0}

    while len(queue):
        tile, level = queue.pop(0)
        current_moves = [((tile[0] + move[0], tile[1] + move[1]), 0) for move in moves]
        if tile in portals_map:
            current_moves.append(portals_map[tile])
        for new_tile, shift_level in current_moves:
            new_level = level + shift_level
            if new_level >= 0:
                if (new_tile, new_level) not in visited and maze[new_tile[0]][new_tile[1]] == '.':
                    visited.add((new_tile, new_level))
                    dist[(new_tile, new_level)] = dist[(tile, level)] + 1
                    queue.append((new_tile, new_level))
                    if new_tile == end and new_level == 0:
                        return dist[(new_tile, new_level)]

    return None


def count_steps(maze):
    height = len(maze)
    width = len(maze[0])
    portals = parse_maze(maze, height, width)
    portals_map = get_portal_mapping(portals, height, width)
    return find_shortest_distance(maze, portals_map, portals['AA'][0], portals['ZZ'][0])


if __name__ == "__main__":
    with open('day20/input.txt') as inp:
        m = inp.read().split('\n')

    m = [line + ' ' * (max(len(item) for item in m) - len(line)) for line in m]
    print(count_steps(m))  # 7568
