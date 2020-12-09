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


if __name__ == "__main__":
    with open('day09/input.txt') as inp:
        ns = list(map(int, inp.readlines()))

    print(find_not_a_sum(ns))  # 3199139634
