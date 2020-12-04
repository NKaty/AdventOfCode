def count_valid_passports(passports):
    return sum([len(passport) == 8 or (len(passport) == 7 and 'cid' not in passport) for passport in
                passports])


if __name__ == "__main__":
    with open('day04/input.txt') as inp:
        data = [dict(field.strip().split(':') for field in item.strip().split()) for item in
                inp.read().split('\n\n')]

    print(count_valid_passports(data))  # 202
