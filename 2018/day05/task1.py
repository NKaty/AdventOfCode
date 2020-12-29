from collections import deque


def find_resulting_polymer(polymer):
    stack = deque()
    for unit in polymer:
        if len(stack) and unit == stack[-1].swapcase():
            stack.pop()
        else:
            stack.append(unit)
    return len(stack)


if __name__ == "__main__":
    with open('day05/input.txt') as inp:
        chemical_composition = inp.read().strip()

    print(find_resulting_polymer(chemical_composition))  # 11264
