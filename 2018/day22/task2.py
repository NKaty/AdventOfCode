from collections import defaultdict
import heapq


def get_grid(depth, target):
    depth = int(depth)
    grid = {}

    for y in range(target[1] + 100):
        for x in range(3 * target[0]):
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

    return grid


def get_graph(grid, target):
    tools = {
        0: (0, 1),  # rocky - torch, climbing gear
        1: (1, 2),  # wet - climbing gear, neither tool
        2: (0, 2)  # narrow - torch, neither tool
    }
    shifts = (0, 1), (0, -1), (1, 0), (-1, 0)
    graph = defaultdict(list)

    for y in range(target[1] + 100):
        for x in range(3 * target[0]):
            possible_tools = tools[grid[(x, y)][1]]
            for tool in possible_tools:
                for shift in shifts:
                    nb_coord = x + shift[0], y + shift[1]
                    if nb_coord in grid:
                        nb_tools = tools[grid[nb_coord][1]]
                        for nb_tool in nb_tools:
                            dist = 1 if tool == nb_tool else 8 if nb_tool in tools[
                                grid[(x, y)][1]] else 15
                            graph[((x, y), tool)].append((dist, nb_coord, nb_tool))

    return graph


def find_dijkstra_path(graph, start, end):
    hq = [(0, start, 0)]
    prev = {(start, 0): 0}
    seen = set()

    while hq:
        d, coord, tool = heapq.heappop(hq)
        seen.add((coord, tool))
        for nb_d, nb_coord, nb_tool in graph[(coord, tool)]:
            if (nb_coord, nb_tool) not in seen:
                next_d = d + nb_d
                if (nb_coord, nb_tool) not in prev or prev[(nb_coord, nb_tool)] > next_d:
                    prev[(nb_coord, nb_tool)] = next_d
                    heapq.heappush(hq, (next_d, nb_coord, nb_tool))

    return prev[(end, 0)]


def find_fastest_path(depth, target):
    target = tuple(map(int, target.split(',')))
    grid = get_grid(depth, target)
    graph = get_graph(grid, target)
    return find_dijkstra_path(graph, (0, 0), target)


if __name__ == "__main__":
    with open('day22/input.txt') as inp:
        data = [line.strip().split(': ')[1] for line in inp]

    print(find_fastest_path(data[0], data[1]))  # 1025
