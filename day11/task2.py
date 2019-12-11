import itertools
import math


def get_instructions(opcode):
    opc_list = [opcode % 100]
    opcode = opcode // 100

    while len(opc_list) < 4:
        opc_list.append(opcode % 10)
        opcode = opcode // 10

    if opc_list[0] not in list(range(1, 10)) + [99] \
            or not all(opc_list[i] in range(3) for i in (1, 2)) \
            or opc_list[3] not in (0, 2):
        raise Exception('Wrong opcode.')

    return opc_list


def get_value(list_, i, default=0):
    try:
        el = list_[i]
    except IndexError:
        el = default
    finally:
        return el


def extend_list(list_, i):
    try:
        el = list_[i]
    except IndexError:
        list_ = list_ + [0] * (i - len(list_) + 1)
    finally:
        return list_


def process_instructions(numbers, inputs, relative_base=0):
    def get_index(idx, mode):
        if mode == 1:
            raise Exception('Wrong mode.')
        return numbers[idx] if mode == 0 else numbers[idx] + relative_base

    def get_param(idx, mode):
        if mode == 1:
            return numbers[idx]
        new_idx = get_index(idx, mode)
        return get_value(numbers, new_idx)

    i = 0
    input_index = 0
    outputs = []

    while i < len(numbers):
        opcode = get_instructions(numbers[i])

        if opcode[0] in (1, 2, 5, 6, 7, 8):
            param1 = get_param(i + 1, opcode[1])
            param2 = get_param(i + 2, opcode[2])
            if opcode[0] in (1, 2, 7, 8):
                index3 = get_index(i + 3, opcode[3])
        if opcode[0] in (4, 9):
            param1 = get_param(i + 1, opcode[1])

        if opcode[0] in (1, 2):
            numbers = extend_list(numbers, index3)
            numbers[index3] = param1 + param2 if opcode[0] == 1 else param1 * param2
            i += 4
        elif opcode[0] == 3:
            try:
                index1 = get_index(i + 1, opcode[1])
                numbers = extend_list(numbers, index1)
                numbers[index1] = inputs[input_index]
                input_index += 1
                i += 2
            except IndexError:
                raise Exception('No input to process.')
        elif opcode[0] == 4:
            outputs.append(param1)
            if len(outputs) == 2:
                new_input = yield outputs
                outputs = []
                if new_input is not None:
                    inputs.append(new_input)
            i += 2
        elif opcode[0] == 5:
            i = i + 3 if param1 == 0 else param2
        elif opcode[0] == 6:
            i = param2 if param1 == 0 else i + 3
        elif opcode[0] == 7:
            numbers = extend_list(numbers, index3)
            numbers[index3] = 1 if param1 < param2 else 0
            i += 4
        elif opcode[0] == 8:
            numbers = extend_list(numbers, index3)
            numbers[index3] = 1 if param1 == param2 else 0
            i += 4
        elif opcode[0] == 9:
            relative_base += param1
            i += 2
        elif opcode[0] == 99:
            yield None
        else:
            raise Exception('Wrong opcode.')


def build_robot(numbers, start):
    # (row, col): color
    robot_moves = {}
    # up, right, down, left
    positions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    # row, col, position
    robot_position = [0, 0, 0]
    gen = process_instructions(numbers, start)

    def update_robot_position(dirct):
        if dirct:
            robot_position[2] = robot_position[2] + 1 if robot_position[2] < 3 else 0
        else:
            robot_position[2] = robot_position[2] - 1 if robot_position[2] > 0 else 3
        robot_position[0] += positions[robot_position[2]][0]
        robot_position[1] += positions[robot_position[2]][1]

    output = next(gen)

    while True:
        if output is None:
            break
        color, pos = output
        robot_moves[(robot_position[0], robot_position[1])] = color
        update_robot_position(pos)
        output = gen.send(robot_moves.get((robot_position[0], robot_position[1]), 0))

    return robot_moves


def print_identifier(coords):
    rows = [item[0] for item in coords.keys()]
    cols = [item[1] for item in coords.keys()]
    min_row = math.fabs(min(rows))
    min_col = math.fabs(min(cols))
    row_limit = int(min_row + math.fabs(max(rows)) + 1)
    col_limit = int(min_col + math.fabs(max(cols)) + 1)
    new_coords = {}

    for coord in coords.items():
        new_coords[coord[0][0] + min_row, coord[0][1] + min_col] = 'X' if coord[1] == 1 else ' '

    for item in itertools.product(range(0, row_limit), range(0, col_limit)):
        print(new_coords.get(item, ' '), end='')
        if item[1] == col_limit - 1:
            print()


if __name__ == "__main__":
    with open('day11/input.txt') as inp:
        ns = list(map(int, inp.read().strip().split(',')))

    robot_coords = build_robot(ns, [1])
    print_identifier(robot_coords)  # AKERJFHK
