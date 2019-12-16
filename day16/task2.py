def apply_fft_algorithm(data, base_pattern, phases):
    offset = int(''.join(map(str, data[:7])))
    if len(data) // offset <= 2:
        output = data[offset:]
        for _ in range(phases):
            new_value = 0
            for i in range(len(output) - 1, -1, -1):
                new_value += output[i] * base_pattern[1]
                output[i] = abs(new_value) % 10
        return ''.join(map(str, output))
    else:
        raise Exception('The calculation will take too long.')


if __name__ == "__main__":
    with open('day16/input.txt') as inp:
        ns = list(map(int, list(inp.read().strip())))

    print(apply_fft_algorithm(ns * 10000, (0, 1, 0, -1), 100)[:8])  # 80722126
