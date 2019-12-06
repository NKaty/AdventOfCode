def get_directed_graph(data):
    graph = {}
    for vert1, vert2 in data:
        if vert1 not in graph:
            graph[vert1] = []
        if vert2 not in graph:
            graph[vert2] = []
        if vert2 not in graph[vert1]:
            graph[vert1].append(vert2)
    return graph


# In case the universal center is not known and we need to determine it.
def topological_sort(graph):
    visited = set()
    sorted_list = []

    def traverse(vert):
        if vert not in visited:
            visited.add(vert)
            for linked_vert in graph[vert]:
                if linked_vert not in visited:
                    traverse(linked_vert)
            sorted_list.append(vert)

    for vert in graph.keys():
        traverse(vert)
    return sorted_list[::-1]


def depth_search(graph, start):
    orbits_num = []
    visited = set()

    def traverse(vert, count):
        orbits_num.append(count)
        visited.add(vert)
        for linked_vert in graph[vert]:
            if linked_vert not in visited:
                traverse(linked_vert, count + 1)

    traverse(start, 0)
    return sum(orbits_num)


with open('day6/input.txt') as inp:
    orbits = [line.strip().split(')') for line in inp]

directed_graph = get_directed_graph(orbits)

print(depth_search(directed_graph, 'COM'))  # 300598
print(depth_search(directed_graph, topological_sort(directed_graph)[0]))  # 300598
