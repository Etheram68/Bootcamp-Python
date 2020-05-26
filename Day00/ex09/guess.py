# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    guess.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: frfrey <frfrey@student.42lyon.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/05/26 16:00:27 by frfrey            #+#    #+#              #
#    Updated: 2020/05/26 16:42:45 by frfrey           ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import random


def main():
    guess = random.randint(1, 99)
    number = "0"
    attempts = 0
    print("\033[1;32mThis is an interactive guessing game!")
    print("You have to enter a number between 1 and 99", end="")
    print(" to find out the secret number.")
    print("Type\033[0m \033[1;31m'exit'\033[0m \033[1;32mto end the game.")
    print("\033[0m", end="")
    print("\033[1;36mGood luck!\033[0m")
    print()
    while (int(number) != guess and number != "exit"):
        attempts += 1
        print("\033[1;32m", end="")
        number = input("What's your guess between 1 and 99?\033[0m\n>> ")
        if (number.isnumeric() and int(number) > guess):
            print("\033[1;35mToo high!\033[0m\n")
        elif (number.isnumeric() and int(number) < guess):
            print("\033[1;36mToo low!\033[0m\n")
        elif (not number.isdigit() and number != "exit"):
            print("\033[1;31mThat's not a number.\033[0m\n")
            number = 0
        if (number == "exit"):
            print("\033[1;36mGoodbye!\033[0m")
            exit(0)
    print()
    if (int(number) == 42):
        print("\033[1;94mThe answer to the ultimate question ", end="")
        print("of life, the universe and everything is 42.\033[0m")
    else:
        print("\033[1;94mCongratulations, you've got it!\033[0m")
    if (attempts == 1):
        print("\033[1;94mCongratulations! ", end="")
        print("You got it on your first try!\033[0m")
    else:
        print("You won in", attempts, "attempts!")


if __name__ == "__main__":
    main()
