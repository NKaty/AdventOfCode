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


def find_highest_seat_id(passes):
    return max(find_seat_id(item) for item in passes)


if __name__ == "__main__":
    with open('day05/input.txt') as inp:
        boarding_passes = tuple(line.strip() for line in inp)

    print(find_highest_seat_id(boarding_passes))  # 861
