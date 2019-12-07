import itertools


def get_instructions(opcode):
    opc_list = [opcode % 100]
    opcode = opcode // 100

    while len(opc_list) < 4:
        opc_list.append(opcode % 10)
        opcode = opcode // 10

    if opc_list[0] not in list(range(1, 9)) + [99] \
            or not all(opc_list[i] in (0, 1) for i in (1, 2)) \
            or opc_list[3] != 0:
        raise Exception('Wrong opcode.')

    return opc_list


def process_instructions(numbers, inputs):
    i = 0
    input_index = 0

    while i < len(numbers):
        opcode = get_instructions(numbers[i])
        if opcode[0] in (1, 2, 5, 6, 7, 8):
            param1 = numbers[numbers[i + 1]] if opcode[1] == 0 else numbers[i + 1]
            param2 = numbers[numbers[i + 2]] if opcode[2] == 0 else numbers[i + 2]
        if opcode[0] in (1, 2):
            numbers[numbers[i + 3]] = param1 + param2 if opcode[0] == 1 else param1 * param2
            i += 4
        elif opcode[0] == 3:
            try:
                numbers[numbers[i + 1]] = inputs[input_index]
                input_index += 1
                i += 2
            except IndexError:
                raise Exception('No input to process.')
        elif opcode[0] == 4:
            output = numbers[numbers[i + 1]] if opcode[1] == 0 else numbers[i + 1]
            new_input = yield output
            inputs.append(new_input)
            i += 2
        elif opcode[0] == 5:
            i = i + 3 if param1 == 0 else param2
        elif opcode[0] == 6:
            i = param2 if param1 == 0 else i + 3
        elif opcode[0] == 7:
            numbers[numbers[i + 3]] = 1 if param1 < param2 else 0
            i += 4
        elif opcode[0] == 8:
            numbers[numbers[i + 3]] = 1 if param1 == param2 else 0
            i += 4
        elif opcode[0] == 99:
            yield None
        else:
            raise Exception('Wrong opcode.')


def get_max_output(numbers, phases, start):
    outputs = []

    if not len(phases):
        raise Exception('Length of the phase setting sequence must not be 0.')

    for phases_seq in itertools.permutations(phases, len(phases)):
        start_input = start
        gens = []
        for phase in phases_seq:
            gen = process_instructions(numbers[:], [phase, start_input])
            gens.append(gen)
            start_input = next(gen)
        for gen in itertools.cycle(gens):
            start_input = gen.send(start_input)
            if start_input is None:
                break
            output = start_input
        outputs.append(output)

    return max(outputs)


with open('day7/input.txt') as inp:
    ns = list(map(int, inp.read().strip().split(',')))

print(get_max_output(ns, (5, 6, 7, 8, 9), 0))  # 36384144
