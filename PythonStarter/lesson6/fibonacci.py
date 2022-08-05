import functools


@functools.lru_cache(maxsize=None)  #  меморизация значений функций
def fib(n):                         #  (кэш для функций)
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


for index in range(1, 100):
    print(fib(index))
