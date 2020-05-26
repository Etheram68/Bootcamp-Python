# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: frfrey <frfrey@student.42lyon.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/05/26 08:37:34 by frfrey            #+#    #+#              #
#    Updated: 2020/05/26 13:45:23 by frfrey           ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

def nothing():
    print("\033[1;31m", end="")
    print("This option does not exist, please type the corresponding number.")
    print("To exit, enter 5.\033[0m\n")
    input("\033[1;32mPress any touch for return menu\033[0m")
    print()


def print_cook(book):
    print("\033[4m\033[33mYou have", len(book), "recipes on cookbook:\033[0m")
    print()
    for i in book:
        print("-", i)
    print()
    input("\033[1;32mPress any touch for return menu\033[0m")
    print()


def print_recipe(book):
    recipe = input("Please enter the recipe's name to get its details:\n>> ")
    print()
    if (recipe in book):
        print("\033[4m\033[33mRecipe for", recipe, ":\033[0m\n")
        print("\033[32mIngredients list:\033[0m ", book[recipe]['ingredients'])
        print("\033[32mTo be eaten for\033[0m", book[recipe]['meal'])
        print(
            "\033[32mTakes\033[0m",
            book[recipe]['prep_time'],
            "\033[32mminutes of cooking.\033[0m")
        print()
    else:
        print("\033[1;31mRecipe does not existe\033[0m")
    input("\033[1;32mPress any touch for return menu\033[0m")
    print()


def del_recipe(book):
    delete = input("Please enter the recipe name to delete\n>> ")
    print()
    if (delete in book):
        del book[delete]
        print("\033[1;32mThe recipe", delete, "as been deleted\033[0m")
    else:
        print("\033[1;31mRecipe does not existe\033[0m")
    print()
    input("\033[1;32mPress any touch for return menu\033[0m")
    print()


def add_recipe(book):
    print("\033[32m", end="")
    new = input("Please enter the recipe name to adding on book:\033[0m\n>> ")
    print()
    if (new not in book):
        book[new] = {}
        book[new]['ingredients'] = []
        compo = ""
        print("\033[32m", end="")
        print("Enter the ingredients of the recipe press 'exit' for quit")
        print("\033[0m", end="")
        while (compo != "exit"):
            compo = input(">> ")
            if (compo not in book[new]['ingredients'] and compo != "exit"):
                book[new]['ingredients'].append(compo)
            elif (compo != "exit" and compo in book[new]['ingredients']):
                print("\033[1;31mIngredients exist to the list\033[0m")
                print()
        print()
        book[new]['meal'] = input(
            "\033[32mEnter when to be eaten this recipe\033[0m\n>> ")
        book[new]['prep_time'] = input(
            "\033[32mEnter time of cooking in minutes\033[0m\n>> ")
    else:
        print("\033[1;31mRecipe existe\033[0m")
        input("\033[1;32mPress any touch for return menu\033[0m")
    print()


def ft_quit(book):
    print("\033[1;32mCookbook closed.\033[0m")
    exit(0)


def switch_case_menu(menu, cookbook):
    switcher = {
        0: add_recipe,
        1: del_recipe,
        2: print_recipe,
        3: print_cook,
        4: ft_quit
    }
    func = switcher.get(menu, nothing)
    return func(cookbook)


def main():
    cookbook = {
        'sandwich':
            {'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
             'meal': 'fast food',
             'prep_time': 10},
        'cake':
            {'ingredients': ['flour', 'sugar', 'egg'],
             'meal': 'dessert',
             'prep_time': 60},
        'salad':
            {'ingredients': ['avocado', 'arygula', 'tomatoes', 'spinach'],
             'meal': 'starter',
             'prep_time': 15}
    }
    while (True):
        print("Please select an option by typing the corresponding number:\n")
        print("1:\033[1;36m Add a recipe\033[0m")
        print("2:\033[1;36m Delete a recipe\033[0m")
        print("3:\033[1;36m Print a recipe\033[0m")
        print("4:\033[1;36m Print the cookbook\033[0m")
        print("5:\033[1;36m Quit\033[0m")
        menu = input("\n>> ")
        print("\n")
        if (menu.isnumeric() is False):
            nothing()
        else:
            switch_case_menu(int(menu) - 1, cookbook)


if __name__ == "__main__":
    main()
