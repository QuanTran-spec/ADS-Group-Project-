from our_classes import *
from our_functions import *
from recipes import RECIPES


def main():

    print('\n-------------------- Welcome to Shoptimize! --------------------')
    print('\nTo start please tell us which ingridients you would like to\nmake use of. Once finished, simply leave the ingridient field\nblank and press enter to continue.\n')

    raw_input = ingredient_input()
    ingredient_list = clean_input(raw_input)

    bst = binary_search_tree(ingredient_list)

    print('\nThe following recipes are recommended based on your preference:')

    io_traverse(bst.root)

    print('\n--------------- Thank you for using Shoptimize! ---------------\n')


    #selected_recipe = user_choice()

    #shopping_list = missing(ingredient_list, selected_recipe)

    #print(shopping_list)


if __name__ == '__main__':
    main()