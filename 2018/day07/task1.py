from collections import defaultdict


def find_instruction_order(steps):
    graph = defaultdict(list)
    for instruction in steps:
        graph[instruction[1]].append(instruction[0])

    remains = set([item[0] for item in steps] + [item[1] for item in steps])
    result = ''
    while remains:
        current = sorted([item for item in remains if
                          item not in graph or all(char in result for char in graph[item])])[0]
        result += current
        remains.remove(current)
    return result


if __name__ == "__main__":
    with open('day07/input.txt') as inp:
        instructions = [(line[5], line[36]) for line in inp]

    print(find_instruction_order(instructions))  # EUGJKYFQSCLTWXNIZMAPVORDBH
