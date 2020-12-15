def find_nth_number(numbers, n):
    map_numbers = dict(zip(numbers, range(1, len(numbers) + 1)))
    count = len(numbers)
    last_number = numbers[-1]

    while count != n:
        prev_last_number = last_number
        last_number = 0 if last_number not in map_numbers else count - map_numbers[last_number]
        map_numbers[prev_last_number] = count
        count += 1

    return last_number


if __name__ == "__main__":
    with open('day15/input.txt') as inp:
        ns = list(map(int, inp.read().strip().split(',')))

    print(find_nth_number(ns, 2020))  # 257
