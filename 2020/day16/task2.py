import re
from math import prod


def find_invalid_fields(fields, tickets):
    return set.difference(set.union(*(set(t) for t in tickets)), set.union(
        *[set.union(set(range(f[1][0], f[1][1] + 1)), set(range(f[1][2], f[1][3] + 1))) for f in
          fields]))


def find_departure_fields(fields, tickets, mine):
    invalid_fields = find_invalid_fields(fields, tickets)
    fields_map = [[i for i in range(len(fields))] for _ in range(len(fields))]

    for ticket in tickets:
        if not len(set.intersection(invalid_fields, set(ticket))):
            for i, v in enumerate(ticket):
                for j, f in enumerate(fields):
                    if not (v in range(f[1][0], f[1][1] + 1) or v in range(f[1][2], f[1][3] + 1)):
                        fields_map[i][j] = False

    fields_map = sorted(
        ((i, set(filter(lambda x: x is not False, item))) for i, item in enumerate(fields_map)),
        key=lambda x: len(x[1]))
    match = {fields_map[0][0]: fields[list(fields_map[0][1])[0]][0]}

    for i in range(1, len(fields)):
        match[fields_map[i][0]] = \
            fields[list(set.difference(fields_map[i][1], fields_map[i - 1][1]))[0]][0]

    return prod(mine[i] if name.startswith('departure') else 1 for i, name in match.items())


if __name__ == "__main__":
    reg_rng = re.compile(r'(\d+)-(\d+) or (\d+)-(\d+)')
    reg_name = re.compile(r'^(\D+):')
    with open('day16/input.txt') as inp:
        data = inp.readlines()

    split_index1 = data.index('\n')
    split_index2 = data.index('\n', split_index1 + 1)
    ticket_fields = [
        [re.search(reg_name, field).group(1), list(map(int, re.findall(reg_rng, field)[0]))] for
        field in data[:split_index1]]
    my_ticket = list(map(int, data[split_index1 + 2].strip().split(',')))
    nearby_tickets = [list(map(int, ticket.strip().split(','))) for ticket in
                      data[split_index2 + 2:]]

    print(find_departure_fields(ticket_fields, nearby_tickets, my_ticket))  # 1053686852011
