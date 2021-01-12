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
    result[0] = 1
    results = []

    while not results or results.count(max(results)) < 10:
        opcode = instructions[result[ip]]
        result[opcode[3]] = operations[opcode[0]](result, opcode)
        result[ip] += 1
        results.append(max(result))

    number = max(results)
    return sum(i for i in range(1, number + 1) if number % i == 0)


if __name__ == "__main__":
    with open('day19/input.txt') as inp:
        data = inp.readlines()

    data = [tuple(int(item) if i > 0 else item for i, item in enumerate(inst.strip().split(' ')))
            for inst in data]
    print(execute_program(data[0][1], data[1:]))  # 21340800
