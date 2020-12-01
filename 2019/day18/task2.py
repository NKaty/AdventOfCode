import copy
import math


def get_grid_info(grid, letters):
    keys = {}
    entrance_shifts = ((1, 1), (-1, -1), (1, -1), (-1, 1))
    wall_shifts = ((0, 1), (0, -1), (1, 0), (-1, 0))
    old_entrance = 0
    entrances = []

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '@':
                old_entrance = row, col
                grid[row][col] = '#'
            if grid[row][col] in letters.lower():
                keys[grid[row][col]] = row, col
    for shift in wall_shifts:
        grid[old_entrance[0] + shift[0]][old_entrance[1] + shift[1]] = '#'
    for shift in entrance_shifts:
        grid[old_entrance[0] + shift[0]][old_entrance[1] + shift[1]] = '.'
        entrances.append((old_entrance[0] + shift[0], old_entrance[1] + shift[1]))

    if not old_entrance:
        raise Exception('No entrance!')

    return entrances, keys


def find_shortest_path(grid, letters):
    entrances, all_keys = get_grid_info(grid, letters)
    keys_map_memo = {}
    shortest_path_memo = {}
    open_doors = {'.'}

    def get_keys_map(row, col, op_d):
        memo_key = (row, col, ''.join(sorted(list(op_d))))
        if memo_key in keys_map_memo:
            return keys_map_memo[memo_key]
        keys = {}
        visited = {}
        shifts = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def get_keys_map_traverse(r, c, dist):
            if (r, c) in visited and visited[(r, c)] <= dist:
                return
            visited[(r, c)] = dist
            if grid[r][c] not in op_d and grid[r][c] not in letters.lower():
                return
            if grid[r][c] in letters.lower() and grid[r][c].upper() not in op_d:
                keys[grid[r][c].upper()] = (r, c, dist)
            else:
                for shift in shifts:
                    get_keys_map_traverse(r + shift[0], c + shift[1], dist + 1)

        get_keys_map_traverse(row, col, 0)
        keys_map_memo[memo_key] = keys

        return keys

    def find_shortest_path_traverse(entrs, op_d):
        if all([key.upper() in op_d for key in all_keys]):
            return 0, ''

        memo_key = (''.join([''.join([str(i) for i in item]) for item in entrs]), ''.join(sorted(list(op_d))))
        if memo_key in shortest_path_memo:
            return shortest_path_memo[memo_key]

        all_paths = {}
        for entrance_index, tile in enumerate(entrs):
            all_paths[entrance_index] = get_keys_map(tile[0], tile[1], op_d)
        best_dist = math.inf
        best_path = ''

        for entrance_index, paths in all_paths.items():
            for k, path in paths.items():
                current_op_d = copy.copy(op_d)
                current_op_d.add(k.upper())
                new_entrances = copy.deepcopy(entrs)
                new_entrances[entrance_index] = (path[0], path[1])
                shortest_dist, shortest_path = find_shortest_path_traverse(new_entrances, current_op_d)
                new_dist = path[2] + shortest_dist
                if new_dist < best_dist:
                    best_dist = new_dist
                    best_path = k.upper() + shortest_path
        shortest_path_memo[memo_key] = (best_dist, best_path)

        return shortest_path_memo[memo_key]

    return find_shortest_path_traverse(entrances, open_doors)


if __name__ == "__main__":
    with open('day18/input.txt') as inp:
        vault_map = [list(line.strip()) for line in inp]

    print(find_shortest_path(vault_map, 'abcdefghijklmnopqrstuvwxyz')[0])  # 1844
