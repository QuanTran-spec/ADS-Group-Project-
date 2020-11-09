from our_classes import *
from our_functions import *
from recipes import RECIPES


def main():

    print('\n-------------------- Welcome to Shoptimize! --------------------')
    print('\nTo start please tell us which ingredients you would like to\n\
make use of. Once finished, simply leave the ingredient field\n\
blank and press enter to continue. If you would like to see a\n\
list of available ingredients write "show available".\n')

    ingredient_list = ingredient_input()
    
    if ingredient_list:

        bst = binary_search_tree(ingredient_list)

        print('\nThe following recipes are recommended based on your preference:')

        recommendations = []
        io_traverse(bst.root, recommendations)
        display_recommendations(recommendations)

        print()

        selected_recipe = user_choice(recommendations)

        shopping_list = missing(selected_recipe, recommendations, ingredient_list)

        print('\nHere is a list of the ingredients you are still missing:\n')

        for i in range(len(shopping_list)):
            print(' -', shopping_list[i].capitalize())
    
    print('\n---------------- Thank you for using Shoptimize! ----------------\n')


if __name__ == '__main__':
    main()