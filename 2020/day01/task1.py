def find_entries(expenses, aim):
    rests = set()
    for expense in expenses:
        rest = aim - expense
        if rest in rests:
            return expense * rest
        rests.add(expense)


if __name__ == "__main__":
    with open('day01/input.txt') as inp:
        ns = list(map(int, inp.readlines()))

    print(find_entries(ns, 2020))  # 1019571
