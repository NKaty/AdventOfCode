import re


def count_bags(graph, start):
    def traverse(nodes):
        return sum(node[0] * traverse(graph[node[1]]) for node in nodes) + 1

    return traverse(graph[start]) - 1


if __name__ == "__main__":
    reg = re.compile(r'(\d+) ([a-z]+ [a-z]+)')

    with open('day07/input.txt') as inp:
        lines = [line.strip().split(' bags contain ') for line in inp]

    luggage_rules = {line[0]: [(int(item[0]), item[1]) for item in re.findall(reg, line[1])] for
                     line in lines}
    print(count_bags(luggage_rules, 'shiny gold'))  # 50100
