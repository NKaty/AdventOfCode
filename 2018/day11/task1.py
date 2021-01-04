def find_square_with_largest_power(sn, cn, sqn):
    grid = [[0 for _ in range(cn)] for _ in range(cn)]
    for x in range(cn):
        for y in range(cn):
            power = int(str(((x + 1 + 10) * (y + 1) + sn) * (x + 1 + 10))[-3]) - 5
            grid[x][y] = power + grid[x - 1][y] + grid[x][y - 1] - grid[x - 1][y - 1]

    square_power = []
    for x in range(cn - sqn + 1):
        for y in range(cn - sqn + 1):
            x0 = x - 1 if x - 1 >= 0 else 0
            y0 = y - 1 if y - 1 >= 0 else 0
            x1 = x + sqn - 1
            y1 = y + sqn - 1
            square_power.append(
                (grid[x0][y0] + grid[x1][y1] - grid[x0][y1] - grid[x1][y0], (x + 1, y + 1)))

    return ','.join(map(str, max(square_power)[1]))


if __name__ == "__main__":
    with open('day11/input.txt') as inp:
        serial_number = int(inp.read().strip())

    print(find_square_with_largest_power(serial_number, 300, 3))  # 235,38
