from copy import deepcopy


def is_first_seen_sead_not_occupied(grid, shift, i, j):
    while True:
        i += shift[0]
        j += shift[1]
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 'L':
            return True
        if grid[i][j] == '#':
            return False


def find_occupied_seats(grid):
    current_grid = deepcopy(grid)
    shifts = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))
    while True:
        previous_grid = deepcopy(current_grid)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if previous_grid[i][j] == '.':
                    continue
                empty_seats = sum(
                    is_first_seen_sead_not_occupied(previous_grid, shift, i, j) for shift in shifts)
                if previous_grid[i][j] == 'L' and empty_seats == 8:
                    current_grid[i][j] = '#'
                if previous_grid[i][j] == '#' and empty_seats < 4:
                    current_grid[i][j] = 'L'
        if current_grid == previous_grid:
            return sum(row.count('#') for row in current_grid)


if __name__ == "__main__":
    with open('day11/input.txt') as inp:
        seat_layout = [list(line.strip()) for line in inp]

    print(find_occupied_seats(seat_layout))  # 2180
