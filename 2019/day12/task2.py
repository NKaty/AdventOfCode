import copy
import itertools
import math


def find_min_steps(steps):
    def lcm(a, b):
        return a * b // math.gcd(a, b)

    min_step = steps[0]
    for i in range(1, len(steps)):
        min_step = lcm(min_step, steps[i])
    return min_step


def track_moons_moving(start_pos, dimen_num):
    moon_num = int(len(start_pos) / dimen_num)
    moons_data = [([start_pos[j] for j in range(i, len(start_pos), dimen_num)], [0, 0, 0, 0])
                  for i in range(0, dimen_num)]
    moons_data_start = copy.deepcopy(moons_data)
    dimen_steps = []

    for i in range(dimen_num):
        steps = 0
        while True:
            for idx1, idx2 in itertools.combinations(range(4), 2):
                if moons_data[i][0][idx1] > moons_data[i][0][idx2]:
                    moons_data[i][1][idx1] -= 1
                    moons_data[i][1][idx2] += 1
                elif moons_data[i][0][idx1] < moons_data[i][0][idx2]:
                    moons_data[i][1][idx1] += 1
                    moons_data[i][1][idx2] -= 1
            for j in range(moon_num):
                moons_data[i][0][j] += moons_data[i][1][j]
            steps += 1
            if moons_data[i] == moons_data_start[i]:
                break
        dimen_steps.append(steps)

    return find_min_steps(dimen_steps)


if __name__ == "__main__":
    with open('day12/input.txt') as inp:
        pos = [int(dimen.split('=')[1]) for line in inp for dimen in line.strip('><\n ').split(', ')]

    print(track_moons_moving(pos, 3))  # 307043147758488
