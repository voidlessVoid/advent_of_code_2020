import os
from functools import reduce
import operator
CURRENT_DIRECTORY = os.path.dirname(__file__)
os.chdir(CURRENT_DIRECTORY)

def read_input_lines():
    with open('input.txt', 'r') as fh:
        return [x.strip() for x in fh.readlines()]

def read_input_text():
    with open('input.txt', 'r') as fh:
        return fh.read().strip()


def part_a():
    ingredientStatements = read_input_lines()
    allIngredientset = set()
    allIngredientlist = []
    allergenToPotentialIngredients = {}

    for ingredientStatement in ingredientStatements:
        ingredients, allergens = ingredientStatement.split("(")
        ingredients = ingredients.split()
        allergens = set(allergens[:-1].replace(",", " ").split()) - {"contains"}
        allIngredientset |= set(ingredients)
        allIngredientlist += ingredients
        for allergen in allergens:
            if allergen in allergenToPotentialIngredients:
                allergenToPotentialIngredients[allergen] &= set(ingredients)
            else:
                allergenToPotentialIngredients[allergen] = set(ingredients)

    safeIngredients = allIngredientset - reduce(operator.__or__, allergenToPotentialIngredients.values())
    print(len([x for x in allIngredientlist if x in safeIngredients]))
    return allergenToPotentialIngredients


def part_b():
    allergenToPotentialIngredients = part_a()
    nSolve = len(allergenToPotentialIngredients)
    solved = {}

    while len(solved) != nSolve:
        for k,v in list(allergenToPotentialIngredients.items()):
            remaining_options = v - set(solved.keys())
            if  len(remaining_options) ==1:
                solved[remaining_options.pop()] = k
                del allergenToPotentialIngredients[k]

    print(",".join(sorted(solved.keys(), key = lambda x: solved[x])))

part_b()