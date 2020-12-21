def find_dangerous_ingredients(ingredients_list):
    allergens = set()
    ingredients = set()
    allergens_map = []

    for item in ingredients_list:
        ingredients |= item[0]
        allergens |= item[1]

    for allergen in allergens:
        current = set()
        for item in ingredients_list:
            if allergen in item[1]:
                current = current | item[0] if not len(current) else current & item[0]
        allergens_map.append((allergen, current))

    for i in range(len(allergens_map)):
        allergens_map = allergens_map[:i] + sorted(allergens_map[i:], key=lambda x: len(x[1]))
        for j in range(i + 1, len(allergens_map)):
            allergens_map[j] = allergens_map[j][0], allergens_map[j][1] - allergens_map[i][1]

    return ','.join([list(item[1])[0] for item in sorted(allergens_map, key=lambda x: x[0])])


if __name__ == "__main__":
    with open('day21/input.txt') as inp:
        ing_list = [line.strip(' \n)').split(' (contains ') for line in inp]

    ing_list = [[set(line[0].split()), set(line[1].split(', '))] for line in ing_list]
    print(find_dangerous_ingredients(ing_list))  # kllgt,jrnqx,ljvx,zxstb,gnbxs,mhtc,hfdxb,hbfnkq
