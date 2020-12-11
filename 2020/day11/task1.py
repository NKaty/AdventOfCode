from copy import deepcopy


def find_occupied_seats(grid):
    current_grid = deepcopy(grid)
    rows = len(grid)
    columns = len(grid[0])
    shifts = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))
    while True:
        previous_grid = deepcopy(current_grid)
        for i in range(rows):
            for j in range(columns):
                if previous_grid[i][j] == '.':
                    continue
                empty_seats = sum(
                    1 if i + shift[0] < 0 or i + shift[0] >= rows or j + shift[1] < 0 or j + shift[
                        1] >= columns or previous_grid[i + shift[0]][j + shift[1]] in (
                         'L', '.') else 0 for shift in shifts)
                if previous_grid[i][j] == 'L' and empty_seats == 8:
                    current_grid[i][j] = '#'
                if previous_grid[i][j] == '#' and empty_seats < 5:
                    current_grid[i][j] = 'L'
        if current_grid == previous_grid:
            return sum(row.count('#') for row in current_grid)


if __name__ == "__main__":
    with open('day11/input.txt') as inp:
        seat_layout = [list(line.strip()) for line in inp]

    print(find_occupied_seats(seat_layout))  # 2489
