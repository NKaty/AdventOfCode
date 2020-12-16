import re
from collections import Counter


def find_ticket_error_rate(fields, tickets):
    tickets_counter = Counter(sum(tickets, []))
    errors = set.difference(set.union(*(set(t) for t in tickets)), set.union(
        *[set.union(set(range(f[0], f[1] + 1)), set(range(f[2], f[3] + 1))) for f in fields]))
    return sum(err * tickets_counter[err] for err in errors)


if __name__ == "__main__":
    reg = re.compile(r'(\d+)-(\d+) or (\d+)-(\d+)')
    with open('day16/input.txt') as inp:
        data = inp.readlines()

    split_index1 = data.index('\n')
    split_index2 = data.index('\n', split_index1 + 1)
    ticket_fields = [list(map(int, re.findall(reg, field)[0])) for field in data[:split_index1]]
    nearby_tickets = [list(map(int, ticket.strip().split(','))) for ticket in
                      data[split_index2 + 2:]]

    print(find_ticket_error_rate(ticket_fields, nearby_tickets))  # 21978
