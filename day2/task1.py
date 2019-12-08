def process_opcode(numbers):
    for i in range(0, len(numbers), 4):
        if numbers[i] == 1:
            numbers[numbers[i + 3]] = numbers[numbers[i + 1]] + numbers[numbers[i + 2]]
        elif numbers[i] == 2:
            numbers[numbers[i + 3]] = numbers[numbers[i + 1]] * numbers[numbers[i + 2]]
        elif numbers[i] == 99:
            return numbers
        else:
            raise Exception('Wrong opcode.')


if __name__ == "__main__":
    with open('day2/input.txt') as inp:
        ns = inp.read().strip().split(',')

    ns = list(map(int, ns))
    ns[1] = 12
    ns[2] = 2

    print(process_opcode(ns)[0])  # 7594646
