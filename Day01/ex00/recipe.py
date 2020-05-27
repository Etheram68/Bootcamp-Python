# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: frfrey <frfrey@student.42lyon.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/05/27 09:04:57 by frfrey            #+#    #+#              #
#    Updated: 2020/05/27 14:08:53 by frfrey           ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

class Recipe:
    """
        This class is use for read the Recipe class
    """
    type = "RECIPE"

    # Constructeur of my object #
    def __init__(self, recipeName, cookLevel, cookTime,
                 ingredients, describe, recipeType):
        if (recipeName == "" or cookLevel == "" or cookTime == ""
                or ingredients == "" or recipeType == ""):
            print("\033[1;36mError:\033[0m Only describe can be empty")
            exit(1)
        if (type(recipeName) != str):
            print("\033[1;36mError:\033[0m Name is not a string")
            exit(1)
        if (type(cookLevel) != int and (cookLevel < 1 or cookLevel > 5)):
            print("\033[1;36mError:\033[0m ", end="")
            print("Cooking_lvl must be a range to 1 and 5")
            exit(1)
        if (type(cookTime) != int and cookTime < 0):
            print("\033[1;36mError:\033[0m ", end="")
            print("Cooking_time must be a positive number")
            exit(1)
        for i in ingredients:
            if (type(i) != str or i == ""):
                print("\033[1;36mError:\033[0m ", end="")
                print("Ingredient is not a string and can be empty")
                exit(1)
        if (type(describe) != str):
            print("\033[1;36mError:\033[0m need be a string")
            exit(1)
        if (recipeType not in ["starter", "lunch", "dessert"]):
            print("\033[1;36mError:\033[0m ", end="")
            print("recip_type need be starter or lunch or dessert")
            exit(1)
        self.name = recipeName
        self.cooking_lvl = cookLevel
        self.cooking_time = cookTime
        self.ingredients = ingredients
        self.description = describe
        self.recipe_type = recipeType

    def __str__(self):
        """Return  the string to print with the recipe info"""
        txt = ("\033[1;37mRecipe of {}\n"
               "This cooking is for the level {}\n"
               "Time for cooking: {} min\nIngredients for cook {}\n"
               "Eat like for {}\nDescription:\n{}\033[0m").format(
                  self.name, self.cooking_lvl, self.cooking_time,
                  self.ingredients, self.recipe_type, self.description
              )
        return txt
