import math


def find_seat_id(boarding_pass):
    height = [0, 127]
    width = [0, 7]
    for char in boarding_pass:
        if char in ('F', 'B'):
            middle = math.floor((height[0] + height[1]) / 2)
            if char == 'F':
                height[1] = middle
            else:
                height[0] = middle + 1
        if char in ('L', 'R'):
            middle = math.floor((width[0] + width[1]) / 2)
            if char == 'L':
                width[1] = middle
            else:
                width[0] = middle + 1
    return height[0] * 8 + width[0]


def find_seat(passes):
    ids = sorted(find_seat_id(item) for item in passes)
    width = [0, len(ids) - 1]
    while width[0] <= width[1]:
        middle = math.floor((width[0] + width[1]) / 2)
        if ids[middle + 1] != ids[middle] + 1:
            return ids[middle] + 1
        if ids[middle] == ids[width[0]] + middle - width[0]:
            width[0] = middle + 1
        else:
            width[1] = middle - 1


if __name__ == "__main__":
    with open('day05/input.txt') as inp:
        boarding_passes = tuple(line.strip() for line in inp)

    print(find_seat(boarding_passes))  # 633
