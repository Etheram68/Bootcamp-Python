# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    loading.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: frfrey <frfrey@student.42lyon.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/05/26 17:00:36 by frfrey            #+#    #+#              #
#    Updated: 2020/05/26 17:34:15 by frfrey           ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import time


def ft_progress(lst):
    start_time = time.time()
    iter_time = 0
    for i in lst:
        if (i == 1):
            iter_time = time.time() - start_time
        print(
            "\rETA: {:5.2f} [{:>4.0%}] [{:=>{}}{:{}}] {}/{} | elapsed time {:.2f}s"
            .format(
                (len(lst) - i) * iter_time, i / len(lst),
                '',
                i * 25 / len(lst),
                '>',
                25 - i * 25 // len(lst),
                i + 1,
                len(lst),
                time.time() - start_time),
            end="")
        yield i


def main():
    listy = range(3333)
    ret = 0
    for elem in ft_progress(listy):
        ret += elem
        time.sleep(0.0008)
    print()
    print("ret =", ret)


if __name__ == "__main__":
    main()
