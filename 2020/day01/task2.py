def find_entries(expenses, aim):
    expenses_length = len(expenses)
    for i in range(expenses_length):
        rests = set()
        rest1 = aim - expenses[i]
        for j in range(i + 1, expenses_length):
            rest2 = rest1 - expenses[j]
            if rest2 in rests:
                return expenses[i] * expenses[j] * rest2
            rests.add(expenses[j])


if __name__ == "__main__":
    with open('day01/input.txt') as inp:
        ns = list(map(int, inp.readlines()))

    print(find_entries(ns, 2020))  # 100655544
