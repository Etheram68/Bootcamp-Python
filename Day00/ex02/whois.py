# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whois.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: frfrey <frfrey@student.42lyon.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/05/25 13:41:10 by frfrey            #+#    #+#              #
#    Updated: 2020/05/25 14:07:24 by frfrey           ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import sys

if (len(sys.argv) == 2 and sys.argv[1].isnumeric()):
    nb = int(sys.argv[1])
    if (nb == 0):
        print("I'm Zero")
    elif (nb % 2 == 0):
        print("I'm Even")
    else:
        print("I'm Odd")
else:
    print("ERROR")
