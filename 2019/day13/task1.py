from intcode import process_instructions


def get_game_grid(data):
    gen = process_instructions(data, [])
    return [output for output in gen]


def count_block_tiles(grid, tiles):
    block_tiles = set()
    for cell in grid:
        if cell[2] == tiles['block']:
            block_tiles.add(tuple(cell))
    return len(block_tiles)


if __name__ == "__main__":
    with open('day13/input.txt') as inp:
        ns = list(map(int, inp.read().strip().split(',')))

    game_grid = process_instructions(ns, [])
    print(count_block_tiles(game_grid, {'empty': 0, 'wall': 1, 'block': 2, 'paddle': 3, 'ball': 4}))  # 277
