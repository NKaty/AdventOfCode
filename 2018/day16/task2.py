import re
from collections import defaultdict

addr = lambda r, o: r[o[1]] + r[o[2]]
addi = lambda r, o: r[o[1]] + o[2]
mulr = lambda r, o: r[o[1]] * r[o[2]]
muli = lambda r, o: r[o[1]] * o[2]
banr = lambda r, o: r[o[1]] & r[o[2]]
bani = lambda r, o: r[o[1]] & o[2]
borr = lambda r, o: r[o[1]] | r[o[2]]
bori = lambda r, o: r[o[1]] | o[2]
setr = lambda r, o: r[o[1]]
seti = lambda r, o: o[1]
gtir = lambda r, o: 1 if o[1] > r[o[2]] else 0
gtri = lambda r, o: 1 if r[o[1]] > o[2] else 0
gtrr = lambda r, o: 1 if r[o[1]] > r[o[2]] else 0
eqir = lambda r, o: 1 if o[1] == r[o[2]] else 0
eqri = lambda r, o: 1 if r[o[1]] == o[2] else 0
eqrr = lambda r, o: 1 if r[o[1]] == r[o[2]] else 0


def execute_test_program(samples, test):
    operations = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr,
                  eqir, eqri, eqrr]
    operations_map = defaultdict(set)
    for start, opcode, result in samples:
        for i, f in enumerate(operations):
            if f(start, opcode) == result[opcode[3]]:
                operations_map[i].add(opcode[0])

    operations_map = list(operations_map.items())
    for i in range(len(operations_map)):
        operations_map = operations_map[:i] + sorted(operations_map[i:], key=lambda x: len(x[1]))
        for j in range(i + 1, len(operations_map)):
            operations_map[j] = operations_map[j][0], operations_map[j][1] - operations_map[i][1]

    operations_map = {item[1].pop(): item[0] for item in operations_map}
    result = [0 for _ in range(4)]
    for opcode in test:
        result[opcode[3]] = operations[operations_map[opcode[0]]](result, opcode)

    return result[0]


if __name__ == "__main__":
    regex = re.compile(r'\d+')
    with open('day16/input.txt') as inp:
        data = inp.read().split('\n\n\n\n')
    instructions = [item.split('\n') for item in data[0].split('\n\n')]
    instructions = [[tuple(map(int, re.findall(regex, item))) for item in i] for i in instructions]
    test_program = [tuple(map(int, re.findall(regex, item))) for item in data[1].split('\n')]

    print(execute_test_program(instructions, test_program))  # 674
