def count_trees(grid):
    width = len(grid[0])
    shift = (3, 1)
    coord = [0, 0]
    count = 0
    while coord[1] < len(grid) - 1:
        if grid[coord[1]][coord[0]] == '#':
            count += 1
        coord = [(coord[0] + shift[0]) % width, coord[1] + shift[1]]
    return count


if __name__ == "__main__":
    with open('day03/input.txt') as inp:
        trees_map = tuple(tuple(line.strip()) for line in inp)

    print(count_trees(trees_map))  # 181
