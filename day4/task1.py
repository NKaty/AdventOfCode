def check_double_digits(num):
    for i in range(len(num) - 1):
        if num[i] == num[i + 1]:
            return True
    return False


def check_no_decrease(num):
    return ''.join(sorted(num)) == num


def find_passwords(interval):
    all_passwords = []
    for num in range(interval[0], interval[1] + 1):
        num = str(num)
        if check_double_digits(num) and check_no_decrease(num):
            all_passwords.append(num)
    return all_passwords


with open('day4/input.txt') as inp:
    intr = tuple(map(int, inp.read().strip().split('-')))

print(len(find_passwords(intr)))  # 1653
