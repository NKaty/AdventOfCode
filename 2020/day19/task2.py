import re


def find_match_rules(rules, messages):
    def traverse(n):
        pattern = ''
        if n not in rules:
            pattern += n
        else:
            for i in range(len(rules[n])):
                if i != 0:
                    pattern += '|'
                for j in range(len(rules[n][i])):
                    pattern += traverse(rules[n][i][j])
        return rf'(?:{pattern})'

    p42 = traverse('42')
    p31 = traverse('31')
    max_len = len(max(messages, key=len))
    # 42 | 42 8 - 42 pattern is repeating + times
    # 42 31 | 42 11 31 - 42 42 42 ... 31 31 31 pattern
    # max_len // 2 - the worst case
    reg = re.compile(
        rf"(?:{p42})+(?:{'|'.join(rf'(?:{p42}){{{n}}}(?:{p31}){{{n}}}' for n in range(1, max_len // 2))})")
    return sum(bool(re.fullmatch(reg, message)) for message in messages)


if __name__ == "__main__":
    with open('day19/input.txt') as inp:
        data = inp.readlines()

    split_index = data.index('\n')
    check_rules = dict(tuple(map(
        lambda x: [tuple(map(lambda x: x.strip('"'), n.split(' '))) for n in x[1].split(' | ')] if
        x[0] == 1 else x[1], enumerate(item.strip().split(': ')))) for item in data[:split_index])
    check_rules['8'] = [('42',), ('42', '8')]
    check_rules['11'] = [('42', '31'), ('42', '11', '31')]
    received_messages = [message.strip() for message in data[split_index + 1:]]

    print(find_match_rules(check_rules, received_messages))  # 306
