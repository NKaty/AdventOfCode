import re


def find_nanobots(bots):
    max_coord, max_r = max(bots, key=lambda item: item[1])
    return sum(sum(map(abs, (m - b for m, b in zip(max_coord, bot[0])))) <= max_r for bot in bots)


if __name__ == "__main__":
    reg = re.compile(r'-?\d+')
    with open('day23/input.txt') as inp:
        data = [list(map(int, re.findall(reg, line.strip()))) for line in inp]
    data = [(item[:3], item[3]) for item in data]

    print(find_nanobots(data))  # 442
