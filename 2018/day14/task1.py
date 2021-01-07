def find_score(n):
    recipes = [3, 7]
    elf1 = 0
    elf2 = 1
    while len(recipes) < n + 10:
        new_rec = list(map(int, list(str(recipes[elf1] + recipes[elf2]))))
        recipes += new_rec
        elf1 = (elf1 + recipes[elf1] + 1) % len(recipes)
        elf2 = (elf2 + recipes[elf2] + 1) % len(recipes)

    return ''.join(map(str, recipes[n:]))


if __name__ == "__main__":
    with open('day14/input.txt') as inp:
        length = int(inp.read().strip())

    print(find_score(length))  # 3610281143
