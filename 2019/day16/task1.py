def get_pattern(base_pattern, index, length):
    pattern = []
    while True:
        for item in base_pattern:
            if index < length - len(pattern) + 1:
                pattern += [item] * index
            else:
                return (pattern + [item] * (length - len(pattern) + 1))[1:]


def apply_fft_algorithm(data, base_pattern, phases):
    output = data[:]
    length = len(output)
    for _ in range(phases):
        for i in range(length):
            pattern = get_pattern(base_pattern, i + 1, length)
            new_value = 0
            for item, patt in zip(output, pattern):
                new_value += item * patt
            output[i] = abs(new_value) % 10
    return ''.join(map(str, output))


if __name__ == "__main__":
    with open('day16/input.txt') as inp:
        ns = list(map(int, list(inp.read().strip())))

    print(apply_fft_algorithm(ns, (0, 1, 0, -1), 100)[:8])  # 10189359
