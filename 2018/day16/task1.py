import re

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


def check_samples(samples):
    operations = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr,
                  eqir, eqri, eqrr]
    count = 0
    for start, opcode, result in samples:
        if sum(f(start, opcode) == result[opcode[3]] for f in operations) > 2:
            count += 1
    return count


if __name__ == "__main__":
    regex = re.compile(r'\d+')
    with open('day16/input.txt') as inp:
        instructions = [item.split('\n') for item in inp.read().split('\n\n\n\n')[0].split('\n\n')]

    instructions = [[tuple(map(int, re.findall(regex, item))) for item in i] for i in instructions]
    print(check_samples(instructions))  # 636
