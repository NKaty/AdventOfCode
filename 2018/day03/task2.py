import re


def find_overlap(squares):
    squares = {square[0]: set(
        (i, j) for i in range(square[1] + 1, square[1] + square[3] + 1) for j in
        range(square[2] + 1, square[2] + square[4] + 1)) for square in squares}

    overlap = set()
    squares_list = list(squares.values())
    for i in range(len(squares_list) - 1):
        for j in range(i + 1, len(squares_list)):
            overlap |= (squares_list[i] & squares_list[j])

    diff = set.union(*squares_list) - overlap
    for _id, square in squares.items():
        if square.issubset(diff):
            return _id


if __name__ == "__main__":
    reg = re.compile(r'^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)$')
    with open('day03/input.txt') as inp:
        claims = [tuple(map(int, re.match(reg, line.strip()).groups())) for line in inp]

    print(find_overlap(claims))  # 701
