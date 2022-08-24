"""Напишите функцию-генератор для получения n первых простых чисел."""

import time


# Решето Эратосфена
def generator(num):
    a = list(range(num + 1))
    a[1] = 0
    i = 2
    while i <= num:
        if a[i] != 0:
            yield a[i]
            for j in range(i, num + 1, i):
                a[j] = 0
        i += 1


def generator1(num):
    # в k будем хранить количество делителей
    k = 0
    # пробегаем все числа от 2 до N
    for result in range(2, num + 1):
        # пробегаем все числа от 2 до текущего
        for j in range(2, result):
            # ищем количество делителей
            if result % j == 0:
                k = k + 1
        # если делителей нет, отдаём число
        if k == 0:
            yield result
        else:
            k = 0


if __name__ == '__main__':
    response = int(input('enter num: '))
    start_time = time.time()
    for i in generator(response):
        #print(i)
        pass

    print("generator {:f} seconds ---".format((time.time() - start_time)))
    start_time = time.time()
    for i in generator1(response):
        #print(i)
        pass
    print("generator1 {:f} seconds ---".format((time.time() - start_time)))
