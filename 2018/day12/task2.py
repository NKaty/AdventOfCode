from copy import copy


def simulate_generation(state, changes):
    prev = copy(state)
    for i in range(min(prev) - 2, max(prev) + 3):
        sl = ''.join(['#' if j in prev else '.' for j in range(i - 2, i + 3)])
        if sl in changes:
            if changes[sl] == '#':
                state.add(i)
            else:
                if i in prev:
                    state.remove(i)
    return state


def simulate_generations(state, changes, generations):
    state_sum = sum(state)
    states_diff = [state_sum]
    for i in range(generations):
        state = simulate_generation(state, changes)
        current_sum = sum(state)
        diff = current_sum - state_sum
        state_sum = current_sum
        if len(state) > 2 and all(item == diff for item in states_diff[-3:]):
            return state_sum + diff * (generations - i - 1)
        states_diff.append(diff)
    return state_sum


if __name__ == "__main__":
    with open('day12/input.txt') as inp:
        data = inp.read().strip().split('\n\n')

    initial_state = set(
        i for i, item in enumerate(data[0].strip().split(' ')[2].strip()) if item == '#')
    changes_map = dict(item.strip().split(' => ') for item in data[1].split('\n'))
    print(simulate_generations(initial_state, changes_map, 50000000000))  # 3450000002268
