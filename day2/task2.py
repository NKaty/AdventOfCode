import itertools


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


def find_pair(output):
    variations = list(itertools.product(range(0, 100), repeat=2))
    for noun, verb in variations:
        num = ns[:]
        num[1] = noun
        num[2] = verb
        if process_opcode(num)[0] == output:
            noun = str(noun)
            verb = str(verb)
            return f'{noun if len(noun) > 1 else "0" + noun}{verb if len(verb) > 1 else "0" + verb}'
    return 'Not found'


with open('day2/input.txt') as inp:
    ns = inp.read().strip().split(',')

ns = list(map(int, ns))

print(find_pair(19690720))  # 3376
