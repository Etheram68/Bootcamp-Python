# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: frfrey <frfrey@student.42lyon.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/05/25 12:49:35 by frfrey            #+#    #+#              #
#    Updated: 2020/05/25 12:53:50 by frfrey           ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import sys

i = 0
for arg in sys.argv:
    if i == 1:
        string = arg
    elif i > 1:
        string += " "
        string += arg
    i += 1
print(string[::-1].swapcase())
