from our_classes import *
from recipes import RECIPES


def ingredient_input():

    ingredients = []
    ingredients_mentioned = []
    ingredient = input('Ingredient: ')
    
    while ingredient != '':
        
        ingredient = ingredient.lower()
        ingredient = ingredient.strip()

        if ingredient not in ingredients_mentioned:
            ingredients_mentioned.append(ingredient)
            if ingredient.replace(' ', '').isalpha():
                if ingredient == 'show available':
                    print(unique_ingredients(RECIPES))
                    ingredient = input('\nIngredient: ')

                if ingredient in unique_ingredients(RECIPES):
                    ingredients.append(ingredient)
                    ingredient = input('\nIngredient: ')
                else:
                    print("\nSorry, the ingredient you typed is not yet in our database.")
                    ingredient = input('\nIngredient: ')
            else:
                print("\nWe are sorry but your input was invalid, please only type characters.")
                ingredient = input('\nIngredient: ')
        else:
            ingredient = input('\nIngredient: ')

    return ingredients


def calculate_similarity(recipe, ingredient_list):

    score = 0
    total = len(recipe.ingredients)

    for i in ingredient_list:
        if i in recipe.ingredients:
            score += 1

    sim_score = 100*score/total

    return sim_score


def binary_search_tree(ingredient_list):

    bst = BinarySearchTree()

    for recipe in RECIPES:
        recipe.similarity = calculate_similarity(recipe, ingredient_list)
        bst.insert(recipe)

    return bst


def io_traverse(current_node, recommendations):

        if current_node.rightChild:
            io_traverse(current_node.rightChild, recommendations)

        if current_node.similarity > 0:
            recommendations.append(current_node)

        if current_node.leftChild:
            io_traverse(current_node.leftChild, recommendations)


def display_recommendations(recommendations):
    num = 0
    for recipe in recommendations:
        num += 1
        print('\n   ', str(num) + ')', recipe.name, '\n       -', str(round(recipe.similarity)) + '% match \n        -', recipe.yt_link)


def user_choice(recommendations):

    while True:
        try:
            choice = int(input('Please select a receipe by writing its respective number: '))
            
            if 0 < choice <= len(recommendations):
                break

            else:
                print('\nSorry, your selection was out of range.\n')

        except ValueError:
            print('\nPlease only write a number to select a recipe.\n')
    
    return choice


def missing(choice, recommendations, ingredient_list):
    
    missing_ingredients = []

    for i in recommendations[choice-1].ingredients:
        if i not in ingredient_list:
            missing_ingredients.append(i)

    return missing_ingredients


def unique_ingredients(RECIPES):

    all_ingredients = []

    for recipe in RECIPES:
        for ingredient in recipe.ingredients:
            if ingredient not in all_ingredients:
                all_ingredients.append(ingredient)
    
    return all_ingredients




