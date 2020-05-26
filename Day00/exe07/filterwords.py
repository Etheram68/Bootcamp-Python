# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    filterwords.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: frfrey <frfrey@student.42lyon.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/05/26 13:47:07 by frfrey            #+#    #+#              #
#    Updated: 2020/05/26 14:17:18 by frfrey           ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import sys
import re


def main():
    if (len(sys.argv) == 3):
        splitted = re.split(r'[\W]+', sys.argv[1])
        i = 0
        while(i < len(splitted)):
            if (int(sys.argv[2]) >= len(splitted[i])):
                del splitted[i]
                i -= 1
            i += 1
        print()
        print(splitted)
    else:
        print()
        print("\033[1;31mERROR\033[0m")


if __name__ == "__main__":
    main()
