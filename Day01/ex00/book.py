# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    book.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: frfrey <frfrey@student.42lyon.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/05/27 09:05:01 by frfrey            #+#    #+#              #
#    Updated: 2020/05/27 15:01:58 by frfrey           ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

from datetime import date
from recipe import Recipe

class Book:
    """
        This class is use for browse the Recipe class
    """
    type = "Book"

    ## Constructeur of my object ##
    def __init__(self, name):
        self.name = name
        self.last_update = date.today()
        self.creation_date = date.today()
        self.recipes_list = {
            'starter': {},
            'lunch': {},
            'dessert': {}
        }

    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        for recipe_type in self.recipes_list:
            for recipe in self.recipes_list[recipe_type]:
                if (name == recipe):
                    print("Recipe:" + name + " found !")
                    print()
                    print(self.recipes_list[recipe_type][name])
                    return
        print("\033[1;36mError:\033[0m Recipe " + name + " not found !")


    def get_recipe_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        print("Recipes for this type '{}'".format(recipe_type))
        try:
            for name in self.recipes_list[recipe_type]:
                print(self.recipes_list[recipe_type][name])
                print()
        except KeyError:
            print("\033[1;36mError:\033[0m This recipe type not exist")

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if (not isinstance(recipe, Recipe)):
            print("\033[1;36mError:\033[0m Not a Recipe")
            exit()
        self.recipes_list[recipe.recipe_type][recipe.name] = recipe
        self.last_update = date.today()
        print("New recipe {}".format(recipe.name))
        print("Last update {}".format(self.last_update))
