from intcode import process_instructions


def find_square(data, square):
    shift = square - 1
    r = shift
    c = 0
    while True:
        while process_instructions(data[:], [c, r])[0] == 0:
            c += 1
        if process_instructions(data[:], [c + shift, r - shift])[0] == 1:
            return c, r - shift
        r += 1


if __name__ == "__main__":
    with open('day19/input.txt') as inp:
        ns = list(map(int, inp.read().strip().split(',')))

    col, row = find_square(ns, 100)
    print(col * 10000 + row)  # 10671712
