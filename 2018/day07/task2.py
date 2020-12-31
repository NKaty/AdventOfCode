from collections import defaultdict
from string import ascii_uppercase


def find_completion_time(steps):
    graph = defaultdict(list)
    for instruction in steps:
        graph[instruction[1]].append(instruction[0])

    time_map = {char: i + 61 for i, char in enumerate(ascii_uppercase)}
    remains = set([item[0] for item in steps] + [item[1] for item in steps])
    result = ''
    workers = [0] * 5
    works = [None] * 5
    seconds = -1
    while remains or any(worker > 0 for worker in workers):
        for i, worker in enumerate(workers):
            if worker == 1:
                result += works[i]
            workers[i] = max(0, worker - 1)

        free_workers = [i for i, worker in enumerate(workers) if worker == 0]
        currents = sorted([item for item in remains if
                          item not in graph or all(char in result for char in graph[item])])

        for worker in free_workers:
            if not currents:
                break
            char = currents.pop(0)
            workers[worker] = time_map[char]
            works[worker] = char
            remains.remove(char)
        seconds += 1
    return seconds


if __name__ == "__main__":
    with open('day07/input.txt') as inp:
        instructions = [(line[5], line[36]) for line in inp]

    print(find_completion_time(instructions))  # 1014
