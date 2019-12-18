import copy
from intcode import process_instructions


def find_robot_position(grid):
    scaffold_number = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 94:
                robot_position = row, col
            if grid[row][col] == 35:
                scaffold_number += 1
    return robot_position, scaffold_number


def print_grid(grid):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 94:
                print('R', end='')
            elif grid[row][col] == 35:
                print('#', end='')
            else:
                print('.', end='')
        print()


def get_movement_sequence(path):
    shifts = {(0, 1, 1, 0): ['R'], (0, 1, -1, 0): ['L'], (0, -1, -1, 0): ['R'], (0, -1, 1, 0): ['L'], (1, 0, 0, -1): ['R'],
              (1, 0, 0, 1): ['L'], (-1, 0, 0, 1): ['R'], (-1, 0, 0, -1): ['L'], (1, 0, -1, 0): ['R', 0, 'R'], (-1, 0, 1, 0): ['R', 0, 'R'], (0, 1, 0, -1): ['R', 0, 'R']}
    movement_sequence = ['R']
    current_shift = (path[1][0] - path[0][0], path[1][1] - path[0][1])
    count = 0
    for i in range(len(path) - 1):
        shift = (path[i + 1][0] - path[i][0], path[i + 1][1] - path[i][1])
        if shift == current_shift:
            count += 1
        else:
            print(current_shift + shift, count, path[i][1], path[i][0], path[i + 1][1], path[i + 1][0])
            movement_sequence.append(count)
            movement_sequence += shifts[current_shift + shift]
            current_shift = shift
            count = 1
    print(movement_sequence)


def get_intersections(grid):
    intersections = []
    shifts = ((0, 1), (0, -1), (1, 0), (-1, 0))
    for row in range(1, len(grid) - 2):
        for col in range(1, len(grid[0]) - 1):
            if grid[row][col] == 35 and all([grid[row + shift[0]][col + shift[1]] == 35 for shift in shifts]):
                intersections.append((row, col))
    return intersections


def tr(grid):
    # grid = get_scaffold_grid(data)
    rows = len(grid)
    cols = len(grid[0])
    robot_position, scaffold_number = find_robot_position(grid)
    print(scaffold_number)
    intersections = get_intersections(grid)
    # print(robot_position, scaffold_number)
    paths = []
    shifts = ((0, 1), (0, -1), (1, 0), (-1, 0))

    def find_paths(tile, visited, path, prev_tiles, count):
        if len(paths) > 0:
            return
        current_path = copy.deepcopy(path)
        current_visited = copy.deepcopy(visited)
        current_prev_tiles = copy.deepcopy(prev_tiles)
        current_path.append(tile)
        current_visited.add(tile)
        unvisited_tiles = []
        # print(count)
        current_count = count + 1
        current_intersections = []
        count_deadend = 0
        for shift in shifts:
            # print(tile, shift)
            row = tile[0] + shift[0]
            col = tile[1] + shift[1]
            if row < 0 or row >= rows or col < 0 or col >= cols:
                count_deadend += 1
                continue
            if grid[row][col] == 46:
                count_deadend += 1
                continue
            if (row, col) in current_visited:
                if (row, col) in intersections:
                    current_intersections.append((row, col))
                continue

            unvisited_tiles.append((row, col))

        # unvisited_tiles = [(tile[0] + shift[0], tile[1] + shift[1]) for shift in shifts if
        #                    (tile[0] + shift[0], tile[1] + shift[1]) not in current_visited and grid[tile[0] + shift[0]][
        #                        tile[1] + shift[1]] == 35]
        # print(unvisited_tiles)
        if not len(unvisited_tiles) and len(current_path) == scaffold_number:
            # return path
            # print(path)
            paths.append(current_path)
            return
        elif not len(unvisited_tiles) and len(current_path) != scaffold_number and len(current_intersections):
            current_prev_tiles.append(tile)
            linked_tile = current_intersections.pop()
            # current_visited.discard(linked_tile)
            find_paths(linked_tile, current_visited, current_path, current_prev_tiles, current_count)
        elif not len(unvisited_tiles) and len(current_path) != scaffold_number and count_deadend == 3:
            if len(current_prev_tiles) - 1 < 0:
                return
            linked_tile = current_prev_tiles[len(current_prev_tiles) - 1]
            # print('link tile', linked_tile)
            # current_visited.discard(linked_tile)
            current_prev_tiles = current_prev_tiles[:-1]
            # print('cur prev tiles', current_prev_tile)
            find_paths(linked_tile, current_visited, current_path, current_prev_tiles, current_count)
        else:
            # print(unvisited_tiles)
            for linked_tile in unvisited_tiles:
                current_prev_tiles.append(tile)
                find_paths(linked_tile, current_visited, current_path, current_prev_tiles, current_count)

    find_paths(robot_position, set(), [], [], 0)
    return paths[0]


def get_scaffold_grid(data):
    gen = process_instructions(data, [])
    grid = []
    while (row := next(gen)) != []:
        grid.append(row)
    return grid


if __name__ == "__main__":
    with open('day17/input.txt') as inp:
        ns = list(map(int, inp.read().strip().split(',')))
    ns[0] = 2
    grid = get_scaffold_grid(ns)
    # print_grid(grid)
    p = tr(grid)
    print(len(p))
    get_movement_sequence(p)
    # print(count_alignment_params_sum(ns, {}))
