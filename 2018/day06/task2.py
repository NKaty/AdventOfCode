def find_total_distance(coords, total_dist):
    min_x = min(coords, key=lambda item: item[0])[0]
    max_x = max(coords, key=lambda item: item[0])[0]
    min_y = min(coords, key=lambda item: item[1])[1]
    max_y = max(coords, key=lambda item: item[1])[1]

    return sum(sum(abs(y - coord[1]) + abs(x - coord[0]) for coord in coords) < total_dist for x in
               range(min_x, max_x + 1) for y in range(min_y, max_y + 1))


if __name__ == "__main__":
    with open('day06/input.txt') as inp:
        coordinates = [tuple(map(int, line.strip().split(', '))) for line in inp]

    print(find_total_distance(coordinates, 10000))  # 39149
