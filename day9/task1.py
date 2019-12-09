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


def process_instructions(numbers, inputs, relative_base):
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
            return outputs
        else:
            raise Exception('Wrong opcode.')


def check_output(output):
    if len(list(filter(lambda x: x != 0, output))) > 1:
        raise Exception('There is more than one Non-zero output. Check your program.')
    return output[len(output) - 1]


if __name__ == "__main__":
    with open('day9/input.txt') as inp:
        ns = list(map(int, inp.read().strip().split(',')))

    print(check_output(process_instructions(ns, [1], 0)))  # 2714716640
