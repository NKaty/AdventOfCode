import re
from collections import defaultdict, Counter
from itertools import chain


def find_guard(records):
    asleep = defaultdict(list)
    guard = None
    start = None
    guard_reg = re.compile(r'(\d+)')
    for record in records:
        if record[1].startswith('Guard'):
            guard = re.search(guard_reg, record[1]).group()
        elif record[1].startswith('falls'):
            start = int(record[0])
        else:
            asleep[guard].append((start, int(record[0])))

    most_asleep = max(
        [(guard[0], sum(item[1] - item[0] for item in guard[1])) for guard in asleep.items()],
        key=lambda x: x[1])[0]
    most_min = Counter(chain(*list(list(range(item[0], item[1])) for item in asleep[most_asleep])))

    return int(most_asleep) * most_min.most_common(1)[0][0]


if __name__ == "__main__":
    reg = re.compile(r'^\[\d+\-\d+\-\d+ \d+:(\d+)\] (.+)$')
    with open('day04/input.txt') as inp:
        repose_records = [re.match(reg, record.strip()).groups() for record in
                          sorted(inp.readlines())]

    print(find_guard(repose_records))  # 85296
