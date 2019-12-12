import itertools


def track_moons_moving(start_pos, num_to_track, dimen_num):
    moons_data = [(start_pos[i:i + dimen_num], [0, 0, 0]) for i in range(0, len(start_pos), dimen_num)]

    for _ in range(num_to_track):
        for idx1, idx2 in itertools.combinations(range(4), 2):
            for i in range(dimen_num):
                if moons_data[idx1][0][i] > moons_data[idx2][0][i]:
                    moons_data[idx1][1][i] -= 1
                    moons_data[idx2][1][i] += 1
                elif moons_data[idx1][0][i] < moons_data[idx2][0][i]:
                    moons_data[idx1][1][i] += 1
                    moons_data[idx2][1][i] -= 1
        for moon in moons_data:
            for i in range(dimen_num):
                moon[0][i] += moon[1][i]

    return int(sum([sum(map(abs, moon[0])) * sum(map(abs, moon[1])) for moon in moons_data]))


if __name__ == "__main__":
    with open('day12/input.txt') as inp:
        pos = [int(dimen.split('=')[1]) for line in inp for dimen in line.strip('><\n ').split(', ')]

    print(track_moons_moving(pos, 1000, 3))  # 9876
