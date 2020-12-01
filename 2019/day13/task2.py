from intcode import process_instructions


def start_game(data):
    gen = process_instructions(data, [])
    return [output for output in gen]


def find_paddle_col_pos(grid, tiles):
    for cell in grid:
        if cell[2] == tiles['paddle']:
            return cell[0]
    raise Exception('There is no paddle in the game!!!')


def play_game(data, free_game_mode, tiles):
    game_grid = start_game(data[:])
    paddle_col = find_paddle_col_pos(game_grid, tiles)
    score = 0

    def get_paddle_shift(col_pos):
        if col_pos < paddle_col:
            return -1
        if col_pos > paddle_col:
            return 1
        return 0

    data[0] = free_game_mode
    gen = process_instructions(data[:], [])
    output = next(gen)

    while True:
        try:
            col, row, tile = output
            paddle_shift = None
            if (col, row) == tiles['score']:
                score = tile
            elif tile == tiles['paddle']:
                paddle_col = col
            elif tile == tiles['ball']:
                paddle_shift = get_paddle_shift(col)
                paddle_col += paddle_shift
            output = gen.send(paddle_shift)
        except StopIteration:
            break

    return score


if __name__ == "__main__":
    with open('day13/input.txt') as inp:
        ns = list(map(int, inp.read().strip().split(',')))

    print(play_game(ns, 2, {'empty': 0, 'wall': 1, 'block': 2, 'paddle': 3, 'ball': 4, 'score': (-1, 0)}))  # 12856
