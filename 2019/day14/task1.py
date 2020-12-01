import math


def get_directed_graph(data):
    graph = {}
    for inputs, output in data:
        inputs = tuple((int(chem[0]), chem[1]) for chem in (item.strip().split() for item in inputs.split(',')))
        output = output.strip().split()
        graph[output[1]] = (int(output[0]), inputs)
    return graph


def topological_sort(graph):
    visited = set()
    sorted_list = []

    def traverse(vert):
        if vert not in visited:
            visited.add(vert)
            if vert not in graph:
                return
            for linked_vert in graph[vert][1]:
                if linked_vert[1] not in visited:
                    traverse(linked_vert[1])
            sorted_list.append(vert)

    for vert in graph.keys():
        traverse(vert)
    return sorted_list[::-1]


def count_chemical_amounts(graph, needed_amount_fuel):
    sorted_chemicals = topological_sort(graph)
    amounts = {sorted_chemicals[0]: needed_amount_fuel}
    for vert in sorted_chemicals:
        for linked_vert in graph[vert][1]:
            amounts[linked_vert[1]] = \
                amounts.get(linked_vert[1], 0) + linked_vert[0] * math.ceil(amounts[vert] / graph[vert][0])
    return amounts


if __name__ == "__main__":
    with open('day14/input.txt') as inp:
        reactions = [line.strip().split('=>') for line in inp]

    reactions_graph = get_directed_graph(reactions)
    print(count_chemical_amounts(reactions_graph, 1)['ORE'])  # 273638
