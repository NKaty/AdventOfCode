def play_game(cups, moves):
    current = 0
    length = len(cups)
    for _ in range(moves):
        if current < length - 3:
            removed = cups[current + 1:current + 4]
            cups = cups[:current + 1] + cups[current + 4:]
        else:
            left = 3 - len(cups[current + 1:])
            removed = cups[current + 1:] + cups[:left]
            cups = cups[left: current + 1]
            current -= left

        sorted_cups = sorted(cups, reverse=True)
        index = sorted_cups.index(cups[current])
        destination_index = cups.index(max(cups)) if index == len(sorted_cups) - 1 else cups.index(
            sorted_cups[index + 1])
        cups = cups[:destination_index + 1] + removed + cups[destination_index + 1:]
        current = (current + (1 if current < destination_index else 4)) % length

    index1 = cups.index(1)
    return ''.join(str(item) for item in cups[index1 + 1:] + cups[:index1])


if __name__ == "__main__":
    with open('day23/input.txt') as inp:
        crab_cups = list(map(int, list(inp.read().strip())))

    print(play_game(crab_cups, 100))  # 69852437
