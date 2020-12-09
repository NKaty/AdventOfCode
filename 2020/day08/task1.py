from Interpreter import Interpreter


def find_accumulator_before_loop(instructions):
    interpreter = Interpreter()
    outputs = set()
    accumulator = 0
    for output in interpreter.launch_process(instructions):
        if output[1] in outputs:
            return accumulator
        outputs.add(output[1])
        accumulator = output[0]


if __name__ == "__main__":
    with open('day08/input.txt') as inp:
        data = list(map(lambda x: (x[0], int(x[1])), (line.strip().split() for line in inp)))

    print(find_accumulator_before_loop(data))  # 1675
