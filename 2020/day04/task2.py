import re


def count_valid_passports(passports):
    rules = {
        'byr': re.compile(r'19[2-9]\d|200[0-2]'),
        'iyr': re.compile(r'20(?:1\d|20)'),
        'eyr': re.compile(r'20(?:2\d|30)'),
        'ecl': re.compile(r'amb|blu|brn|gr[yn]|hzl|oth'),
        'hgt': re.compile(r'(?:1(?:[5-8]\d|9[0-3]))cm|(?:59|6\d|7[0-6])in'),
        'hcl': re.compile(r'#[\da-f]{6}'),
        'pid': re.compile(r'\d{9}')
    }

    def check_validation(passport):
        for field, rule in rules.items():
            if field not in passport or not re.fullmatch(rule, passport[field]):
                return False
        return True

    return sum([check_validation(passport) for passport in passports])


if __name__ == "__main__":
    with open('day04/input.txt') as inp:
        data = [dict(field.strip().split(':') for field in item.strip().split()) for item in
                inp.read().split('\n\n')]

    print(count_valid_passports(data))  # 137
