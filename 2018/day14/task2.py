def count_recipes(n):
    recipes = [3, 7]
    elf1 = 0
    elf2 = 1
    n = list(map(int, list(n)))

    while True:
        new_rec = recipes[elf1] + recipes[elf2]
        new_rec = [new_rec] if new_rec < 10 else [1, new_rec % 10]
        recipes += new_rec
        elf1 = (elf1 + recipes[elf1] + 1) % len(recipes)
        elf2 = (elf2 + recipes[elf2] + 1) % len(recipes)
        if recipes[-len(n) - 1:-1] == n:
            return len(recipes) - len(n) - 1
        if recipes[-len(n):] == n:
            return len(recipes) - len(n)


if __name__ == "__main__":
    with open('day14/input.txt') as inp:
        number = inp.read().strip()

    print(count_recipes(number))  # 20211326
