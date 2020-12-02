import re


def find_valid_passwords(passwords):
    return sum((item[3][item[0] - 1] == item[2] and item[3][item[1] - 1] != item[2]) or (
            item[3][item[0] - 1] != item[2] and item[3][item[1] - 1] == item[2]) for item in
               passwords)


if __name__ == "__main__":
    reg = r'(\d+)-(\d+) (\w): (\w+)'
    with open('day02/input.txt') as inp:
        lines = [tuple(map(lambda x: x[1] if x[0] > 1 else int(x[1]),
                           enumerate(re.match(reg, line.strip()).groups()))) for line in inp]

    print(find_valid_passwords(lines))  # 272
