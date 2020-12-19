import re


def find_match_rules(rules, start, messages):
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
    reg = re.compile(traverse(start))
    return sum(bool(re.fullmatch(reg, message)) for message in messages)


if __name__ == "__main__":
    with open('day19/input.txt') as inp:
        data = inp.readlines()

    split_index = data.index('\n')
    check_rules = dict(tuple(map(
        lambda x: [tuple(map(lambda x: x.strip('"'), n.split(' '))) for n in x[1].split(' | ')] if
        x[0] == 1 else x[1], enumerate(item.strip().split(': ')))) for item in data[:split_index])
    received_messages = [message.strip() for message in data[split_index + 1:]]

    print(find_match_rules(check_rules, '0', received_messages))  # 132
