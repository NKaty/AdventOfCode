def find_largest_area(coords):
    min_x = min(coords, key=lambda item: item[0])[0]
    max_x = max(coords, key=lambda item: item[0])[0]
    min_y = min(coords, key=lambda item: item[1])[1]
    max_y = max(coords, key=lambda item: item[1])[1]
    counts = {coord: 0 for coord in coords}

    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            dists = sorted([(coord, abs(y - coord[1]) + abs(x - coord[0])) for coord in coords],
                           key=lambda item: item[1])
            if dists[0][0] not in counts:
                continue
            if dists[0][1] != dists[1][1]:
                counts[dists[0][0]] += 1
            if x in (min_x, max_x) or y in (min_y, max_y):
                counts.pop(dists[0][0])

    return max(counts.values())


if __name__ == "__main__":
    with open('day06/input.txt') as inp:
        coordinates = [tuple(map(int, line.strip().split(', '))) for line in inp]

    print(find_largest_area(coordinates))  # 4771
