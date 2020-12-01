import itertools
import math


def form_variations_of_lines(size):
    height, width = size
    limit = height if height > width else width
    variations = tuple(itertools.product((-1, 1), repeat=2)) + \
                 tuple(itertools.permutations(range(-limit + 1, limit), 2))
    variations = tuple(filter(lambda item: math.gcd(item[0], item[1]) < 2, variations))
    return sorted(list(set(variations)), key=lambda item: math.atan2(item[1], item[0]), reverse=True)


def find_visible_ast(ast_map, row, col, i, j, size, ast='#', empty='.', vap=False):
    height, width = size
    while 0 <= row < height and 0 <= col < width:
        if ast_map[row][col] == ast:
            if vap:
                ast_map[row][col] = empty
            return row, col
        row += i
        col += j
    return None


def complete_vaporization(ast_map, coords, num_to_vap, ast='#', empty='.'):
    height = len(ast_map)
    width = len(ast_map[0])
    row, col = coords
    vaporized = 0
    variations = form_variations_of_lines((height, width))

    while True:
        start_vaporized = vaporized
        for i, j in variations:
            ast_coords = find_visible_ast(ast_map, row + i, col + j, i, j, (height, width), ast, empty, vap=True)
            if ast_coords is not None:
                vaporized += 1
                if vaporized == num_to_vap:
                    return ast_coords
        if not start_vaporized - vaporized:
            #  There are less asteroids than the provided number of asteroids to vaporize
            return None


def count_visible_asts(ast_map, coords, size, variations, ast='#'):
    visible_asts = set()
    height, width = size
    row, col = coords

    for i, j in variations:
        ast_coords = find_visible_ast(ast_map, row + i, col + j, i, j, (height, width), ast)
        if ast_coords is not None:
            visible_asts.add(ast_coords)

    return len(visible_asts)


def find_best_location(ast_map, ast='#'):
    visible_asts = []
    height = len(ast_map)
    width = len(ast_map[0])
    variations = form_variations_of_lines((height, width))

    for row in range(height):
        for col in range(width):
            if ast_map[row][col] == ast:
                visible_asts.append(((row, col), count_visible_asts(ast_map, (row, col), (height, width), variations)))

    return sorted(visible_asts, key=lambda item: item[1], reverse=True)[0]


if __name__ == "__main__":
    with open('day10/input.txt') as inp:
        mp = [list(line.strip()) for line in inp]

    best_ast_coords = find_best_location(mp)[0]
    print(best_ast_coords)  # (25, 37)
    ast_200th = complete_vaporization(mp, best_ast_coords, 200)
    print(ast_200th)  # (16, 4)
    print(ast_200th[1] * 100 + ast_200th[0])  # 416
