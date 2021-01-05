from copy import copy


def simulate_generations(state, changes, generations):
    for _ in range(generations):
        prev = copy(state)
        for i in range(min(prev) - 2, max(prev) + 3):
            sl = ''.join(['#' if j in prev else '.' for j in range(i - 2, i + 3)])
            if sl in changes:
                if changes[sl] == '#':
                    state.add(i)
                else:
                    if i in prev:
                        state.remove(i)
    return sum(state)


if __name__ == "__main__":
    with open('day12/input.txt') as inp:
        data = inp.read().strip().split('\n\n')

    initial_state = set(
        i for i, item in enumerate(data[0].strip().split(' ')[2].strip()) if item == '#')
    changes_map = dict(item.strip().split(' => ') for item in data[1].split('\n'))
    print(simulate_generations(initial_state, changes_map, 20))  # 3903
