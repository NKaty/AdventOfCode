from copy import deepcopy
from Interpreter import Interpreter


def process_instructions(interpreter, instructions):
    if not len(instructions):
        return
    outputs = set()
    for output in interpreter.launch_process(instructions):
        if output[1] in outputs:
            return outputs
        outputs.add(output[1])
    return output[0]


def find_accumulator_after_fixing(instructions):
    swap_map = {
        'jmp': 'nop',
        'nop': 'jmp'
    }
    interpreter = Interpreter()
    outputs = process_instructions(interpreter, instructions)
    possible_errors = set(filter(lambda x: instructions[x][0] in ('jmp', 'nop'), outputs))

    for index in possible_errors:
        current_instructions = deepcopy(instructions)
        current_instructions[index][0] = swap_map[current_instructions[index][0]]
        accumulator = process_instructions(interpreter, current_instructions)
        if type(accumulator) is int:
            return accumulator


if __name__ == "__main__":
    with open('day08/input.txt') as inp:
        data = list(map(lambda x: [x[0], int(x[1])], (line.strip().split() for line in inp)))

    print(find_accumulator_after_fixing(data))  # 1532
