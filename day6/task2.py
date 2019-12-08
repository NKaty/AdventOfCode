def get_undirected_graph(data):
    graph = {}
    for vert1, vert2 in data:
        if vert1 not in graph:
            graph[vert1] = []
        if vert2 not in graph:
            graph[vert2] = []
        if vert2 not in graph[vert1]:
            graph[vert1].append(vert2)
            graph[vert2].append(vert1)
    return graph


def find_shortest_distance(graph, start, end):
    visited = {start}
    queue = [start]
    dist = {start: 0}

    while len(queue):
        vert = queue.pop(0)
        for linked_vert in graph[vert]:
            if linked_vert not in visited:
                visited.add(linked_vert)
                dist[linked_vert] = dist[vert] + 1
                queue.append(linked_vert)
                if linked_vert == end:
                    return dist[linked_vert]

    return None


if __name__ == "__main__":
    with open('day6/input.txt') as inp:
        orbits = [line.strip().split(')') for line in inp]

    undirected_graph = get_undirected_graph(orbits)

    # We need to find the distance between the objects,
    # YOU and SAN are orbiting - not between YOU and SAN.
    print(find_shortest_distance(undirected_graph, 'YOU', 'SAN') - 2)  # 520
