def manhattan_distance(a, b):
    return sum(abs(ac - bc) for ac, bc in zip(a, b))


def count_constellations(coords):
    constellations = [{coords[0]}]
    for coord in coords:
        found = []
        for i, constellation in enumerate(constellations):
            if any(manhattan_distance(coord, c_coord) <= 3 for c_coord in constellation):
                found.append(i)
        if not found:
            constellations.append({coord})
        elif len(found) == 1:
            constellations[found[0]].add(coord)
        else:
            new_item = set()
            for item in found[::-1]:
                new_item |= constellations[item]
                constellations.pop(item)
            new_item.add(coord)
            constellations.append(new_item)

    return len(constellations)


if __name__ == "__main__":
    with open('day25/input.txt') as inp:
        data = [tuple(map(int, line.strip().split(','))) for line in inp]

    print(count_constellations(data))  # 428
