import re


def find_valid_passwords(passwords):
    return sum(
        [bool(re.fullmatch(rf'(?:[^{item[2]}]*{item[2]}){{{item[0]},{item[1]}}}[^{item[2]}]*',
                           item[3])) for item in passwords])


if __name__ == "__main__":
    reg = r'(\d+)-(\d+) (\w): (\w+)'
    with open('day02/input.txt') as inp:
        lines = [re.match(reg, line.strip()).groups() for line in inp]

    print(find_valid_passwords(lines))  # 383
