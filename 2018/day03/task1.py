import re


def find_overlap(squares):
    squares = [set((i, j) for i in range(square[0] + 1, square[0] + square[2] + 1) for j in
                   range(square[1] + 1, square[1] + square[3] + 1)) for square in squares]

    overlap = set()
    for i in range(len(squares) - 1):
        for j in range(i + 1, len(squares)):
            overlap |= (squares[i] & squares[j])

    return len(overlap)


if __name__ == "__main__":
    reg = re.compile(r'^#\d+ @ (\d+),(\d+): (\d+)x(\d+)$')
    with open('day03/input.txt') as inp:
        claims = [tuple(map(int, re.match(reg, line.strip()).groups())) for line in inp]

    print(find_overlap(claims))  # 104439
