from intcode import process_instructions


def count_tractor_beam_points(data, square):
    count = 0
    for row in range(square):
        for col in range(square):
            if process_instructions(data[:], [row, col])[0] == 1:
                count += 1
    return count


if __name__ == "__main__":
    with open('day19/input.txt') as inp:
        ns = list(map(int, inp.read().strip().split(',')))

    print(count_tractor_beam_points(ns, 50))  # 114
