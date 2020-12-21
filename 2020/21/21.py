def parse(file):
    ingredient_lists = []
    all_allergens = set()
    all_ingredients = set()
    with open(file) as f:
        for line in f.readlines():
            line = line.strip().replace(')', '')
            ingredients, allergens = line.split(' (contains ')

            ingredients = set(ingredients.split())
            allergens = set(allergens.split(', '))

            all_allergens |= allergens
            all_ingredients |= ingredients
            ingredient_lists.append((ingredients, allergens))

        return all_allergens, all_ingredients, ingredient_lists

def find(all_allergens, all_ingredients, ingredient_lists):
    for allergen in list(all_allergens):
        possible = all_ingredients
        for ingredients, allergens in ingredient_lists:
            if allergen in allergens:
                possible = possible & ingredients
        if len(possible) == 1:
            return allergen, possible.pop()

def map_ingredients(all_allergens, all_ingredients, ingredient_lists):
    all_allergens = set() | all_allergens
    all_ingredients = set() | all_ingredients
    allergen_map = {}
    while all_allergens:
        allergen, ingredient = find(
            all_allergens,
            all_ingredients,
            ingredient_lists
        )
        allergen_map[allergen] = ingredient
        all_allergens.remove(allergen)
        all_ingredients.remove(ingredient)
        
        updated_lists = []
        for ingredients, alls in ingredient_lists:
            ingredients.discard(ingredient)
            alls.discard(allergen)
            updated_lists.append((ingredients, alls))
        ingredient_lists = updated_lists
    return allergen_map

def count(ingredient, ingredient_lists):
    count = 0
    for ingredients, _ in ingredient_lists:
        if ingredient in ingredients:
            count += 1
    return count

all_allergens, all_ingredients, ingredient_lists = parse('input.txt')
allergen_map = map_ingredients(
    all_allergens,
    all_ingredients,
    ingredient_lists
)

non_allergens = set() | all_ingredients
for all, ingredient in allergen_map.items():
    non_allergens.discard(ingredient)

non_allergen_ingredient_count = 0
for ingredient in non_allergens:
    non_allergen_ingredient_count += count(ingredient, ingredient_lists)

sorted_allergen_map = sorted([
    (allergen, ingredient)
    for allergen, ingredient in allergen_map.items()
])
allergen_ingredients = ','.join(
    ingredient for _, ingredient in sorted_allergen_map
)

print('Part 1:', non_allergen_ingredient_count)
print('Part 2:', allergen_ingredients)
