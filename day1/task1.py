def count_fuel(ms):
    return sum(int(i) // 3 - 2 for i in ms)


if __name__ == "__main__":
    with open('day1/input.txt') as inp:
        masses = inp.readlines()

    print(count_fuel(masses))  # 3212842
