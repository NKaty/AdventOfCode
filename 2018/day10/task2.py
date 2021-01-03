import re


def check_message(points):
    min_x = min(points, key=lambda item: item[0])[0]
    max_x = max(points, key=lambda item: item[0])[0]
    min_y = min(points, key=lambda item: item[1])[1]
    max_y = max(points, key=lambda item: item[1])[1]
    return max_x - min_x, max_y - min_y, min_x, max_x, min_y, max_y


def find_seconds_to_wait(points):
    prev_check = None
    seconds = 0
    while True:
        points = [[item[0] + item[2], item[1] + item[3], item[2], item[3]] for item in points]
        check = check_message(points)
        if prev_check and prev_check[0] < check[0] and prev_check[1] < check[1]:
            return seconds
        prev_check = check
        seconds += 1


if __name__ == "__main__":
    reg = re.compile(r'[-\d]+')
    with open('day10/input.txt') as inp:
        data = [list(map(int, re.findall(reg, line))) for line in inp]

    print(find_seconds_to_wait(data))  # 10105
