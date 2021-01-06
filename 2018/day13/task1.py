def find_first_crash(grid):
    moves = {
        'u': (-1, 0),
        'd': (1, 0),
        'r': (0, 1),
        'l': (0, -1)
    }
    directions = {
        '^': 'u',
        'v': 'd',
        '>': 'r',
        '<': 'l'
    }
    turns = {
        'r': 'l',
        'l': 's',
        's': 'r'
    }
    changes = 'urdl'

    carts = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] in directions.keys():
                carts.append(((i, j), directions[grid[i][j]], 'r'))

    while True:
        for cart_i, cart in enumerate(carts):
            coord, d, prev = cart
            i = coord[0] + moves[d][0]
            j = coord[1] + moves[d][1]
            if (i, j) in set(c[0] for idx, c in enumerate(carts)):
                return f'{j},{i}'
            index = changes.index(d)
            if grid[i][j] == '\\':
                if d in 'ud':
                    index = index - 1 if index - 1 >= 0 else 3
                else:
                    index = index + 1 if index + 1 <= 3 else 0
            elif grid[i][j] == '/':
                if d in 'ud':
                    index = index + 1 if index + 1 <= 3 else 0
                else:
                    index = index - 1 if index - 1 >= 0 else 3
            elif grid[i][j] == '+':
                prev = turns[prev]
                if prev == 'l':
                    index = index - 1 if index - 1 >= 0 else 3
                elif prev == 'r':
                    index = index + 1 if index + 1 <= 3 else 0
            d = changes[index]
            carts[cart_i] = ((i, j), d, prev)


if __name__ == "__main__":
    with open('day13/input.txt') as inp:
        data = [list(line.strip('\n')) for line in inp]
    max_len = len(max(data, key=len))
    data = [item + [' '] * (max_len - len(item)) for item in data]

    print(find_first_crash(data))  # 43,111

