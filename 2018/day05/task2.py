from collections import deque
from string import ascii_lowercase


def find_resulting_polymer(polymer, removed):
    stack = deque()
    for unit in polymer:
        if unit in removed:
            continue
        if len(stack) and unit == stack[-1].swapcase():
            stack.pop()
        else:
            stack.append(unit)
    return len(stack)


def find_shortest_polymer(polymer):
    return min(find_resulting_polymer(polymer, (char, char.swapcase())) for char in ascii_lowercase)


if __name__ == "__main__":
    with open('day05/input.txt') as inp:
        chemical_composition = inp.read().strip()

    print(find_shortest_polymer(chemical_composition))  # 4552
