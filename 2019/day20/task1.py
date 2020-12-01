def parse_maze(maze):
    portals = {}
    height = len(maze)
    width = len(maze[0])
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


def get_portal_mapping(portals):
    portals_map = {}
    for portal, tiles in portals.items():
        if len(tiles) == 2:
            portals_map[tiles[0]] = tiles[1]
            portals_map[tiles[1]] = tiles[0]
    return portals_map


def find_shortest_distance(maze, portals_map, start, end):
    moves = ((-1, 0), (1, 0), (0, -1), (0, 1))
    visited = {start}
    queue = [start]
    dist = {start: 0}

    while len(queue):
        tile = queue.pop(0)
        current_moves = [(tile[0] + move[0], tile[1] + move[1]) for move in moves]
        if tile in portals_map:
            current_moves.append(portals_map[tile])
        for new_tile in current_moves:
            if new_tile not in visited and maze[new_tile[0]][new_tile[1]] == '.':
                visited.add(new_tile)
                dist[new_tile] = dist[tile] + 1
                queue.append(new_tile)
                if new_tile == end:
                    return dist[new_tile]

    return None


def count_steps(maze):
    portals = parse_maze(maze)
    portals_map = get_portal_mapping(portals)
    return find_shortest_distance(maze, portals_map, portals['AA'][0], portals['ZZ'][0])


if __name__ == "__main__":
    with open('day20/input.txt') as inp:
        m = inp.read().split('\n')

    m = [line + ' ' * (max(len(item) for item in m) - len(line)) for line in m]
    print(count_steps(m))  # 666
