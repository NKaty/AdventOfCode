import itertools
import math


def form_variations_of_lines(size):
    height, width = size
    limit = height if height > width else width
    variations = ((1, 1),) + tuple(itertools.permutations(range(0, limit), 2))
    return tuple(filter(lambda item: math.gcd(item[0], item[1]) < 2, variations))


def count_visible_asts(ast_map, coords, size, variations, ast='#'):
    visible_asts = set()
    height, width = size
    row, col = coords
    rotating = ((False, True), (True, True), (True, False), (False, False))

    def find_visible_ast(r, c, row_inc, col_inc):
        while 0 <= r < height and 0 <= c < width:
            if (r != coords[0] or c != coords[1]) and ast_map[r][c] == ast:
                return visible_asts.add((r, c))
            r += i if row_inc else -i
            c += j if col_inc else -j

    for i, j in variations:
        for i_inc, j_inc in rotating:
            find_visible_ast(row, col, i_inc, j_inc)

    return len(visible_asts)


def find_best_location(ast_map, ast='#'):
    visible_asts = []
    height = len(ast_map)
    width = len(ast_map[0])
    variations = form_variations_of_lines((height, width))

    for row in range(height):
        for col in range(width):
            if ast_map[row][col] == ast:
                visible_asts.append((row, col, count_visible_asts(ast_map, (row, col), (height, width), variations)))

    return sorted(visible_asts, key=lambda item: item[2], reverse=True)[0]


if __name__ == "__main__":
    with open('day10/input.txt') as inp:
        mp = [line.strip() for line in inp]

    print(find_best_location(mp)[2])  # 309
