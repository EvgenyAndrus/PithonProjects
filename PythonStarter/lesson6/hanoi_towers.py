def hanoi(n, a='A', b='B', c="C"):
    if n != 0:
        hanoi(n - 1, a, c, b)
        print('Transfer a ring from', a, 'to', c)
        hanoi(n - 1, b, a, c)


hanoi(8)
