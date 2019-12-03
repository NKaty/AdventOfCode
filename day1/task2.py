def count_fuel(ms):
    all_fuel = 0
    fuel = int(ms)
    while (fuel := fuel // 3 - 2) > 0:
        all_fuel += fuel
    return all_fuel


with open('day1/input.txt') as inp:
    masses = inp.readlines()

print(sum(map(count_fuel, masses)))  # 4816402
