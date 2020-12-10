from functools import lru_cache


def get_chain(adapters):
    sorted_adapters = sorted(adapters)
    return [0] + sorted_adapters + [sorted_adapters[-1] + 3]


def count_diff_ways(adapters):
    chain = get_chain(adapters)
    chain_len = len(chain)

    @lru_cache
    def traverse(index):
        if index + 1 == chain_len:
            return 1
        return sum(traverse(index + i) if chain_len > index + i and chain[index + i] - chain[
            index] < 4 else 0 for i in range(1, 4))

    return traverse(0)


if __name__ == "__main__":
    with open('day10/input.txt') as inp:
        ns = list(map(int, inp.readlines()))

    print(count_diff_ways(ns))  # 4049565169664
