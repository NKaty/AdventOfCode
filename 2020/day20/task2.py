from collections import defaultdict


def rotate(grid):
    rotated_grid = []
    for i in range(len(grid[0])):
        rotated_grid.append(''.join(row[i] for row in grid)[::-1])
    return rotated_grid


def flip(grid):
    return grid[::-1]


def get_possible_borders(grid):
    left = [row[0] for row in grid]
    right = [row[-1] for row in grid]
    return [grid[0], ''.join(grid[0][::-1]), grid[-1], ''.join(grid[-1][::-1]),
            ''.join(left), ''.join(left[::-1]), ''.join(right), ''.join(right[::-1])]


def get_tile_map(borders):
    tiles_map = defaultdict(set)
    for i, (k1, grid1) in enumerate(borders):
        for border1 in grid1:
            for k2, grid2 in borders[i + 1:]:
                for border2 in grid2:
                    if border1 == border2:
                        tiles_map[k1].add(k2)
                        tiles_map[k2].add(k1)
    return tiles_map


def change_orientation(grid):
    current = grid
    for _ in range(2):
        yield current
        for _ in range(3):
            current = rotate(current)
            yield current
        current = flip(current)


def adjust_corner(grid, borders):
    for adjusted_grid in change_orientation(grid):
        count = 0
        left_border = ''.join([row[-1] for row in adjusted_grid])
        top_border = adjusted_grid[-1]
        for adjusted_grid_border in left_border, top_border:
            for _, item in borders:
                for border in item:
                    if adjusted_grid_border == border:
                        count += 1
            if count == 2:
                return adjusted_grid


def find_next_grid(grid, grids, nums, right=True):
    current_border = ''.join([row[-1] for row in grid]) if right else grid[-1]
    for num in nums:
        if num in grids:
            for next_grid in change_orientation(grids[num]):
                next_border = ''.join([row[0] for row in next_grid]) if right else next_grid[0]
                if current_border == next_border:
                    return num, next_grid
    return None


def build_image(image, grids, tile_map):
    x, y = 0, 0
    for i in range(len(grids)):
        current = image[x][y]
        next_grid = find_next_grid(current[1], grids, tile_map[current[0]])
        if next_grid is not None:
            image[-1].append(next_grid)
            y += 1
        else:
            y = 0
            current = image[x][y]
            next_grid = find_next_grid(current[1], grids, tile_map[current[0]], right=False)
            if next_grid is None:
                break
            image.append([next_grid])
            x += 1
        grids.pop(next_grid[0])
    return image


def prepare_image(pieces):
    image = []
    for piece in pieces:
        for i in range(1, len(piece[0][1]) - 1):
            image_row = ''
            for _, item in piece:
                image_row += item[i][1:-1]
            image.append(image_row)
    return image


def get_monster_pattern(monster):
    pattern = []
    for i, string in enumerate(monster):
        for j, char in enumerate(string):
            if char == '#':
                pattern.append((i, j))
    return pattern


def find_monsters(image, monster):
    monster_pattern = get_monster_pattern(monster)
    monster_count = 0
    for grid in change_orientation(image):
        for i in range(len(grid) - len(monster)):
            for j in range(len(grid[0]) - len(monster[0])):
                if all(grid[i + piece[0]][j + piece[1]] == '#' for piece in monster_pattern):
                    monster_count += 1
        if monster_count != 0:
            return len(monster_pattern) * monster_count
    return monster_count


def count_water_roughness(grids, monster):
    borders = [(i, get_possible_borders(grid)) for i, grid in grids.items()]
    tile_map = get_tile_map(borders)
    corner = sorted(tile_map, key=lambda item: len(tile_map.get(item)))[0]
    corner_grid = adjust_corner(grids[corner], list(
        filter(lambda item: item[0] in tile_map[corner], borders)))
    grids.pop(corner)
    image = prepare_image(build_image([[(corner, corner_grid)]], grids, tile_map))
    return sum(row.count('#') for row in image) - find_monsters(image, monster)


if __name__ == "__main__":
    with open('day20/input.txt') as inp:
        tiles = [tile.split('\n') for tile in inp.read().strip().split('\n\n')]

    tiles = {int(tile[0][-5:-1]): [row.strip() for row in tile[1:]] for tile in tiles}
    sea_monster = (
        '                  # ',
        '#    ##    ##    ###',
        ' #  #  #  #  #  #   '
    )
    print(count_water_roughness(tiles, sea_monster))  # 1692
