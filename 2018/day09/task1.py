from collections import deque


def play_game(players, last_points):
    circle = deque([0])
    scores = [0] * players
    for i in range(1, last_points + 1):
        if i % 23 != 0:
            circle.rotate(-1)
            circle.append(i)
        else:
            circle.rotate(7)
            scores[i % players] += i + circle.pop()
            circle.rotate(-1)
    return max(scores)


if __name__ == "__main__":
    with open('day09/input.txt') as inp:
        game_data = tuple(int(item) for i, item in enumerate(inp.read().split(' ')) if i in (0, 6))

    print(play_game(*game_data))  # 398371
