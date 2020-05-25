# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operations.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: frfrey <frfrey@student.42lyon.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/05/25 15:55:11 by frfrey            #+#    #+#              #
#    Updated: 2020/05/25 17:21:18 by frfrey           ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import sys


def operations(nb1, nb2):
    """
        This function return basic operation, Sum, Differene, Product
        Quotient, Remainder.
    """
    print("Sum: \t\t{}".format(int(nb1) + int(nb2)))
    print("Difference: \t{}".format(int(nb1) - int(nb2)))
    print("Product: \t{}".format(int(nb1) * int(nb2)))
    if (int(nb1) > 0 and int(nb2) > 0):
        print("Quotient: \t{}".format(int(nb1) / int(nb2)))
    else:
        print("Quotient:\tERROR (div by zero)")
    if (int(nb1) > 0 and int(nb2) > 0):
        print("Remainder: \t{}".format(int(nb1) % int(nb2)))
    else:
        print("Remainder:\tERROR (modulo by zero)")

def main():
    if (len(sys.argv) == 1):
        print("Usage: python operation.py <number1> <number2>\n")
        print("Example:\n\tpython operation.py 10 3")
    elif (len(sys.argv) <= 3):
        if (sys.argv[1].isnumeric() and sys.argv[2].isnumeric()):
            operations(sys.argv[1], sys.argv[2])
        else:
            print("InputError: only numbers\n")
            print("Usage: python operation.py <number1> <number2>")
    else:
        print("InputError: too many arguments\n")
        print("Usage: python operation.py <number1> <number2>")

if __name__ == "__main__":
    main()
