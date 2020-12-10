def get_chain(adapters):
    sorted_adapters = sorted(adapters)
    return [0] + sorted_adapters + [sorted_adapters[-1] + 3]


def find_differences(adapters):
    chain = get_chain(adapters)
    jolt_1 = 0
    jolt_3 = 0
    for i in range(len(chain) - 1):
        diff = chain[i + 1] - chain[i]
        if diff == 1:
            jolt_1 += 1
        elif diff == 3:
            jolt_3 += 1
    return jolt_1 * jolt_3


if __name__ == "__main__":
    with open('day10/input.txt') as inp:
        ns = list(map(int, inp.readlines()))

    print(find_differences(ns))  # 1755
