def find_ingredients_without_allergens(ingredients_list):
    allergens = set()
    ingredients = set()

    for item in ingredients_list:
        ingredients |= item[0]
        allergens |= item[1]

    for allergen in allergens:
        current = set()
        for item in ingredients_list:
            if allergen in item[1]:
                current = current | item[0] if not len(current) else current & item[0]
        ingredients -= current

    return sum(len(item[0] & ingredients) for item in ingredients_list)


if __name__ == "__main__":
    with open('day21/input.txt') as inp:
        ing_list = [line.strip(' \n)').split(' (contains ') for line in inp]

    ing_list = [[set(line[0].split()), set(line[1].split(', '))] for line in ing_list]
    print(find_ingredients_without_allergens(ing_list))  # 1815
