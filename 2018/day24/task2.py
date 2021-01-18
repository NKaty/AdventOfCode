import re
from copy import deepcopy


class Group:
    def __init__(self, units, hit, weak, immune, damage, damage_type, initiative, side):
        self.units = units
        self.hit = hit
        self.weak = weak
        self.immune = immune
        self.damage = damage
        self.damage_type = damage_type
        self.initiative = initiative
        self.side = side
        self.target = None

    def effective_power(self):
        return self.units * self.damage

    def select_target(self, enemies):
        if not enemies:
            self.target = None
            return
        enemies.sort(key=lambda e: (e.count_damage(self), e.effective_power(), e.initiative))
        self.target = enemies.pop() if enemies[-1].count_damage(self) > 0 else None

    def count_damage(self, enemy):
        if enemy.damage_type in self.immune:
            return 0
        if enemy.damage_type in self.weak:
            return enemy.effective_power() * 2
        return enemy.effective_power()


def get_groups(sides):
    groups = []
    for i, side in enumerate(sides):
        for unit in side:
            weak, immune = [], []
            if unit[2]:
                wi = unit[2].strip('() ')
                wi = wi.split('; ') if '; ' in wi else [wi]
                for item in wi:
                    if item.startswith('weak'):
                        weak = item[8:].split(', ')
                    else:
                        immune = item[10:].split(', ')
            groups.append(Group(int(unit[0]), int(unit[1]), weak, immune, int(unit[3]), unit[4],
                                int(unit[5]), i))
    return groups


def fight(groups):
    while True:
        groups = list(filter(lambda g: g.units > 0, groups))
        system = list(filter(lambda g: g.side == 0, groups))
        infection = list(filter(lambda g: g.side == 1, groups))

        if not system:
            return 1, sum(group.units for group in infection)
        if not infection:
            return 0, sum(group.units for group in system)

        for group in sorted(groups, key=lambda g: (g.effective_power(), g.initiative),
                            reverse=True):
            group.select_target(system if group.side == 1 else infection)

        lost = 0
        for group in sorted(groups, key=lambda g: g.initiative, reverse=True):
            if group.target and group.units > 0:
                damage = group.target.count_damage(group) // group.target.hit
                lost += damage
                group.target.units = max(group.target.units - damage, 0)

        if not lost:
            return 1, sum(group.units for group in infection)


def add_boost(groups, boost):
    for group in groups:
        if group.side == 0:
            group.damage += boost
    return groups


def find_boost(sides):
    groups = get_groups(sides)
    min_b, max_b = 0, 10
    while True:
        winner, _ = fight(add_boost(deepcopy(groups), max_b))
        if winner == 0:
            break
        max_b *= max_b

    while True:
        boost = (min_b + max_b) // 2
        winner, units = fight(add_boost(deepcopy(groups), boost))
        if min_b == max_b:
            return units
        if winner == 1:
            min_b = boost + 1
        else:
            max_b = boost - 1


if __name__ == "__main__":
    reg = re.compile(
        r'(\d+) units each with (\d+) hit points (\([^)]*\) )?with an attack that does (\d+)' +
        r' (\w+) damage at initiative (\d+)')
    with open('day24/input.txt') as inp:
        data = [[re.match(reg, item).groups() for item in fighter.strip().split('\n')[1:]] for
                fighter in inp.read().strip().split('\n\n')]

    print(find_boost(data))  # 3045
