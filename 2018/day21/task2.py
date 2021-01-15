# 0: seti 123 0 3 - r[3] = 123
# 1: bani 3 456 3 - r[3] = r[3] & 456 -> 123 & 456 == 72
# 2: eqri 3 72 3 - r[3] == 72 ? 1 : 0 -> r[3]
# 3: addr 3 2 2 - r[2] = r[3] + r[2] -> r[3] == 0 ? go to 4 : go to 5
# 4: seti 0 0 2 - r[2] = 0 -> go to 1
# 5: seti 0 5 3 - r[3] = 0 -> 0 0 6 0 0 0 start
# 6: bori 3 65536 1 - r[1] = r[3] | 65536
# 7: seti 10373714 2 3 - r[3] = 10373714
# 8: bani 1 255 5 - r[5] = r[1] & 255
# 9: addr 3 5 3 - r[3] = r[3] + r[5]
# 10: bani 3 16777215 3 - r[3] = r[3] & 16777215
# 11: muli 3 65899 3 - r[3] = r[3] * 65899
# 12: bani 3 16777215 3 - r[3] = r[3] & 16777215
# 13: gtir 256 1 5 - 256 > r[1] -> r[5]
# 14: addr 5 2 2 - r[2] = r[5] + r[2] -> r[5] == 0 ? go to 15 : go to 16
# 15: addi 2 1 2 - r[2] = r[2] + 1 -> go to 17
# 16: seti 27 7 2 - r[2] = 27 -> go to 28
# 17: seti 0 3 5 - r[5] = 0
# 18: addi 5 1 4 - r[4] = r[5] + 1
# 19: muli 4 256 4 - r[4] = r[4] * 256
# 20: gtrr 4 1 4 - r[4] > r[1] ? 1 : 0 -> r[4]
# 21: addr 4 2 2 - r[2] = r[2] + r[4] -> r[4] == 0 ? go to 22 : go to 23
# 22: addi 2 1 2 - r[2] = r[2] + 1 -> go to 24
# 23: seti 25 4 2 - r[2] = 25 -> go to 26
# 24: addi 5 1 5 - r[5] = r[5] + 1
# 25: seti 17 0 2 - r[2] = 17 -> go to 18
# 26: setr 5 2 1 - r[1] = r[5]
# 27: seti 7 4 2 - r[2] = 7 -> go to 8
# 28: eqrr 3 0 5 - r[3] == r[0] -> r[5]
# 29: addr 5 2 2 - r[2] = r[5] + r[2] -> r[5] == 0 ? go to 30 : go to 31
# 30: seti 5 7 2 - r[2] = 5 -> go to 6

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
    r3_all = []
    r3 = 0

    while result[ip] < len(instructions):
        if r3 in r3_all:
            return r3_all[-1]
        r3_all.append(r3)
        r1 = r3 | 65536
        r3 = 10373714
        while True:
            r3 += r1 & 255
            r3 &= 16777215
            r3 *= 65899
            r3 &= 16777215
            if r1 < 256:
                break
            r1 //= 256


if __name__ == "__main__":
    with open('day21/input.txt') as inp:
        data = inp.readlines()

    data = [tuple(int(item) if i > 0 else item for i, item in enumerate(inst.strip().split(' ')))
            for inst in data]
    print(execute_program(data[0][1], data[1:]))  # 16477902




