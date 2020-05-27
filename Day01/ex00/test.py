# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: frfrey <frfrey@student.42lyon.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/05/27 08:51:27 by frfrey            #+#    #+#              #
#    Updated: 2020/05/27 15:02:08 by frfrey           ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

from recipe import Recipe
from book import Book
from datetime import date


def main():
    burger = Recipe('Burger', 1, 15,
                    ['Bread burger', 'Meat', 'cheddar'],
                    'Mc Do fries would be a miracle remedy for hair loss',
                    'lunch',)
    Pizza = Recipe('Pizza', 1, 25,
                    ['Mozzarella', 'eggs', 'cheddar'],
                    'Pizza owes its popularity mainly to the second world war',
                    'lunch',)
    painperdu = Recipe('pain perdu', 1, 10,
                   ['brioche', 'oeuf', 'lait'],
                   'Pain perdu is a french dish.',
                   'dessert')
    print(burger)
    print()
    book = Book('Cookbook')
    book.add_recipe(burger)
    book.add_recipe(Pizza)
    book.add_recipe(painperdu)
    print()
    book.get_recipe_by_name('pain perdu')
    print()
    book.get_recipe_by_types('lunch')
    print()


if __name__ == "__main__":
    main()
