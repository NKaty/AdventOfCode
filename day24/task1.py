import copy


def calculate_biodiversity_rating_of_repeating_layout(grid):
    height = len(grid)
    width = len(grid[0])
    shifts = ((0, 1), (0, -1), (1, 0), (-1, 0))
    biodiversity_ratings = []

    while True:
        biodiversity_rating = 0
        new_grid = copy.deepcopy(grid)

        for row in range(height):
            for col in range(width):
                bugs = 0
                for r_sh, c_sh in shifts:
                    if 0 <= row + r_sh < height and 0 <= col + c_sh < width and grid[row + r_sh][col + c_sh] == '#':
                        bugs += 1
                if grid[row][col] == '#' and bugs != 1:
                    new_grid[row][col] = '.'
                if grid[row][col] == '.' and bugs in (1, 2):
                    new_grid[row][col] = '#'
                if new_grid[row][col] == '#':
                    biodiversity_rating += 2 ** (row * width + col)

        if biodiversity_rating in biodiversity_ratings:
            return biodiversity_rating

        grid = copy.deepcopy(new_grid)
        biodiversity_ratings.append(biodiversity_rating)


if __name__ == "__main__":
    with open('day24/input.txt') as inp:
        eris = [list(line.strip()) for line in inp]

    print(calculate_biodiversity_rating_of_repeating_layout(eris))  # 17863711
