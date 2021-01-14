from copy import deepcopy
from itertools import count


class KilledElf(Exception):
    pass


class Unit:
    def __init__(self, coord, side):
        self.power = 3
        self.hit_points = 200
        self.coord = coord
        self.side = side

    def attack(self, enemy):
        enemy.hit_points = max(enemy.hit_points - self.power, 0)
        if enemy.hit_points == 0 and enemy.side == 0:
            raise KilledElf


class Field:
    def __init__(self, field):
        self.height = len(field)
        self.width = len(field[0])
        self.walls = set()
        self.elves = []
        self.goblins = []
        self.parse_field(field)

    def parse_field(self, field):
        for y in range(len(field)):
            for x in range(len(field[0])):
                if field[y][x] == '#':
                    self.walls.add((y, x))
                if field[y][x] == 'E':
                    self.elves.append(Unit((y, x), 0))
                if field[y][x] == 'G':
                    self.goblins.append(Unit((y, x), 1))

    def shifts(self, coord):
        for shift in (-1, 0), (0, -1), (0, 1), (1, 0):
            y = coord[0] + shift[0]
            x = coord[1] + shift[1]
            if 0 <= y < self.height and 0 <= x < self.width:
                yield y, x

    @staticmethod
    def get_alive(units):
        return [u for u in units if u.hit_points > 0]

    def find_enemies(self, unit):
        return self.get_alive(self.goblins if unit.side == 0 else self.elves)

    def find_enemy_to_attack(self, unit, enemies):
        adjacent_enemies = list(filter(lambda e: e.coord in set(self.shifts(unit.coord)), enemies))
        if not adjacent_enemies:
            return None
        return min(adjacent_enemies, key=lambda e: (e.hit_points, e.coord))

    def move(self, unit, enemies):
        enemies = set(e.coord for e in enemies)
        seen = self.walls | set(u.coord for u in self.get_alive(self.elves + self.goblins))
        paths = [[unit.coord]]
        while paths:
            current_paths = []
            enemy_paths = []
            for path in paths:
                for nb in self.shifts(path[-1]):
                    if nb in enemies:
                        enemy_paths.append(path + [nb])
                    elif nb not in seen:
                        current_paths.append(path + [nb])
                    seen.add(nb)
            if enemy_paths:
                return min(enemy_paths, key=lambda t: (t[-1], t[1]))[1]
            paths = current_paths

    def get_winner(self):
        return sum(u.hit_points for u in self.elves + self.goblins)

    def increase_elf_power(self, power):
        for elf in self.elves:
            elf.power = power


def play_game(field, elf_power):
    field.increase_elf_power(elf_power)
    rounds = 0
    while True:
        for unit in sorted(field.elves + field.goblins, key=lambda u: u.coord):
            if unit.hit_points > 0:
                enemies = field.find_enemies(unit)
                if not enemies:
                    return field.get_winner() * rounds
                enemy = field.find_enemy_to_attack(unit, enemies)
                if not enemy:
                    move_to = field.move(unit, enemies)
                    if not move_to:
                        continue
                    unit.coord = move_to
                    enemy = field.find_enemy_to_attack(unit, enemies)
                if enemy:
                    unit.attack(enemy)
        rounds += 1


def find_elf_power(grid):
    field = Field(grid)
    for elf_power in count(4):
        try:
            return play_game(deepcopy(field), elf_power)
        except KilledElf:
            pass


if __name__ == "__main__":
    with open('day15/input.txt') as inp:
        data = [list(line.strip()) for line in inp]

    print(find_elf_power(data))  # 68324
