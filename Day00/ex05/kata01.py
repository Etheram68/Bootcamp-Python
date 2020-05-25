# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata01.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: frfrey <frfrey@student.42lyon.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/05/25 18:01:47 by frfrey            #+#    #+#              #
#    Updated: 2020/05/25 18:12:13 by frfrey           ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

def main():
    languages = {
        'Python': 'Guido van Rossum',
        'Ruby': 'Yukihiro Matsumoto',
        'PHP': 'Rasmus Lerdorf',
    }
    for key, value in languages.items():
        print(key + "was created by" + value)


if __name__ == "__main__":
    main()
