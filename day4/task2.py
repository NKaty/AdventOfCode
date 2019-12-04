def check_double_digits(num):
    return 2 in [num.count(digit) for digit in num]


def check_no_decrease(num):
    return ''.join(sorted(num)) == num


def find_passwords(interval):
    all_passwords = []
    for num in range(interval[0], interval[1] + 1):
        num = str(num)
        if check_no_decrease(num) and check_double_digits(num):
            all_passwords.append(num)
    return all_passwords


with open('day4/input.txt') as inp:
    intr = tuple(map(int, inp.read().strip().split('-')))

print(len(find_passwords(intr)))  # 1133
