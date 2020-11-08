from our_classes import *
from recipes import RECIPES


def ingredient_input():

    ingredients = []
    ingredient = input('Ingredient (enter to confirm): ')
    
    while ingredient != '':
        
        if ingredient.replace(' ', '').isalpha():
            ingredients.append(ingredient)
            ingredient = input('\nIngredient (enter to confirm): ')
        else:
            print("\nWe are sorry but your input was invalid, please only type characters.")
            ingredient = input('\nIngredient (enter to confirm): ')

    return ingredients


def clean_input(ingredient_list):

    ing_lower = [x.lower() for x in ingredient_list]
    ing_lower_ws = [x.strip() for x in ing_lower]

    return ing_lower_ws


def calculate_similarity(recipe, ingridient_list):

    score = 0
    total = len(recipe.ingridients)

    for i in ingridient_list:
        if i in recipe.ingridients:
            score += 1

    sim_score = 100*score/total

    return sim_score


def binary_search_tree(ingredient_list):

    bst = BinarySearchTree()

    for recipe in RECIPES:
        recipe.similarity = calculate_similarity(recipe, ingredient_list)
        bst.insert(recipe)

    return bst


def io_traverse(current_node):

        if current_node.rightChild:
            io_traverse(current_node.rightChild)

        if current_node.similarity > 0:
            print('\n   ', current_node.name, '\n       -', current_node.similarity, '% match \n        -', current_node.yt_link)   

        if current_node.leftChild:
            io_traverse(current_node.leftChild)


def user_choice():

    return None


def missing():
    
    return None