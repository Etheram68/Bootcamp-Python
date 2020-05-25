# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: frfrey <frfrey@student.42lyon.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/05/25 15:52:55 by frfrey            #+#    #+#              #
#    Updated: 2020/05/25 15:53:02 by frfrey           ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import string


def text_analyzer(*text):
    """
        This function counts the number of upper characters, lower characters,
        punctuation and spaces in a given text.
    """
    if (len(text) <= 1):
        line = ""
        if (len(text) == 0):
            line = input("What is the text to analyse?\n>> ")
        else:
            line = text[0]
        upper = 0
        lower = 0
        punc = 0
        space = 0
        for c in line:
            if (c.islower()):
                lower += 1
            elif (c.isupper()):
                upper += 1
            elif (c.isspace()):
                space += 1
            elif(c in string.punctuation):
                punc += 1
        print("The text contains", len(line), "characters")
        print("-", upper, "upper letters")
        print("-", lower, "lower letters")
        print("-", punc, "punctuation marks")
        print("-", space, "spaces")
    else:
        print("ERROR")
