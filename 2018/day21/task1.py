def execute_program(ip, instructions):
    operations = {
        'addr': lambda r, o: r[o[1]] + r[o[2]],
        'addi': lambda r, o: r[o[1]] + o[2],
        'mulr': lambda r, o: r[o[1]] * r[o[2]],
        'muli': lambda r, o: r[o[1]] * o[2],
        'banr': lambda r, o: r[o[1]] & r[o[2]],
        'bani': lambda r, o: r[o[1]] & o[2],
        'borr': lambda r, o: r[o[1]] | r[o[2]],
        'bori': lambda r, o: r[o[1]] | o[2],
        'setr': lambda r, o: r[o[1]],
        'seti': lambda r, o: o[1],
        'gtir': lambda r, o: 1 if o[1] > r[o[2]] else 0,
        'gtri': lambda r, o: 1 if r[o[1]] > o[2] else 0,
        'gtrr': lambda r, o: 1 if r[o[1]] > r[o[2]] else 0,
        'eqir': lambda r, o: 1 if o[1] == r[o[2]] else 0,
        'eqri': lambda r, o: 1 if r[o[1]] == o[2] else 0,
        'eqrr': lambda r, o: 1 if r[o[1]] == r[o[2]] else 0
    }
    result = [0 for _ in range(6)]

    while result[ip] < len(instructions):
        # The only instruction with register 0 in it is 28 - eqrr 3 0 5.
        # This instruction compares the values in the register 3 and 0 and stores the result
        # in register 5 - now the result is 0. To halt the program we need to set value
        # in register 5 to 1. For that we must set value in register 0 to value in register 3.
        # With register 0 set to 7967233 the program halts after executing one more instruction
        # (after 28th instruction) that sets the instruction pointer to value outside the program.
        # Before register 0 set to 7967233
        # ('seti', 27, 7, 2) [0, 1, 28, 7967233, 1, 1]
        # ('eqrr', 3, 0, 5) [0, 1, 29, 7967233, 1, 0]
        # ('addr', 5, 2, 2) [0, 1, 30, 7967233, 1, 0]
        # ('seti', 5, 7, 2) [0, 1, 6, 7967233, 1, 0]
        # After register 0 set to 7967233
        # ('seti', 27, 7, 2) [7967233, 1, 28, 7967233, 1, 1]
        # ('eqrr', 3, 0, 5) [7967233, 1, 29, 7967233, 1, 1]
        # ('addr', 5, 2, 2) [7967233, 1, 31, 7967233, 1, 1]
        if result[ip] == 28:
            return result[3]
        opcode = instructions[result[ip]]
        result[opcode[3]] = operations[opcode[0]](result, opcode)
        result[ip] += 1


if __name__ == "__main__":
    with open('day21/input.txt') as inp:
        data = inp.readlines()

    data = [tuple(int(item) if i > 0 else item for i, item in enumerate(inst.strip().split(' ')))
            for inst in data]
    print(execute_program(data[0][1], data[1:]))  # 7967233




