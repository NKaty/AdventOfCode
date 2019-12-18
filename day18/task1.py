import copy
import math


def get_grid_info(grid, letters):
    keys = {}
    entrance = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '@':
                entrance = row, col
                grid[row][col] = '.'
            if grid[row][col] in letters.lower():
                keys[grid[row][col]] = row, col

    if not entrance:
        raise Exception('No entrance!')

    return entrance, keys


def find_shortest_path(grid, letters):
    entrance, all_keys = get_grid_info(grid, letters)
    memo = {}
    open_doors = {'.'}

    def traverse(row, col, op_d):
        if all([key.upper() in op_d for key in all_keys]):
            return 0, ''

        memo_key = (row, col, ''.join(sorted(list(op_d))))
        if memo_key in memo:
            return memo[memo_key]

        all_paths = get_keys_map(grid, row, col, op_d, letters)
        best_dist = math.inf
        best_path = ''

        for k, path in all_paths.items():
            current_op_d = copy.copy(op_d)
            current_op_d.add(k.upper())
            shortest_dist, shortest_path = traverse(path[0], path[1], current_op_d)
            new_dist = path[2] + shortest_dist
            if new_dist < best_dist:
                best_dist = new_dist
                best_path = k.upper() + shortest_path
        memo[memo_key] = (best_dist, best_path)

        return memo[memo_key]

    return traverse(entrance[0], entrance[1], open_doors)


def get_keys_map(grid, row, col, open_doors, letters):
    keys = {}
    visited = {}
    shifts = ((0, 1), (0, -1), (1, 0), (-1, 0))

    def traverse(r, c, dist):
        if (r, c) in visited and visited[(r, c)] <= dist:
            return
        visited[(r, c)] = dist
        if grid[r][c] not in open_doors and grid[r][c] not in letters.lower():
            return
        if grid[r][c] in letters.lower() and grid[r][c].upper() not in open_doors:
            keys[grid[r][c].upper()] = (r, c, dist)
        else:
            for shift in shifts:
                traverse(r + shift[0], c + shift[1], dist + 1)

    traverse(row, col, 0)
    return keys


if __name__ == "__main__":
    with open('day18/input.txt') as inp:
        vault_map = [list(line.strip()) for line in inp]

    print(find_shortest_path(vault_map, 'abcdefghijklmnopqrstuvwxyz')[0])  # 3962
