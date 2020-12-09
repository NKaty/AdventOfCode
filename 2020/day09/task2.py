def is_number_a_sum(numbers, to_check):
    rests = set()
    for number in numbers:
        rest = to_check - number
        if rest in rests:
            return True
        rests.add(number)
    return False


def find_not_a_sum(numbers):
    for i in range(26, len(numbers)):
        current_numbers = numbers[i - 26:i]
        if not is_number_a_sum(current_numbers, numbers[i]):
            return numbers[i]


def find_encryption_weakness(numbers):
    weak_number = find_not_a_sum(numbers)
    weak_sum = 0
    start = 0
    end = 0
    while end < len(numbers):
        weak_sum += numbers[end]
        end += 1
        while weak_sum > weak_number:
            weak_sum -= numbers[start]
            start += 1
        if weak_sum == weak_number and start != end - 1:
            weak_range = sorted(numbers[start:end])
            return weak_range[0] + weak_range[len(weak_range) - 1]


if __name__ == "__main__":
    with open('day09/input.txt') as inp:
        ns = list(map(int, inp.readlines()))

    print(find_encryption_weakness(ns))  # 438559930
