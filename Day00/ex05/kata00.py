# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata00.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: frfrey <frfrey@student.42lyon.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/05/25 17:33:01 by frfrey            #+#    #+#              #
#    Updated: 2020/05/25 17:58:36 by frfrey           ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

def	main():
    t = (16, 42, 21, 23)
    i = 0
    print("The 3 numbers are:", end=" ")
    while (i < len(t) - 1):
        print(t[i], end=", ")
        i += 1
    print(t[i])

if __name__ == "__main__":
    main()
