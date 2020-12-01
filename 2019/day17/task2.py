import copy
from intcode import process_instructions


def find_robot_position(grid):
    robot_position = None
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] in ('^', 'v', '<', '>'):
                robot_position = row, col
    if robot_position is None:
        raise Exception('There is no vacuum robot on the map.')
    return robot_position


def get_instruction_components(robot_path, max_len, func_num):
    robot_path = [f'{robot_path[i]},{str(robot_path[i + 1])}' for i in range(0, len(robot_path), 2)]
    max_len_robot_path = max_len // 4

    def traverse_path(path, functions, main_routine):
        # remove the found functions from the path
        while True:
            is_removed = False
            for i, function in enumerate(functions):
                if path[:len(function)] == function:
                    path = path[len(function):]
                    main_routine = main_routine[:] + [i]
                    is_removed = True
            if not is_removed:
                break

        # success, found the combination
        if not len(path):
            return functions, main_routine

        # number of functions already 3, so don't look further
        if len(functions) > func_num - 1:
            return [], []

        # try all possible combinations until the solution is found
        for i in range(max_len_robot_path, 0, -1):
            funcs, routine = traverse_path(path[:], copy.deepcopy(functions) + [path[:i]], main_routine[:])
            if len(funcs) == func_num:
                return funcs, routine

        # failure, did not find the combination
        return [], []

    return traverse_path(robot_path, [], [])


def get_robot_path(grid, tiles):
    height = len(grid)
    width = len(grid[0])
    row, col = find_robot_position(grid)
    directions = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
    turn_left = {(0, 1): (-1, 0), (0, -1): (1, 0), (1, 0): (0, 1), (-1, 0): (0, -1)}
    turn_right = {(1, 0): (0, -1), (0, 1): (1, 0), (0, -1): (-1, 0), (-1, 0): (0, 1)}
    robot_path = []
    shift = directions[grid[row][col]]

    def check_new_pos(r, c):
        return 0 <= r < height and 0 <= c < width and grid[r][c] == tiles['scaffold']

    while True:
        if check_new_pos(row + shift[0], col + shift[1]):
            row, col = row + shift[0], col + shift[1]
            robot_path[-1] += 1
            continue
        if check_new_pos(row + turn_right[shift][0], col + turn_right[shift][1]):
            shift = turn_right[shift]
            row, col = row + shift[0], col + shift[1]
            robot_path += ['R', 1]
            continue
        if check_new_pos(row + turn_left[shift][0], col + turn_left[shift][1]):
            shift = turn_left[shift]
            row, col = row + shift[0], col + shift[1]
            robot_path += ['L', 1]
        else:
            break

    return robot_path


def count_dust(data, tiles, max_func_len, functions_names):
    grid = []
    gen = process_instructions(data, [])

    grid_row = ''
    while True:
        while (output := next(gen)) != 10:
            grid_row += chr(output)
        if not grid_row and output == 10:
            break
        grid.append(grid_row)
        print(grid_row)
        grid_row = ''

    robot_path = get_robot_path(grid, tiles)
    functions, main_routine = get_instruction_components(list(map(str, robot_path)), max_func_len, len(functions_names))

    if not len(functions) or not len(main_routine):
        raise Exception('There are no combination to solve the puzzle.')

    main_routine = ','.join([functions_names[item] for item in main_routine])
    functions = '\n'.join([','.join(func) for func in functions])
    instructions = f'{main_routine}\n{functions}\nn\n'

    output = gen.send((list(map(ord, instructions))))
    message = ''
    while output is not None and output < 256:
        message += chr(output)
        output = next(gen)
    print(message)

    return output


if __name__ == "__main__":
    with open('day17/input.txt') as inp:
        ns = list(map(int, inp.read().strip().split(',')))
    ns[0] = 2

    print(count_dust(ns, {'scaffold': '#', 'open_space': '.'}, 20, ('A', 'B', 'C')))  # 578918
