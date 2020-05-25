# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: frfrey <frfrey@student.42lyon.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/05/25 12:49:35 by frfrey            #+#    #+#              #
#    Updated: 2020/05/25 13:56:30 by frfrey           ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import sys

if (len(sys.argv) > 1):
    i = 0
    for arg in sys.argv:
        if i == 1:
            string = arg
        elif i > 1:
            string += " "
            string += arg
        i += 1
    print(string[::-1].swapcase())
