import re


def reverse_graph(graph):
    reversed_graph = {}
    for bag, content in graph.items():
        if bag not in reversed_graph:
            reversed_graph[bag] = []
        for item in content:
            reversed_graph[item] = reversed_graph.get(item, []) + [bag]
    return reversed_graph


def count_bag_colors(graph, searching_for):
    reversed_graph = reverse_graph(graph)
    visited = set()

    def traverse(nodes):
        for node in nodes:
            if node not in visited:
                visited.add(node)
                traverse(reversed_graph[node])

    traverse(reversed_graph[searching_for])

    return len(visited)


if __name__ == "__main__":
    reg = re.compile(r'(\d+) ([a-z]+ [a-z]+)')

    with open('day07/input.txt') as inp:
        lines = [line.strip().split(' bags contain ') for line in inp]

    luggage_rules = {line[0]: [item[1] for item in re.findall(reg, line[1])] for line in lines}
    print(count_bag_colors(luggage_rules, 'shiny gold'))  # 337
