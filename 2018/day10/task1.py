import re
from copy import deepcopy


def check_message(points):
    min_x = min(points, key=lambda item: item[0])[0]
    max_x = max(points, key=lambda item: item[0])[0]
    min_y = min(points, key=lambda item: item[1])[1]
    max_y = max(points, key=lambda item: item[1])[1]
    return max_x - min_x, max_y - min_y, min_x, max_x, min_y, max_y


def print_message(points, board):
    points = set(tuple(item[:2]) for item in points)
    min_x, max_x, min_y, max_y = board
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if (x, y) in points:
                print('#', end='')
            else:
                print('.', end='')
        print()


def get_message(points):
    prev_check = None
    while True:
        prev_points = deepcopy(points)
        points = [[item[0] + item[2], item[1] + item[3], item[2], item[3]] for item in points]
        check = check_message(points)
        if prev_check and prev_check[0] < check[0] and prev_check[1] < check[1]:
            return prev_points, prev_check[2:]
        prev_check = check


if __name__ == "__main__":
    reg = re.compile(r'[-\d]+')
    with open('day10/input.txt') as inp:
        data = [list(map(int, re.findall(reg, line))) for line in inp]

    print_message(*get_message(data))  # ZAEZRLZG
